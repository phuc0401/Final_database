USE sport_tickets;

-- FUNCTION 1: Tổng doanh thu của 1 sự kiện
DROP FUNCTION IF EXISTS GetTotalRevenue;
DELIMITER //
CREATE FUNCTION GetTotalRevenue(p_EventID INT)
RETURNS DECIMAL(12,2)
DETERMINISTIC
BEGIN
    DECLARE total DECIMAL(12,2);

    SELECT COALESCE(SUM(t.Price), 0) INTO total
    FROM Bookings b
    JOIN Seats s ON b.SeatID = s.SeatID
    JOIN Tickets t ON s.TicketID = t.TicketID
    WHERE s.EventID = p_EventID
    AND b.Status = 'confirmed';

    RETURN total;
END //
DELIMITER ;

-- FUNCTION 2: Tổng số vé đã bán của 1 sự kiện
DROP FUNCTION IF EXISTS GetTotalTicketsSold;
DELIMITER //
CREATE FUNCTION GetTotalTicketsSold(p_EventID INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;

    SELECT COUNT(b.BookingID) INTO total
    FROM Bookings b
    JOIN Seats s ON b.SeatID = s.SeatID
    WHERE s.EventID = p_EventID
    AND b.Status = 'confirmed';

    RETURN IFNULL(total, 0);
END //
DELIMITER ;

-- Test dùng function trong query
SELECT
    EventName,
    GetTotalRevenue(EventID) AS DoanhThu,
    GetTotalTicketsSold(EventID) AS SoVeDaBan
FROM Events;