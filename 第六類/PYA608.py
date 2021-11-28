# list1 = [[6, 4, 8], [39, 12, 3], [-3, 49, 33]]

list1 = []

for i in range(3):

    list1.append([])

    for j in range(3):

        list1[i].append(int(input()))

max_n = list1[0][0]
max_idx = (0, 0)

min_n = list1[0][0]
min_idx = (0, 0)

for i in range(3):

    for j in range(3):

        if list1[i][j] >= max_n:

            max_n = list1[i][j]
            max_idx = (i, j)

        elif list1[i][j] <= min_n:
            
            min_n = list1[i][j]
            min_idx = (i, j)

print("Index of the largest number {} is: {}".format(max_n, max_idx))
print("Index of the smallest number {} is: {}".format(min_n, min_idx))