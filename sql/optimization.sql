USE sport_tickets;

-- Xem query đang chậm thế nào trước khi tối ưu
EXPLAIN SELECT * FROM Bookings
WHERE CustomerID = 1 AND Status = 'confirmed';

EXPLAIN SELECT * FROM Seats
WHERE EventID = 1 AND Status = 'available';

-- Chạy lại sau khi đã tạo index để so sánh
-- (cột "key" sẽ hiện tên index thay vì NULL)
EXPLAIN SELECT * FROM Bookings
WHERE CustomerID = 1 AND Status = 'confirmed';

-- Xem tất cả index hiện có
SHOW INDEX FROM Bookings;
SHOW INDEX FROM Seats;
SHOW INDEX FROM Tickets;