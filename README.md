# 🏟️ Sports Ticketing Management System

A console-based sports ticket booking and management system developed using **Python** and **MySQL**.

This project was developed for the **Database Systems / DATCOM Lab** course at  
**National Economics University (NEU)**.

---

# 📌 Project Objective

The system helps organizers manage:

- Sports events
- Ticket sales
- Seat booking
- Customers
- Box office operations
- Revenue reporting

The application focuses on:
- Fast ticket booking
- Secure transactions
- Customer verification
- Real-time seat tracking

---

# 🚀 Main Features

## 🎫 Ticket Booking
- View available events
- Choose seats
- Book tickets
- Auto-update seat status

---

## 👤 Customer Management
- Auto-detect customers using phone numbers
- Save booking history
- Prevent duplicate customer records

---

## 🔐 Security Features
- OTP verification before:
  - viewing booking history
  - canceling tickets
- Ownership validation
- Protected customer information
- Transaction-safe booking process

---

## 📊 Reporting System
- Revenue reports
- Event popularity statistics
- Ticket type statistics
- Seat availability reports

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| MySQL | Database management |
| mysql-connector-python | Database connection |
| tabulate | Console table display |

---

# 🗂️ Project Structure

```text
sports_ticketing_project/
│
├── docs/
│   ├── PerformanceOptimization.md
│   ├── SecurityPlan.md
│   
│   
│
├── python/
│   ├── auth.py
│   ├── booking_system.py
│   ├── db_connection.py
│   ├── menu.py
│   ├── otp_service.py
│   ├── reporting.py
│   ├── ui_console.py
│   └── utils.py
│
├── sql/
│   ├── schema.sql
│   ├── sample_data.sql
│   ├── procedures.sql
│   ├── triggers.sql
│   ├── functions.sql
│   ├── views.sql
│   ├── indexes.sql
│   ├── security_roles.sql
│   ├── encryption.sql
│   ├── optimization.sql
│   └── backup_restore.sql
│
└── README.md
```

---

# 🧩 Database Design

## Main Tables

| Table | Description |
|---|---|
| Events | Sports events information |
| Tickets | Ticket types and prices |
| Customers | Customer information |
| Seats | Seat management |
| Bookings | Booking transactions |
| BoxOffices | Ticket office locations |

---

# ⚡ Advanced Database Features

## ✅ Stored Procedures
- `SafeBookTicket`
- `CancelBooking`

Used to:
- ensure transaction consistency
- automate booking logic
- prevent invalid operations

---

## ✅ Triggers
Triggers automatically:
- update seat status after booking
- restore seat availability after cancellation

---

## ✅ Views
Views are used for:
- revenue reports
- available seats
- sold-out events

---

## ✅ Functions
Custom MySQL functions calculate:
- total revenue
- total tickets sold

---

## ✅ Indexes
Indexes improve performance for:
- seat searching
- customer history lookup
- booking operations

---

# 🔐 Security Implementation

The system includes multiple security mechanisms.

## OTP Verification
Users must verify their phone number using OTP before:
- viewing booking history
- canceling bookings

---

## Ownership Validation
Customers can only:
- view their own bookings
- cancel their own tickets

---

## Data Protection
Sensitive customer information:
- phone numbers
- addresses

is hidden from public screens.

---

## Database Roles

Three database roles are defined:

| Role | Permissions |
|---|---|
| Admin | Full access |
| Manager | Reporting access |
| Cashier | Ticket sales operations |

---

# 📈 Performance Optimization

Optimization techniques include:

- Indexing frequently queried columns
- Optimized JOIN queries
- Stored procedures for faster execution
- Transaction-safe operations

---

# 🖥️ Console Interface

The system provides a console-based interface for:

- event searching
- seat booking
- ticket cancellation
- reporting

---





# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/phuc0401/Final_database.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install mysql-connector-python tabulate
```

---

## 3️⃣ Create Database

Run SQL files in this order:

```text
schema.sql
sample_data.sql
functions.sql
procedures.sql
triggers.sql
views.sql
indexes.sql
```

---

## 4️⃣ Configure Database Connection

Edit:

```text
python/db_connection.py
```

Update:

```python
host=
user=
password=
database=
```

---

## 5️⃣ Run Application

```bash
cd python
python ui_console.py
```

---




# 🔮 Future Improvements

Possible future enhancements:

- Flask web application
- QR code tickets
- Real SMS OTP integration
- Online payment gateway
- Mobile application
- Email notifications

---

# 👨‍💻 Author

**Dương Huy Phúc**  
National Economics University (NEU)

---

# 📚 References

- MySQL Documentation
- Python Documentation
- mysql-connector-python Documentation
- DATCOM Lab Materials


