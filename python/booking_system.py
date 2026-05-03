from db_connection import get_connection
from tabulate import tabulate
from utils import print_header, format_currency

# ─── SỰ KIỆN ───────────────────────────────────────

def view_all_events():
    """Xem tất cả sự kiện"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Events")
    rows = cursor.fetchall()
    print_header("DANH SÁCH SỰ KIỆN")
    print(tabulate(rows,
        headers=["ID", "Tên sự kiện", "Ngày", "Địa điểm"],
        tablefmt="grid"))
    cursor.close()
    conn.close()

def search_event(keyword):
    """Tìm kiếm sự kiện theo tên"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM Events WHERE EventName LIKE %s",
        (f"%{keyword}%",))
    rows = cursor.fetchall()
    print_header(f"KẾT QUẢ TÌM KIẾM: '{keyword}'")
    if rows:
        print(tabulate(rows,
            headers=["ID", "Tên sự kiện", "Ngày", "Địa điểm"],
            tablefmt="grid"))
    else:
        print(f"  Không tìm thấy sự kiện nào!")
    cursor.close()
    conn.close()

def view_available_seats(event_id):
    """Xem ghế còn trống theo sự kiện"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.SeatID, s.SeatNumber, t.TicketType, t.Price, s.Status
        FROM Seats s
        JOIN Tickets t ON s.TicketID = t.TicketID
                      
        WHERE s.EventID = %s AND s.Status = 'available'
    """, (event_id,))
    rows = cursor.fetchall()
    rows = [(r[0], r[1], r[2], format_currency(r[3]), r[4]) for r in rows]
    print_header(f"GHẾ TRỐNG - SỰ KIỆN {event_id}")
    if rows:
        print(tabulate(rows,
            headers=["SeatID", "Số ghế", "Loại ghế", "Giá (VND)", "Trạng thái"],
            tablefmt="grid"))
    else:
        print("  Sự kiện này không còn ghế trống!")
    cursor.close()
    conn.close()

# ─── GHẾ ─────────────────────────────────────────

def get_available_seat_ids(event_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SeatID
        FROM Seats
        WHERE EventID = %s AND Status = 'available'
    """, (event_id,))

    seats = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return seats


# ─── ĐẶT VÉ ────────────────────────────────────────

def book_ticket(customer_id,  seat_id, box_office_id):
    """Đặt vé — gọi Stored Procedure SafeBookTicket"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc('SafeBookTicket',
        [customer_id,  seat_id, box_office_id])
    for result in cursor.stored_results():
        print("\n >>>", result.fetchone()[0])
    conn.commit()
    cursor.close()
    conn.close()

def cancel_booking(booking_id, customer_id):
    """Hủy vé — gọi Stored Procedure CancelBooking"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc('CancelBooking', [booking_id, customer_id])
    for result in cursor.stored_results():
        print("\n >>>", result.fetchone()[0])
    conn.commit()
    cursor.close()
    conn.close()

def view_booking_history(customer_id):
    """Xem lịch sử đặt vé của khách hàng"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            b.BookingID,
            c.CustomerName,
            e.EventName,
            t.TicketType,
            t.Price,
            s.SeatNumber,
            b.BookingDate,
            b.Status
        FROM Bookings b
        JOIN Customers c ON b.CustomerID = c.CustomerID
        JOIN Seats s     ON b.SeatID     = s.SeatID
        JOIN Tickets t   ON s.TicketID   = t.TicketID
        JOIN Events e    ON s.EventID    = e.EventID
        
        WHERE b.CustomerID = %s
        ORDER BY b.BookingDate DESC
    """, (customer_id,))
    rows = cursor.fetchall()
    print_header(f"LỊCH SỬ ĐẶT VÉ - KHÁCH HÀNG {customer_id}")
    if rows:
        print(tabulate(rows,
            headers=["BookingID", "Khách hàng", "Sự kiện",
                     "Loại vé", "Giá (VND)", "Ghế",
                     "Ngày đặt", "Trạng thái"],
            tablefmt="grid"))
    else:
        print("  Khách hàng này chưa có đơn đặt vé nào!")
    cursor.close()
    conn.close()

def view_all_customers():
    """Xem danh sách khách hàng"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT CustomerID, CustomerName FROM Customers")
    rows = cursor.fetchall()
    print_header("DANH SÁCH KHÁCH HÀNG")
    print(tabulate(rows,
        headers=["ID", "Tên khách hàng"],
        tablefmt="grid"))
    cursor.close()
    conn.close()


def create_customer(name, phone, address):
    conn = get_connection()
    cursor = conn.cursor()

    # 🔍 Kiểm tra đã tồn tại chưa
    cursor.execute("""
        SELECT CustomerID FROM Customers WHERE PhoneNumber = %s
    """, (phone,))
    existing = cursor.fetchone()

    if existing:
        cursor.close()
        conn.close()
        return existing[0]  # 👉 dùng lại ID cũ

    # 👉 Nếu chưa có thì tạo mới
    cursor.execute("""
        INSERT INTO Customers (CustomerName, PhoneNumber, Address)
        VALUES (%s, %s, %s)
    """, (name, phone, address))

    conn.commit()
    customer_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return customer_id




def get_customer_info_by_phone(phone):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT CustomerID, CustomerName, Address
        FROM Customers
        WHERE PhoneNumber = %s
    """, (phone,))

    # Dùng fetchall để đọc hết dữ liệu
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    if rows:
        # Trả về tuple (CustomerID, CustomerName, Address)
        return rows[0]
    return None



    