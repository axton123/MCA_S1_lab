import graphics
from graphics import circle,rectangle
from graphics.init import cuboid,sphere
#from graphics.circle import *

print("\nArea of circle : ",circle.a_c(5))
print("\nPermeter of circle : ",circle.p_c(5))

print("\nArea of rectangle : ",rectangle.a_r(4,5))
print("\nPermeter of rectangle : ",rectangle.p_r(4,5))

print("\nArea of cuboid : ",cuboid.a_c(4,6,2))
print("\nPermeter of cuboid : ",cuboid.p_c(4,6,2))

print("\nArea of sphere : ",sphere.a_s(5))
print("\nPermeter of sphere : ",sphere.p_s(5))
