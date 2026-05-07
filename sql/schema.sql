DROP DATABASE IF EXISTS sport_tickets;
CREATE DATABASE sport_tickets
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE sport_tickets;

CREATE TABLE Events (
  EventID INT AUTO_INCREMENT,
  EventName VARCHAR(100) NOT NULL,
  EventDate DATE NOT NULL,
  Venue VARCHAR(255) NOT NULL,
  PRIMARY KEY (EventID)
);

CREATE TABLE Customers (
  CustomerID INT AUTO_INCREMENT,
  CustomerName VARCHAR(100) NOT NULL,
  PhoneNumber VARCHAR(20) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PRIMARY KEY (CustomerID)
);

CREATE TABLE Tickets (
  TicketID INT AUTO_INCREMENT,
  TicketType VARCHAR(50) NOT NULL,
  Price DECIMAL(10,2) NOT NULL,
  EventID INT NOT NULL,
  PRIMARY KEY (TicketID),
  FOREIGN KEY (EventID) REFERENCES Events(EventID),
  UNIQUE (EventID, TicketType)
);

CREATE TABLE Seats (
  SeatID INT AUTO_INCREMENT,
  SeatNumber VARCHAR(10) NOT NULL,
  Status ENUM('available', 'booked') NOT NULL,
  EventID INT NOT NULL,
  TicketID INT NOT NULL,
  PRIMARY KEY (SeatID),
  FOREIGN KEY (EventID) REFERENCES Events(EventID),
  FOREIGN KEY (TicketID) REFERENCES Tickets(TicketID),
  UNIQUE (EventID, SeatNumber)
);

CREATE TABLE BoxOffices (
  BoxOfficeID INT AUTO_INCREMENT,
  OfficeName VARCHAR(100) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  PRIMARY KEY (BoxOfficeID)
);

CREATE TABLE Bookings (
  BookingID INT AUTO_INCREMENT,
  SeatID INT NOT NULL,
  BookingDate DATETIME DEFAULT CURRENT_TIMESTAMP,
  Status ENUM('confirmed', 'canceled') NOT NULL,
  CustomerID INT NOT NULL,
  BoxOfficeID INT NOT NULL,
  PRIMARY KEY (BookingID),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (BoxOfficeID) REFERENCES BoxOffices(BoxOfficeID),
  FOREIGN KEY (SeatID) REFERENCES Seats(SeatID)
);

CREATE TABLE Users (
  UserID INT AUTO_INCREMENT PRIMARY KEY,
  Username VARCHAR(50) UNIQUE NOT NULL ,
  PasswordHash VARCHAR(255) NOT NULL,
  Role ENUM('customer','cashier','manager','admin')
);