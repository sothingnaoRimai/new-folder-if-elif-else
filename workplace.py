
a=input(" male or female ")
b= int(input(" enter age"))
if a=="male" and b>=15 and b<=50:
    print("can work everywhere")
elif a=="female" and b>=15:
    print("work only in urban areas")
elif a=="male" and b>=50:
    print(" can work only in urban areas")
else:
    print("too young to work")
