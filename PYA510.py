def compute(n):

    if n < 2:

        return n

    else:

        return compute(n - 1) + compute(n - 2)

num = int(input())

for i in range(num):

    print(compute(i), end = " ")



# def fib(n):

#     if n <= 1:

#         return n

#     else:

#         return fib(n - 1) + fib(n - 2)

# def compute(n):

#     result = []

#     for i in range(n):

#         result.append(str(fib(i)))

#     return result

# num = int(input())

# print(" ".join(compute(num)))



# def compute(n):

#     result = [0, 1]

#     any(map(lambda _: result.append(sum(result[-2:])), range(2, n)))

#     return result[:n]

# num = int(input())

# for i in compute(num):

#     print("{} ".format(i), end = "")

# print()