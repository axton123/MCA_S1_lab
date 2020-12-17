a=int(input("\nEnter the year\t"))
if(a%4==0 & a%400==0):
    if(a%100==0):
        print("\nLeap year")
    elif(a%100!=0):
        print("\nLeap Year")
    else:
        print("\nNot LY")
else:
    print("\nNot Leap Year")
