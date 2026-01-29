m, n =map (int, input().split())
if n == 0:
    print("Lỗi: n phải khác 0.")
else:
    ket_qua = m // n
    print("Kết quả làm tròn xuống" , ket_qua)