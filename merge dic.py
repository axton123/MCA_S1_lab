d1={}
d2={}
d3={}

a=int(input("\nEnter the limit dictionary1: "))

for i in range(a):
    d1[i]=input("\nEnter the elements : ")

b=int(input("\nEnter the limit dictionary2: "))

for i in range(3,3+b):
    d2[i]=input("\nEnter the elements : ")

print(d1,"\n\n",d2)

for i in d1:
    if i not in d2:
        n={i:d1[i]}
        d3.update(n)
    else:
        n={i:d1[i]+d2[i]}
        d3.update(n)

for i in d2:
    if i not in d1:
        n={i:d2[i]}
        d3.update(n)

print("\n",d3)

'''dict1 = {}
dict2 = {}
dict3 = {}

n1 = int(input("Total number of elements in dict 1 : "))
for i in range(n1):
    dict1[i] = int(input("Enter element : "))

n2 = int(input("Total number of elements in dict 2 : "))
for i in range(3, 3 + n2):
    dict2[i] = int(input("Enter element : "))

print(dict1)
print(dict2)

for i in dict1:
    if i not in dict2:
        new = {i: dict1[i]}
        dict3.update(new)
    else:
        new = {i: dict1[i] + dict2[i]}
        dict3.update(new)

for i in dict2:
    if i not in dict1:
        new = {i: dict2[i]}
        dict3.update(new)

print(dict3)'''