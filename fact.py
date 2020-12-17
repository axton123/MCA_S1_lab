x=int(input("enter the num"))
if(x>0):
    fact=1
    i=1
    while(i<=x):
        fact=fact*i
        i+=1

    print(fact)
else:
    print("\ninvalid")

print("\n")
