try:
    m, n = map(int, input().split())
except ValueError:
    print("Lỗi: Đầu vào phải là số nguyên.")
    exit()
if n == 0:
    print("Phép tính không xảy ra. (Lỗi chia cho 0)")
else:
    ket_qua = m // n
    print("Làm tròn xuống:", ket_qua)