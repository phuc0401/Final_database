from booking_system import (
    view_all_events, search_event, view_available_seats,
    book_ticket, cancel_booking, get_customer_info_by_phone,
    view_booking_history, view_all_customers,
    get_available_seat_ids, create_customer
)
from auth import login
from menu import print_menu
from reporting import (
    revenue_report, event_detail_report,
    ticket_type_stats, available_seats_report
)
from utils import print_header, print_divider, confirm_action
from db_connection import get_connection
from otp_service import generate_otp, verify_otp
from auth import login, register_customer



def get_ticket_info(seat_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            t.TicketID,
            t.TicketType,
            t.Price
        FROM Seats s
        JOIN Tickets t ON s.TicketID = t.TicketID
        WHERE s.SeatID = %s
    """, (seat_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def main():
    while True:
        print("\n  Chào mừng đến với hệ thống bán vé thể thao!")
        print("1. Đăng nhập ")
        print("2. Đăng ký tài khoản ")
        print("3. Guest mode")
        print("0. Thoát")

        choice = input("Chọn (1/2/3/0): ").strip()

        role = None
        customer_id = None

        if choice == "0":
            print("\n  👋 Tạm biệt! Hẹn gặp lại!\n")
            break

        elif choice == "1":
            username = input("  Phone Number: ")
            password = input("  Password: ")
            role, customer_id = login(username, password)
            if not role:
                print("\n  ❌ Sai tài khoản hoặc mật khẩu!")
                continue   # quay lại menu chính
            print(f"\n  ✅ Đăng nhập thành công!!!")

        elif choice == "2":
            phone = input("  Số điện thoại: ").strip()
            name = input("  Tên khách hàng: ").strip()
            address = input("  Địa chỉ: ").strip()
            password = input("  Mật khẩu: ").strip()
            confirm_password = input("  Xác nhận mật khẩu: ").strip()

            if not phone or not name or not address or not password or not confirm_password:
                print("\n  ❌ Vui lòng nhập đầy đủ thông tin!")
                continue


            if password != confirm_password:
                print("\n  ❌ Mật khẩu xác nhận không khớp. Vui lòng thử lại!\n")
                continue   # quay lại menu chính

            if get_customer_info_by_phone(phone):
                print("\n  ⚠️ Số điện thoại này đã được đăng ký. Vui lòng dùng số khác hoặc đăng nhập.")
                continue   # quay lại menu chính

            if register_customer(phone, password, name, address):
                print("\n  ✅ Đăng ký thành công! Vui lòng đăng nhập lại bằng số điện thoại + mật khẩu.\n")

            continue   # quay lại menu chính

        elif choice == "3":
            print("\n  ✅ Vào hệ thống với tư cách Guest\n")
            role = "guest"

        # Nếu đã đăng nhập hoặc chọn Guest thì vào vòng lặp menu chức năng
        if role:
            while True:
                print_menu(role)
                sub_choice = input("  Chọn chức năng: ").strip()

                try:
                    if sub_choice == "1":
                        view_all_events()

                    elif sub_choice == "2":
                        keyword = input("  Nhập tên sự kiện cần tìm: ").strip()
                        search_event(keyword)

                    elif sub_choice == "3":
                        view_all_events()
                        eid = int(input("  Nhập EventID: "))
                        view_available_seats(eid)

                    elif sub_choice == "4":
                        # Đặt vé
                        view_all_events()
                        eid = int(input("  Nhập EventID muốn đặt vé: "))
                        view_available_seats(eid)

                        seats = get_available_seat_ids(eid)
                        if not seats:
                            print("\n  ❌ Sự kiện này không còn ghế trống!")
                            continue

                        sid = int(input("  Nhập SeatID muốn chọn: "))
                        if sid not in seats:
                            print("\n  ❌ SeatID không hợp lệ!")
                            continue

                        ticket = get_ticket_info(sid)
                        if not ticket:
                            print("\n  Không tìm thấy vé!")
                            continue

                        print(f"\n  Loại vé : {ticket[1]}")
                        print(f"  Giá     : {ticket[2]:,} VND")

                        # Nếu là guest thì nhập số điện thoại và OTP
                        if role == "guest":
                            phone = input("  Nhập số điện thoại: ")

                            # 🔐 Check số đã có account chưa
                            conn = get_connection()
                            cursor = conn.cursor()
                            cursor.execute("""
                                SELECT UserID
                                FROM Users
                                WHERE  Username = %s
                            
                            """, (phone,))
                            existing_account = cursor.fetchone()
                            cursor.close()
                            conn.close()

                            if existing_account:
                              print("\n  ⚠️ Số điện thoại này đã liên kết với tài khoản.")
                              print("  👉 Vui lòng đăng nhập để tiếp tục!")
                              continue

  


                            customer = get_customer_info_by_phone(phone)

                            if customer:
                                cid, name, address = customer
                                
                            else:
                                print("\n  ➕ Khách hàng mới")
                                name = input("  Nhập tên: ")
                                address = input("  Nhập địa chỉ: ")
                                cid = create_customer(name, phone, address)

                            generate_otp(phone)
                            user_otp = input("  Nhập OTP: ")
                            if not verify_otp(phone, user_otp):
                                print("\n  ❌ OTP không đúng!")
                                continue
                        else:
                            # Nếu đã đăng nhập thì dùng luôn customer_id
                            cid = customer_id 

                        print("\n  Chọn quầy vé:")
                        print("  1. Quầy vé Mỹ Đình")
                        print("  2. Quầy vé Thống Nhất")
                        print("  3. Online")
                        bid = int(input("  Nhập lựa chọn (1/2/3): "))

                        if confirm_action("Xác nhận đặt vé?"):
                            book_ticket(cid, sid, bid)

                    elif sub_choice == "5":
                        # Guest phải OTP
                        if role == "guest":
                           phone = input("  Nhập số điện thoại: ")
                            # 🔐 Check số này có account không
                           conn = get_connection()
                           cursor = conn.cursor()

                           cursor.execute("""
                              SELECT UserID
                              FROM Users
                              WHERE Username = %s
                           """, (phone,))

                           existing_account = cursor.fetchone()

                           cursor.close()
                           conn.close()

                         # ❌ Nếu có account → bắt login
                           if existing_account:
                             print("\n  ⚠️ Số điện thoại này thuộc tài khoản đã đăng ký.")
                             print("  👉 Vui lòng đăng nhập để hủy vé!")
                             continue
                           
                           customer = get_customer_info_by_phone(phone)

                           if not customer:
                               print("\n  ❌ Không tìm thấy khách hàng!")
                               continue
                           generate_otp(phone)
                           user_otp = input("  Nhập OTP: ")

                           

                           if not verify_otp(phone, user_otp):
                               print("\n  ❌ OTP không đúng!")
                               continue
                           cid, name, address = customer

                    # Đăng nhập rồi => dùng luôn account
                        else:
                           cid = customer_id
                        print(f"\n  👤 Khách hàng ID: {cid}")
                        view_booking_history(cid)

                        try:
                             bkid = int(input("\n  Nhập BookingID cần hủy: "))
                        except ValueError:
                             print("\n  ⚠️ BookingID phải là số!")
                             continue
                        if confirm_action("Xác nhận hủy vé?"):
                             
                             cancel_booking(bkid, cid)

                    elif sub_choice == "6":
                        # Lịch sử đặt vé
                

                        if role == "guest":
                            phone = input("  Nhập số điện thoại: ")
                            # 🔐 Check phone có account không
                            conn = get_connection()
                            cursor = conn.cursor()

                            cursor.execute("""
                                SELECT UserID
                                FROM Users
                                WHERE Username = %s
                            """, (phone,))

                            existing_account = cursor.fetchone()

                            cursor.close()
                            conn.close()

                            # ❌ Nếu đã có account
                            if existing_account:
                               print("\n  ⚠️ Số điện thoại này thuộc tài khoản đã đăng ký.")
                               print("  👉 Vui lòng đăng nhập để xem lịch sử đặt vé!")
                               continue
                            customer = get_customer_info_by_phone(phone)

                            if not customer:
                               print("\n  ❌ Không tìm thấy khách hàng!")
                               continue


                            generate_otp(phone)
                            user_otp = input("  Nhập OTP: ")
                            if not verify_otp(phone, user_otp):
                                print("\n  ❌ OTP không đúng!")
                                continue

                            cid, name, address = customer

                        # User login rồi
                        else:
                            cid = customer_id
                        
                        view_booking_history(cid)

                    elif sub_choice == "7":
                        view_all_customers()

                    elif sub_choice == "8":
                        revenue_report()

                    elif sub_choice == "9":
                        view_all_events()
                        print("\n  Nhập EventID để xem chi tiết doanh thu.")
                        print("  (Nhấn Enter để thoát về menu chính)\n")
                        while True:
                            eid_input = input("  Nhập EventID: ").strip()
                            if eid_input == "":
                                break
                            try:
                                eid = int(eid_input)
                                event_detail_report(eid)
                            except ValueError:
                                print("  ⚠️ Vui lòng nhập số hợp lệ!")

                    elif sub_choice == "10":
                        ticket_type_stats()

                    elif sub_choice == "11":
                        available_seats_report()

                    elif sub_choice == "0":
                        print("\n  👋 Thoát khỏi menu chức năng!\n")
                        break

                    else:
                        print("\n  ⚠️ Lựa chọn không hợp lệ, vui lòng thử lại!")

                except ValueError:
                    print("\n  ⚠️ Vui lòng nhập số hợp lệ!")

                input("\n  Nhấn Enter để quay lại menu...")  # dừng lại để người dùng xem kết quả


if __name__ == "__main__":
    main()


