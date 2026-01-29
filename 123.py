import math

a = float(input("Nhập chiều rộng a: "))
b = float(input("Nhập chiều dài b: "))

dien_tich_hcn = a * b
ban_kinh = min(a, b) / 2
dien_tich_tron = 3.14 * (ban_kinh ** 2)

con_lai = dien_tich_hcn - dien_tich_tron
print(f"Diện tích còn lại: {con_lai:.2f}")