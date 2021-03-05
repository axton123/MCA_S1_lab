a=int(input("\nEnter a num : "))
def pat(a):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(i*j,end=" ")
        print("")

pat(a)