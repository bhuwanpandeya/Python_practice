a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
num = int(input("Enter a number"))
for i in a:
    if i < num:
        new_list.append(i)
print(new_list)