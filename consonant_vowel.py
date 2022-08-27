
# checking vowel or consonant
ch = input("Enter a character: ")
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
if(ch=='1' or ch=='2' or ch=='3' or ch =='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9'or ch=="0" ):
    print(ch,"is digit ")
else:
    print(ch, "is a Consonant")