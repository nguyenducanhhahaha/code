T = input("Nhập tài khoản:  ")
if T == ("hoimatbo"):
    M = input("Nhập mật khẩu:  ")
    if M == ("hoi123"):
        N = input("Nhập lại mật khẩu:  ")
        if N == M:
            E = input("Nhập E-mail:  ")
            if E == ("hoimatbo@email.com"):
                print ("login succesful")
            else:
                ("xem lại E-mail")
        else:
            print("Xem lại mật khẩu")
    else:
        print("xem lại mật khẩu")
else:
    print("xem lại tài khoản")