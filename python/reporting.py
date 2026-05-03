from db_connection import get_connection
from tabulate import tabulate
from utils import print_header, format_currency

def revenue_report():
    """Báo cáo doanh thu theo từng sự kiện — dùng View"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RevenueByEvent")
    rows = cursor.fetchall()
    print_header("BÁO CÁO DOANH THU THEO SỰ KIỆN")
    if rows:
        print(tabulate(rows,
            headers=["ID", "Sự kiện", "Ngày",
                     "Địa điểm", "Số vé bán", "Doanh thu (VND)"],
            tablefmt="grid"))
    else:
        print("  Chưa có dữ liệu doanh thu!")
    cursor.close()
    conn.close()

def event_detail_report(event_id):
    """Doanh thu chi tiết 1 sự kiện — dùng UDF"""
    conn = get_connection()
    cursor = conn.cursor()

    # Lấy tên sự kiện
    cursor.execute(
        "SELECT EventName FROM Events WHERE EventID = %s",
        (event_id,))
    event = cursor.fetchone()

    if not event:
        print("\n  Không tìm thấy sự kiện!")
        cursor.close()
        conn.close()
        return

    # Gọi 2 UDF đã tạo trong MySQL
    cursor.execute("""
        SELECT
            GetTotalRevenue(%s)     AS revenue,
            GetTotalTicketsSold(%s) AS tickets_sold
    """, (event_id, event_id))
    row = cursor.fetchone()

    print_header(f"CHI TIẾT: {event[0]}")
    print(f"  Tổng doanh thu : {format_currency(row[0])}")
    print(f"  Số vé đã bán   : {row[1]} vé")

    cursor.close()
    conn.close()

def ticket_type_stats():
    """Thống kê vé theo loại"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            t.TicketType            AS LoaiVe,
            COUNT(b.BookingID)      AS SoLuong,
            SUM(t.Price)            AS DoanhThu
        FROM Bookings b
        JOIN Seats s   ON b.SeatID = s.SeatID
        JOIN Tickets t ON s.TicketID = t.TicketID
        WHERE b.Status = 'confirmed'
        GROUP BY t.TicketType
        ORDER BY DoanhThu DESC
    """)
    rows = cursor.fetchall()
    print_header("THỐNG KÊ VÉ THEO LOẠI")
    print(tabulate(rows,
        headers=["Loại vé", "Số lượng bán", "Doanh thu (VND)"],
        tablefmt="grid"))
    cursor.close()
    conn.close()

def available_seats_report():
    """Báo cáo ghế còn trống — dùng View"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM AvailableSeats")
    rows = cursor.fetchall()
    print_header("BÁO CÁO GHẾ CÒN TRỐNG")
    if rows:
        print(tabulate(rows,
            headers=["Sự kiện", "SeatID", "Số ghế", "Loại ghế", "Trạng thái"],
            tablefmt="grid"))
    else:
        print("  Không còn ghế trống!")
    cursor.close()
    conn.close()