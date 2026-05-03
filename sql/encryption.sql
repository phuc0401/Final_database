USE sport_tickets;

-- Tạo bảng lưu thông tin đã mã hóa
CREATE TABLE IF NOT EXISTS CustomerSecure (
    SecureID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    EncryptedPhone VARBINARY(255),
    EncryptedAddress VARBINARY(255),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Mã hóa số điện thoại và địa chỉ bằng AES
INSERT INTO CustomerSecure (CustomerID, EncryptedPhone, EncryptedAddress)
SELECT
    CustomerID,
    AES_ENCRYPT(PhoneNumber, 'SportKey2025'),
    AES_ENCRYPT(Address, 'SportKey2025')
FROM Customers;

-- Xem dữ liệu đã mã hóa (ký tự lạ)
SELECT * FROM CustomerSecure;

-- Giải mã để đọc
SELECT
    c.CustomerName,
    CAST(AES_DECRYPT(cs.EncryptedPhone, 'SportKey2025') AS CHAR) AS PhoneNumber,
    CAST(AES_DECRYPT(cs.EncryptedAddress, 'SportKey2025') AS CHAR) AS Address
FROM CustomerSecure cs
JOIN Customers c ON cs.CustomerID = c.CustomerID;