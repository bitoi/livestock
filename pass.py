import bcrypt

# Mật khẩu bạn muốn đặt (ví dụ: 123456)
password_raw = "123456"

# Tạo mã hash (độ khó 12 cho giống DB cũ)
hashed = bcrypt.hashpw(password_raw.encode('utf-8'), bcrypt.gensalt(rounds=12))
hashed_str = hashed.decode('utf-8')

print("-" * 50)
print("CHẠY CÂU LỆNH SQL NÀY TRONG WORKBENCH/DATABASE:")
print(f"UPDATE account SET password = '{hashed_str}' WHERE username = 'admin';")
print("-" * 50)