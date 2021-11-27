num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# 靠右對齊
print("|{:>7.2f} {:>7.2f}|".format(num1, num2))
print("|{:>7.2f} {:>7.2f}|".format(num3, num4))

# 靠左對齊
print("|{:<7.2f} {:<7.2f}|".format(num1, num2))
print("|{:<7.2f} {:<7.2f}|".format(num3, num4))