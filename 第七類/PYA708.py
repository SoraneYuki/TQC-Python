dict1 = {}
dict2 = {}
dict3 = {}

num = 1

while True:

    print("Create dict{}:".format(num))

    while True:

        key = input("Key: ")

        if key == "end":

            num += 1
            break

        else:

            value = input("Value: ")

            if num == 1:

                dict1[key] = value

            else:

                dict2[key] = value

    if num > 2:

        break

dict3.update(dict1)
dict3.update(dict2)

for k, v in sorted(dict3.items()):

    print("{}: {}".format(k, v))