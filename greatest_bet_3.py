
a=int(input("enter no"))
b=int(input("enter no"))
c=int(input("enter no"))
if a>b and a>c:
    if a>b:
        print(a,"is greatest")
    else:
        print("both are equal")
elif b>a and b>c:
    if b>a:
        print(b,"is greatest")
    else:
        print("both are equal")
else:
    if c>a and c>b:
        print(c,"is greatest")
    else:
        print(a,b,c,"all of them are equal")