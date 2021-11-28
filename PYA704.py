set1 = set()

while True:

    n = int(input())
    
    if n == -9999:

        break

    set1.add(n)

print("Length: {}".format(len(set1)))
print("Max: {}".format(max(set1)))
print("Min: {}".format(min(set1)))
print("Sum: {}".format(sum(set1)))