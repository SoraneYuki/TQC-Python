n = int(input())

result = 0

for i in range(1, n):

    result += 1 / (i ** 0.5 + (i + 1) ** 0.5)

print("%.4f" % result)

# sum(map(lambda x: 1 / (x ** 0.5 + (x + 1) ** 0.5), range(1, n)))