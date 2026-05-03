import random
import time

otp_storage = {}

def generate_otp(phone):
    otp = str(random.randint(100000, 999999))
    otp_storage[phone] = (otp, time.time())

    print(f"\n  🔐 OTP của bạn là: {otp}")  # ⚠️ demo thôi (thực tế phải gửi SMS)

def verify_otp(phone, user_otp):
    if phone not in otp_storage:
        return False

    otp, created_time = otp_storage[phone]

    # ⏱️ OTP hết hạn sau 60s
    if time.time() - created_time > 60:
        print("\n  ⏰ OTP đã hết hạn!")
        return False

    return otp == user_otp