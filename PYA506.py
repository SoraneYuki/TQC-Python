def compute(a, b, c):

    d = b ** 2 - 4 * a * c

    if d < 0:

        return None

    elif d == 0:

        return -b / (2 * a)

    else:

        ans1 = (-b + d ** 0.5) / (2 * a)
        ans2 = (-b - d ** 0.5) / (2 * a)

a = int(input())
b = int(input())
c = int(input())

ans = compute(a, b, c)

if ans == None:
    print("Your equation has no root.")
else:
    print("{}, {}".format())

"""
Your equation has no root.
"""