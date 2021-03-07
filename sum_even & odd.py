a=int(input("\nEnter a num"))
e=o=0 

for i in range(1,a+1):
    #print(i)
    if(i%2==0):
        e=e+i
    elif(i%2!=0):
        o=o+i

print(e,o)
