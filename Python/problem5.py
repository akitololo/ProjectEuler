setting = True
on = 1
print("Working")
million = 10**6

while setting:
	pass_array = []

	for i in range(20):
		value = on % (i+1)
		pass_array.append(value)

	if sum(list(pass_array)) == 0:
		setting = False

	on += 1

print("\n\nIt worked! Number: ", on-1)