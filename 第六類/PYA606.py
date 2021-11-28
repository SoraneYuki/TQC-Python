def compute(lst):
    for sublst in lst:
        for x in sublst:
            print("{:4d}".format(x), end = "")
        print()

rows = int(input())
cols = int(input())

list1 = list()

for row in range(rows):
    list1.append(list())
    for col in range(cols):
        list1[row].append(col - row)

compute(list1)