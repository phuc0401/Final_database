from db_connection import get_connection
from utils import hash_password


# ───────────────── REGISTER ─────────────────

def register_customer(phone, password, name, address):

    conn = get_connection()
    cursor = conn.cursor()

    # Kiểm tra số điện thoại đã tồn tại
    cursor.execute(
        "SELECT UserID FROM Users WHERE Username = %s",
        (phone,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        print("\n  ⚠️ Số điện thoại này đã được đăng ký!")

        cursor.close()
        conn.close()

        return False

    # Thêm vào Users
    cursor.execute("""
        INSERT INTO Users (Username, PasswordHash, Role)
        VALUES (%s, %s, 'customer')
    """, (
        phone,
        hash_password(password)
    ))

    # Thêm vào Customers
    cursor.execute("""
        INSERT INTO Customers (
            CustomerName,
            PhoneNumber,
            Address
        )
        VALUES (%s, %s, %s)
    """, (
        name,
        phone,
        address
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return True


# ───────────────── LOGIN ─────────────────

def login(username, password):

    conn = get_connection()

    # 🔥 dùng buffered=True để tránh unread result
    cursor = conn.cursor(buffered=True)

    # =========================
    # Lấy user
    # =========================
    cursor.execute("""
        SELECT Role, PasswordHash
        FROM Users
        WHERE Username = %s
    """, (username,))

    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return None, None

    role, password_hash = user

    # =========================
    # Check password
    # =========================
    if password_hash != hash_password(password):
        cursor.close()
        conn.close()
        return None, None

    # =========================
    # Lấy CustomerID
    # =========================
    cursor.execute("""
        SELECT CustomerID
        FROM Customers
        WHERE PhoneNumber = %s
    """, (username,))

    customer = cursor.fetchone()

    customer_id = customer[0] if customer else None

    cursor.close()
    conn.close()

    return role, customer_id
