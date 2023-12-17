# import os
# os.system("pip install pyotp")
import pyotp
import time

# Generate a new secret key
secret = pyotp.random_base32()

# Create a TOTP object
totp = pyotp.TOTP(secret)

# Generate the OTP code
otp_code = totp.now()

print(f"Secret Key: {secret}")
print(f"Current OTP Code: {otp_code}")

# Validate the OTP code
time.sleep(30)  # Wait for a short duration to simulate time passing
is_valid = totp.verify(otp_code)

if is_valid:
    print("OTP code is valid!")
else:
    print("OTP code is not valid.")
