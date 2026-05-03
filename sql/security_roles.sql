USE sport_tickets;

-- Xóa user cũ nếu có
DROP USER IF EXISTS 'cashier'@'localhost';
DROP USER IF EXISTS 'manager'@'localhost';
DROP USER IF EXISTS 'admin_user'@'localhost';

-- Tạo 3 user
CREATE USER 'cashier'@'localhost' IDENTIFIED BY 'Cashier@123';
CREATE USER 'manager'@'localhost' IDENTIFIED BY 'Manager@123';
CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'Admin@123';

-- CASHIER: chỉ xem và đặt vé
GRANT SELECT ON sport_tickets.Events TO 'cashier'@'localhost';
GRANT SELECT ON sport_tickets.Seats TO 'cashier'@'localhost';
GRANT SELECT ON sport_tickets.Tickets TO 'cashier'@'localhost';
GRANT SELECT ON sport_tickets.Customers TO 'cashier'@'localhost';
GRANT SELECT, INSERT ON sport_tickets.Bookings TO 'cashier'@'localhost';

-- MANAGER: quản lý nhưng không xóa được
GRANT SELECT, INSERT, UPDATE ON sport_tickets.* TO 'manager'@'localhost';

-- ADMIN: toàn quyền
GRANT ALL PRIVILEGES ON sport_tickets.* TO 'admin_user'@'localhost';

FLUSH PRIVILEGES;

-- Kiểm tra
SHOW GRANTS FOR 'cashier'@'localhost';
SHOW GRANTS FOR 'manager'@'localhost';
SHOW GRANTS FOR 'admin_user'@'localhost';