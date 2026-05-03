USE sport_tickets;

-- PROCEDURE 1: Đặt vé đơn giản
DROP PROCEDURE IF EXISTS BookTicket;
DELIMITER //
CREATE PROCEDURE BookTicket(
    IN p_CustomerID INT,
    IN p_SeatID INT,
    IN p_BoxOfficeID INT
)
BEGIN
    DECLARE seat_status VARCHAR(20);

    SELECT Status INTO seat_status
    FROM Seats WHERE SeatID = p_SeatID;

    IF seat_status = 'available' THEN
        INSERT INTO Bookings(CustomerID, SeatID, BoxOfficeID, BookingDate, Status)
        VALUES (p_CustomerID, p_SeatID, p_BoxOfficeID, NOW(), 'confirmed');

        SELECT 'Đặt vé thành công!' AS Message;
    ELSE
        SELECT 'Ghế này đã được đặt rồi!' AS Message;
    END IF;
END //
DELIMITER ;

-- PROCEDURE 2: Hủy vé
DROP PROCEDURE IF EXISTS CancelBooking;
DELIMITER //
CREATE PROCEDURE CancelBooking(
    IN p_BookingID INT,
    IN p_CustomerID INT
)
BEGIN
    DECLARE booking_status VARCHAR(20);
    DECLARE owner_id INT;

    SELECT Status, CustomerID INTO booking_status, owner_id
    FROM Bookings WHERE BookingID = p_BookingID;

    IF booking_status IS NULL THEN
        SELECT '❌ Booking không tồn tại!' AS Message;
    ELSEIF owner_id != p_CustomerID THEN
        SELECT '❌ Bạn không có quyền hủy vé này!' AS Message;
    ELSEIF booking_status = 'confirmed' THEN
        UPDATE Bookings SET Status = 'canceled'
        WHERE BookingID = p_BookingID;
        UPDATE Seats
        SET Status = 'available'
        WHERE SeatID = (
            SELECT SeatID
            FROM Bookings
            WHERE BookingID = p_BookingID
        );
        SELECT '✅ Hủy vé thành công!' AS Message;
    ELSE
        SELECT '⚠️ Vé này đã bị hủy rồi!' AS Message;
    END IF;
END //
DELIMITER ;

-- PROCEDURE 3: Đặt vé an toàn có transaction
DROP PROCEDURE IF EXISTS SafeBookTicket;
DELIMITER //
CREATE PROCEDURE SafeBookTicket(
    IN p_CustomerID INT,
    IN p_SeatID INT,
    IN p_BoxOfficeID INT
)
BEGIN
    DECLARE seat_status VARCHAR(20);
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Lỗi hệ thống! Giao dịch đã được hủy.' AS Message;
    END;

    START TRANSACTION;

        SELECT Status INTO seat_status
        FROM Seats WHERE SeatID = p_SeatID
        FOR UPDATE;

        IF seat_status = 'available' THEN
            INSERT INTO Bookings(CustomerID, SeatID, BoxOfficeID, BookingDate, Status)
            VALUES (p_CustomerID, p_SeatID, p_BoxOfficeID, NOW(), 'confirmed');

            UPDATE Seats SET Status = 'booked' WHERE SeatID = p_SeatID;

            COMMIT;
            SELECT '✅ Đặt vé thành công!' AS Message;
        ELSE
            ROLLBACK;
            SELECT '❌ Ghế đã được đặt rồi!' AS Message;
        END IF;
END //
DELIMITER ;

-- Test
CALL SafeBookTicket(1, 2, 1);
CALL CancelBooking(1, 1);