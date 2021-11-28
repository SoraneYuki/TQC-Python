f = open("read.txt", "r")
line = f.readline()
f.close()

total = 0

for num in line.split(" "):

    total += int(num)

print(total)

# print(sum(map(int, line.split(" "))))