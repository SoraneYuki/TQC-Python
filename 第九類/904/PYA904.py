data = []

with open("read.txt","r") as file:
   
   for line in file:

      print(line)
      name, height, weight = line.strip().split(" ")
      data.append([name, int(height), int(weight)])    

print("Average height: {:.2f}".format(sum([x[1] for x in data]) / len(data)))
print("Average weight: {:.2f}".format(sum([x[2] for x in data]) / len(data)))

tallest = max(data, key = lambda x: x[1])
heaviest = max(data, key = lambda x: x[2])

print("The tallest is {} with {:.2f}cm".format(tallest[0], tallest[1]))
print("The heaviest is {} with {:.2f}kg".format(heaviest[0], heaviest[2]))