

-- VIEW 1: Doanh thu theo từng sự kiện
CREATE VIEW RevenueByEvent AS
SELECT
    e.EventID,
    e.EventName,
    e.EventDate,
    e.Venue,
    COUNT(b.BookingID) AS TotalTicketsSold,
    COALESCE(SUM(
        CASE WHEN b.BookingID IS NOT NULL THEN t.Price ELSE 0 END
    ), 0) AS TotalRevenue
FROM Events e
LEFT JOIN Seats s ON e.EventID = s.EventID
LEFT JOIN Bookings b ON s.SeatID = b.SeatID AND b.Status = 'confirmed'
LEFT JOIN Tickets t ON s.TicketID = t.TicketID
GROUP BY e.EventID, e.EventName, e.EventDate, e.Venue;

-- VIEW 2: Ghế còn trống theo từng sự kiện
CREATE VIEW AvailableSeats AS
SELECT
    e.EventName,
    s.SeatID,
    s.SeatNumber,
    t.TicketType,
    s.Status
FROM Seats s
JOIN Events e ON s.EventID = e.EventID
JOIN Tickets t ON s.TicketID = t.TicketID
WHERE s.Status = 'available';

-- VIEW 3: Lịch sử mua vé của khách hàng
CREATE VIEW CustomerBookingHistory AS
SELECT
    c.CustomerID,
    c.CustomerName,
    c.PhoneNumber,
    e.EventName,
    t.TicketType,
    t.Price,
    s.SeatNumber,
    b.BookingDate,
    b.Status
FROM Bookings b
JOIN Customers c ON b.CustomerID = c.CustomerID
JOIN Seats s ON b.SeatID = s.SeatID
JOIN Tickets t ON s.TicketID = t.TicketID
JOIN Events e ON s.EventID = e.EventID;

-- Kiểm tra
SELECT * FROM RevenueByEvent;
SELECT * FROM AvailableSeats;
SELECT * FROM CustomerBookingHistory;
