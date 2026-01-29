def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
try:
    so_luong_test = int(input())
    for _ in range(so_luong_test):
        a, b = map(int, input().split())
        tong = 0
        for so in range(a, b + 1):
            if kiem_tra_so_nguyen_to(so):
                tong += so
        print(tong)
except:
    pass
