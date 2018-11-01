T = input("Nhập tài khoản:  ")
if T == ("hoimatbo"):
    M = input("Nhập mật khẩu:  ")
    if M == ("hoi123"):
        N = input("Nhập lại mật khẩu:  ")
        if N == M:
            E = input("Nhập E-mail:  ")
            if E == ("Hoimatbo132@email.com") and E.alpha and E.digit and len(N) >8 :
                print ("login succesful")
            else:
                ("xem lại E-mail")
        else:
            print("Xem lại mật khẩu")
    else:
        print("xem lại mật khẩu")
else:
    print("xem lại tài khoản")