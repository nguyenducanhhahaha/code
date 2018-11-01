N = int(input("Nhập số tháng trong năm:  "))
if N == 1 or N == 3 or N == 5 or N == 7 or N == 8 or N == 10 or N == 12:
    print("Tháng đó có 31 ngày")
elif N == 2:
    print("Tháng này có 28 hoặc 29 ngày")
else:
    print("Tháng này 30 ngày")

