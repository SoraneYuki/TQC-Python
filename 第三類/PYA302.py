a = int(input())
b = int(input())

total = 0

for i in range(a, b + 1):

    if i % 2 == 0:

        total += i

print("%d" % total)

# print(sum(filter(lambda x: x % 2 == 0, range(a, b + 1))))