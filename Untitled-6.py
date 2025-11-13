try:
    dau_diem = input("nhap 6 dau diem theo dung thu tu a1,b1,c1,a2,b2,a3: ")
    a1, b1, c1, a2, b2, a3 = map(float, dau_diem.split())
    
    # Công thức: TB = ((a1+b1+c1) + (a2+b2)*2 + a3*3) / 10
    tong_diem = (a1 + b1 + c1) + (a2 + b2) * 2 + a3 * 3
    diem_tb = tong_diem / 10
    
    # In kết quả lấy 1 chữ số phần thập phân
    print(f"{diem_tb:.1f}")
except ValueError:
    print("loi: vui long nhap 6 so thuc, cach nhau bang khoang trang")
except:
    print("loi: khong du 6 gia tri")
    




