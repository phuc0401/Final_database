USE sport_tickets;

-- Tìm ghế còn trống nhanh hơn
CREATE INDEX idx_seat_status
ON Seats(Status);

-- Tìm lịch sử mua vé của khách nhanh hơn
CREATE INDEX idx_booking_customer
ON Bookings(CustomerID);

-- Tìm vé theo sự kiện nhanh hơn
CREATE INDEX idx_ticket_event
ON Tickets(EventID);

-- Thêm composite index cho query phổ biến
CREATE INDEX idx_booking_customer_status
ON Bookings(CustomerID, Status);

-- Index cho tìm ghế theo sự kiện + trạng thái
CREATE INDEX idx_seat_event_status
ON Seats(EventID, Status);

-- Kiểm tra
SHOW INDEX FROM Seats;
SHOW INDEX FROM Bookings;
SHOW INDEX FROM Tickets;
