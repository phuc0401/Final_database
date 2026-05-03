USE sport_tickets;

-- TRIGGER 1: Tự động cập nhật ghế thành 'booked' khi có booking mới
DROP TRIGGER IF EXISTS AfterBookingInsert;
DELIMITER //
CREATE TRIGGER AfterBookingInsert
AFTER INSERT ON Bookings
FOR EACH ROW
BEGIN
    IF NEW.Status = 'confirmed' THEN
        UPDATE Seats SET Status = 'booked'
        WHERE SeatID = NEW.SeatID;
    END IF;
END //
DELIMITER ;

-- TRIGGER 2: Tự động trả ghế về 'available' khi hủy vé
DROP TRIGGER IF EXISTS AfterBookingCancel;
DELIMITER //
CREATE TRIGGER AfterBookingCancel
AFTER UPDATE ON Bookings
FOR EACH ROW
BEGIN
    IF NEW.Status = 'canceled' AND OLD.Status = 'confirmed' THEN
        UPDATE Seats SET Status = 'available'
        WHERE SeatID = NEW.SeatID;
    END IF;
END //
DELIMITER ;

-- Test trigger: hủy booking và xem ghế có tự động available không
UPDATE Bookings SET Status = 'canceled' WHERE BookingID = 4;
SELECT * FROM Seats WHERE SeatID = 6;  -- phải thấy Status = 'available'