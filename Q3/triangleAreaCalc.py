import math
while True:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    s = 0.5*(a+b+c)

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("area: ", area)