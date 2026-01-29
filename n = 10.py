n = int(input())
while n > 0:
    if int(n**0.5) * int(n**0.5) == n:
        print(n, "la so chinh phuong")
    else:
        print(n,"khong phai la so chinh phuong")
    n= int(input())
 