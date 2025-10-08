my_list=[1,2,3,4]
print(my_list)

my_list.append(5)
print(my_list)

my_list.extend([6,7,8])
print(my_list)

my_list.insert(2,9)
print(my_list)

my_list.remove(9)
print(my_list)

popping=my_list.pop(7)
print(my_list,"removed elementis:",popping)

counting=my_list.count(4)
print (my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)

length=len(my_list)
print(length)

maximum=min(my_list)
print(maximum)

checking=4 in my_list
print(checking)

umi=my_list.copy()

my_list.clear()
print(my_list)

print(umi)

