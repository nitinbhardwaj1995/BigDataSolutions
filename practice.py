ee="nitinbhardwaj04@gmail.com"
def check_email(email):
    l=['nitinbhardwaj00','nitinbhardwaj01','nitinbhardwaj02']
    email=email.split("@")[0]
    if email in l:
        print("already exist")
    else:
        if email not in l and email.isalnum():
            l.append(email)
            print(l,"yes")
        else:
            print("No")


print(check_email(ee))
