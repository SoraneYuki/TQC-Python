import math

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

print("( {:g} , {:g} )".format(x1, y1))
print("( {:g} , {:g} )".format(x2, y2))

print("Distance = {:.4f}".format(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)))