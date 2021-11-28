# def fn(n):

#     sum(map(lambda x: int(x), list(n)))

# n = input()

# print("Sum of all digits of {} is {}".format(n, fn(n)))

n = int(input())

for i in range(n):

    num = input()
    total = 0

    for d in list(num):

        total += int(d)
    
    print("Sum of all digits of {} is {}".format(num, total))