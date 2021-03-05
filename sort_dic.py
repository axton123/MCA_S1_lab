dict={}
n1=int(input("Total number of elements in dict: "))
for i in range(n1):
    dict[i]=input("Enter element : ")
asc=sorted(dict.values())
print("Ascending : ",asc)
asc.reverse()
print("Descending : ",asc)