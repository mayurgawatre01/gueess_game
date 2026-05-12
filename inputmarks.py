m=int(input("enter the marks : "))
if m>100:
    print("not valid plz enter your marks below 100")
elif m>90:
    print("A")
elif m>=75 and m<=89:
    print("B")
elif m>=50   and m<=74 :
    print("c")
else:
    print("F")