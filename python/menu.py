# menu.py
from utils import print_header, print_divider

def print_menu(role):
    print_header("SPORTS TICKETING MANAGEMENT SYSTEM")
    print("── SỰ KIỆN ──────────────────────")
    print("1. Xem sự kiện")
    print("2. Tìm kiếm sự kiện")
    print("3. Xem ghế trống")

    if role in ("customer","cashier","manager","admin", "guest"):
        print("── ĐẶT VÉ ───────────────────────")
        print("4. Đặt vé")
        print("5. Hủy vé")
        print("6. Lịch sử đặt vé")

    if role in ("cashier","manager","admin"):
        print("7. Danh sách khách hàng")

    if role in ("manager","admin"):
        print("── BÁO CÁO ──────────────────────")
        print("8. Báo cáo doanh thu")
        print("9. Doanh thu chi tiết sự kiện")
        print("10. Thống kê theo loại vé")
        print("11. Báo cáo ghế trống")
    
        

    print("0. Thoát")
    print_divider()
