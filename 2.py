my_list = [100, 50, 400, 500]


my_list[1] = 200
print("After change:", my_list)


my_list.append(600)
print("After append:", my_list)


my_list.insert(2, 300)
print("After insert:", my_list)


my_list.remove(600)
print("After removing 600:", my_list)


my_list.pop(0)
print("After removing index 0:", my_list)