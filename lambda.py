a_s = lambda s: s*s
a_r = lambda l,b: l*b
a_t = lambda h,ba: (h*ba)

s=int(input("\nArea of Square\nEnter length of side : "))
l=int(input("\nArea of Reactangle\nlength :"))
b=int(input("\nbreadth : "))
h=int(input("\nArea of Triangle\nheight :"))
ba=int(input("\nbase :"))

print("\nArea of square : ",a_s(s))
print("\nArea of square : ",a_r(l,b))
print("\nArea of square : ",a_r(h,ba)/2)
