import random
import time
import hashlib

def format_currency(amount):
    """Định dạng số tiền VND"""
    return f"{amount:,.0f} VND"

def print_header(title):
    """In tiêu đề đẹp"""
    print("\n" + "="*50)
    print(f"    {title}")
    print("="*50)

def print_divider():
    print("-"*50)

def confirm_action(message):
    """Hỏi xác nhận trước khi thực hiện"""
    choice = input(f"\n  {message} (y/n): ").strip().lower()
    return choice == 'y'


OTP_STORE = {}  # lưu tạm trong RAM

def generate_otp(phone):
    otp = str(random.randint(100000, 999999))
    expire = time.time() + 60  # hết hạn sau 60s

    OTP_STORE[phone] = (otp, expire)

    print(f"\n  🔐 OTP của bạn là: {otp} (demo)")  # giả lập SMS
    return otp


def verify_otp(phone, user_input):
    if phone not in OTP_STORE:
        return False

    otp, expire = OTP_STORE[phone]

    if time.time() > expire:
        print("\n  ⏰ OTP đã hết hạn!")
        return False

    return otp == user_input

def hash_password(password: str) -> str:
    """Mã hóa mật khẩu bằng SHA256"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()