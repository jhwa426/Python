##Lecture 9

my_map = dict()
my_list = list()10

for i in range(0, 10):
	my_list.append(str(i))

for i in range(0, 10):
	my_map[str(i)] = i

print(my_list)
print(my_map)

print('5' in my_list)
print('5' in my_map)

print('xyz' in my_list)
print('xyz' in my_map)

