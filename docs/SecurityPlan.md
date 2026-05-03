# 🔐 Security Plan
## Sports Ticketing Management System

This document describes the security architecture and protection mechanisms implemented in the Sports Ticketing Management System.

The system was designed to provide:
- secure customer authentication
- protected booking operations
- transaction consistency
- privacy protection
- role-based access control
- safe ticket management

The application supports:
- customer accounts
- login/register system
- OTP verification
- role-based administration

---

# 1️⃣ Authentication System

## Customer Registration

The system allows customers to create personal accounts.

During registration, users provide:
- full name
- phone number
- address
- username
- password

---

## Password Protection

Passwords are not stored as plain text.

The system uses:
- password hashing
- secure authentication validation

This reduces the risk of:
- password theft
- credential leakage

---

## Login System

Customers must log in before accessing protected features.

After successful login, customers can:
- book tickets
- view booking history
- cancel bookings
- manage their information

---

## Authentication Workflow

### Step 1
User enters:
- username
- password

### Step 2
System validates credentials.

### Step 3
If authentication succeeds:
- access is granted

Otherwise:
- login is denied

---

## Security Benefits

- Prevents unauthorized access
- Protects customer bookings
- Supports account-based operations
- Improves user experience

---

# 2️⃣ OTP Verification System

## Purpose

The system adds an additional verification layer using OTP (One-Time Password).

OTP verification is required before:
- viewing booking history
- canceling tickets
- performing sensitive operations

---

## OTP Workflow

### Step 1
Customer enters registered phone number.

### Step 2
System generates temporary OTP code.

### Step 3
Customer enters OTP.

### Step 4
System validates OTP.

If valid:
- operation continues

Otherwise:
- access is denied

---

## Security Advantages

- Adds multi-layer authentication
- Prevents unauthorized booking access
- Protects customer operations
- Reduces account abuse risk

---

# 3️⃣ Authorization and Access Control

The system implements role-based access control.

Different users have different permissions.

---

# 👤 Customer Role

Customers can:
- register accounts
- log in
- book tickets
- cancel their own bookings
- view personal booking history

Customers cannot:
- access admin functions
- modify database structure
- access other customers’ data

---

# 💼 Cashier Role

Cashiers can:
- process bookings
- assist ticket sales
- check seat availability

Cashiers cannot:
- access system administration
- modify security settings

---

# 📊 Manager Role

Managers can:
- access reports
- analyze ticket sales
- monitor revenue statistics

Managers cannot:
- directly modify database schema
- manage system security

---

# 🛠️ Admin Role

Admins have:
- full system access
- database administration rights
- user management permissions
- security configuration permissions

---

# 4️⃣ Booking Ownership Validation

## Problem

Without ownership validation:
- users could cancel other customers’ tickets
- unauthorized booking access could occur

---

## Solution

The system verifies:
- booking ownership
- customer identity
- booking validity

before allowing cancellation.

---

## Validation Process

Before canceling a booking, the system checks:

### ✅ Booking exists
The booking must exist in the database.

### ✅ Booking belongs to logged-in customer
Only the booking owner can cancel the ticket.

### ✅ Booking status is valid
Only confirmed bookings can be canceled.

Canceled bookings cannot be canceled again.

---

## Security Benefits

- Prevents ticket fraud
- Prevents unauthorized cancellation
- Protects customer purchases

---

# 5️⃣ Secure Transaction Handling

## Problem

Multiple users may try to:
- book the same seat
- cancel bookings simultaneously

This may create:
- inconsistent data
- double booking
- invalid seat status

---

## Solution

The system uses:
- MySQL transactions
- stored procedures
- rollback protection

---

## Stored Procedures

| Procedure | Purpose |
|---|---|
| SafeBookTicket | Secure ticket booking |
| CancelBooking | Secure cancellation |
| RegisterCustomer | Secure customer creation |

---

## Transaction Safety

Booking operations include:
- booking creation
- seat status update
- payment processing logic

If any step fails:
- transaction is rolled back

This guarantees:
- data consistency
- reliable operations

---

# 6️⃣ Trigger-Based Protection

The database uses triggers to automate critical operations.

---

## Booking Trigger

After successful booking:
- seat status automatically changes

```text
available → booked
```

---

## Cancellation Trigger

After cancellation:
- seat becomes available again

```text
booked → available
```

---

## Advantages

Triggers:
- reduce human errors
- improve consistency
- automate database synchronization

---

# 7️⃣ Data Privacy Protection

## Sensitive Information Protection

The system avoids exposing sensitive customer information.

Protected data includes:
- phone numbers
- addresses
- passwords

---

## Public Console Restrictions

Public interfaces only display:
- customer names
- booking information

Sensitive data is hidden.

---

## Password Security

Passwords are:
- hashed before storage
- never displayed publicly
- never stored as plain text

---

# 8️⃣ Input Validation

Input validation prevents:
- invalid operations
- malicious inputs
- accidental mistakes

---

## Validation Examples

### Event Validation
Users cannot:
- select invalid EventIDs
- book unavailable events

---

### Seat Validation
Users cannot:
- choose non-existing seats
- select booked seats

---

### Booking Validation
Users cannot:
- cancel invalid bookings
- access other users’ bookings

---

### Login Validation
Users cannot:
- log in with incorrect credentials
- bypass authentication checks

---

# 9️⃣ Database Security

## Database Roles

The system separates permissions using MySQL roles.

---

## Principle of Least Privilege

Each role receives only the permissions required for its tasks.

This reduces:
- security risks
- accidental database damage

---

## SQL Injection Protection

Parameterized queries are used throughout the application.

Example:

```python
cursor.execute(
    "SELECT * FROM Customers WHERE PhoneNumber = %s",
    (phone,)
)
```

Benefits:
- prevents SQL injection attacks
- improves query safety

---

# 🔟 Backup and Disaster Recovery

## Backup Strategy

Database backup scripts are included in:

```text
sql/backup_restore.sql
```

---

## Recovery Objectives

The recovery plan ensures:
- fast restoration
- protection against data loss
- operational continuity

---

# 1️⃣1️⃣ Performance and Security Optimization

Indexes are used on:
- CustomerID
- EventID
- SeatID
- BookingID

Benefits:
- faster queries
- reduced server load
- improved booking speed

---

# 1️⃣2️⃣ Future Security Improvements

Future enhancements may include:

---

## Real SMS OTP Integration
Current OTP uses:
- console simulation

Future versions may use:
- Twilio API
- Firebase Authentication

---

## JWT Authentication
For future web applications:
- token-based login
- secure sessions

---

## QR Code Verification
Future tickets may include:
- encrypted QR codes
- anti-fraud scanning

---

## HTTPS Protection
Future web deployment may include:
- HTTPS encryption
- secure cookies
- CSRF protection

---

# ✅ Conclusion

The Sports Ticketing Management System implements a multi-layer security architecture to protect:
- customer accounts
- ticket bookings
- payment-related operations
- sensitive information

The system includes:
- authentication
- OTP verification
- authorization control
- secure transactions
- protected database operations
- role-based access management

These mechanisms improve:
- system reliability
- operational safety
- customer privacy
- overall trustworthiness