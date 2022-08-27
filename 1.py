ch=input("enter the cheractor:")
if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    print(ch,"is alphabet")
elif ch=='@' or ch=='#' or ch=='&' or ch=='_':
    print(ch,"is special character")
else:
    print(ch,"is digit")

