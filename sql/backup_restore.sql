-- File này chạy trên Command Prompt, không phải Workbench!

-- BACKUP (chạy trong terminal):
-- mysqldump -u root -p sport_tickets > backup_sport_2025.sql

-- RESTORE (chạy trong terminal):
-- mysql -u root -p sport_tickets < backup_sport_2025.sql

-- Kiểm tra backup trong Workbench:
USE sport_tickets;
SHOW TABLES;
SELECT COUNT(*) FROM Bookings;
SELECT COUNT(*) FROM Customers;
SELECT COUNT(*) FROM Events;