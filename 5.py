import math
m, n = map(int, input().split())
if n == 0:
    print("Lỗi: Phép chia cho 0 không hợp lệ.")
else:
    ket_qua_thuc=m/n
    ket_qua_lam_tron_len= math.celi(ket_qua_thuc)
    print("ket qua lam tron len", ket_qua)