f_name = input()
str_old = input()
str_new = input()

with open(f_name, "r") as file:
    data = file.read()

print("=== Before the replacement")
print(data)

data = data.replace(str_old, str_new)

print("=== After the replacement")
print(data)