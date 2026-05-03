USE sport_tickets;

INSERT INTO Events (EventName, EventDate, Venue) VALUES
('Vietnam vs Thailand', '2025-06-15', 'Sân Mỹ Đình, Hà Nội'),
('VBA Finals 2025', '2025-07-20', 'Nhà thi đấu Trống Đồng'),
('Ho Chi Minh Open Tennis', '2025-08-01', 'Sân Thống Nhất, TP.HCM'),
('SEA Games Swimming', '2025-09-10', 'Hồ bơi Quốc gia Mỹ Đình'),
('Vietnam Grand Prix MotoGP', '2025-10-05', 'Trường đua Hà Nội');

INSERT INTO Customers (CustomerName, PhoneNumber, Address) VALUES
('Nguyễn Văn An', '0901234567', 'Hà Nội'),
('Trần Thị Bích', '0912345678', 'TP. Hồ Chí Minh'),
('Lê Văn Cường', '0923456789', 'Đà Nẵng'),
('Phạm Thị Dung', '0934567890', 'Hải Phòng'),
('Hoàng Văn Em', '0945678901', 'Cần Thơ'),
('Vũ Thị Phương', '0956789012', 'Huế'),
('Đặng Văn Giang', '0967890123', 'Nha Trang');

INSERT INTO Tickets (EventID, TicketType, Price) VALUES
(1, 'VIP', 500000),
(1, 'Standard', 200000),
(1, 'Economy', 100000),
(2, 'VIP', 350000),
(2, 'Standard', 150000),
(3, 'VIP', 450000),
(4, 'Standard', 120000),
(5, 'VIP', 600000);

INSERT INTO Seats (EventID, SeatNumber, Status, TicketID) VALUES
(1, 'A1', 'available', 1),
(1, 'A2', 'available', 1),
(1, 'B1', 'available', 2),
(1, 'B2', 'available', 2),
(1, 'C1', 'available', 1),
(2, 'A1', 'available', 4),
(2, 'B1', 'available', 5),
(3, 'A1', 'available', 6),
(4, 'B1', 'available', 7),
(5, 'A1', 'available', 8);

INSERT INTO BoxOffices (OfficeName, Address) VALUES
('Quầy vé Mỹ Đình', 'Số 1 Lê Đức Thọ, Nam Từ Liêm, Hà Nội'),
('Quầy vé Thống Nhất', 'Số 138 Đường 3/2, Quận 10, TP.HCM'),
('Quầy vé Online', 'ticketsports.vn');

INSERT INTO Bookings (CustomerID, SeatID, BoxOfficeID, BookingDate, Status) VALUES
(1, 1, 1, '2025-05-01 10:00:00', 'confirmed'),
(2, 3, 2, '2025-05-02 11:00:00', 'confirmed'),
(3, 5, 3, '2025-05-03 09:30:00', 'confirmed'),
(4, 6, 1, '2025-05-04 14:00:00', 'confirmed'),
(5, 7, 2, '2025-05-05 15:30:00', 'canceled'),
(6, 8, 3, '2025-05-06 08:00:00', 'confirmed'),
(7, 9, 1, '2025-05-07 16:00:00', 'confirmed');

INSERT INTO Users (Username, PasswordHash, Role) VALUES
('admin1',    SHA2('1234', 256), 'admin'),
('manager1',  SHA2('1234', 256), 'manager'),
('cashier1',  SHA2('1234', 256), 'cashier'),
('0901234567', SHA2('1234', 256), 'customer');