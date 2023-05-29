import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

top = math.pow(a,2) - math.pow(b,2)- math.pow(c,2)

bottom = -2*b*c

whole = top/bottom

toRad = math.acos(whole)

toDeg = toRad *180/ math.pi
print("deg: ",toDeg)