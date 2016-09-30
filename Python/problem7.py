count = 2
number = 5
setting = True

while setting:
	for i in range(2, number):
		if (number % i) == 0:
#			print("Number on: ", number)
#			print("Count on: ", count)
			break
	else:
		count += 1
#		print("Number on: ", number)
#		print("Count on: ", count)

#	print("Number on: ", number)
#	print("Count on: ", count)
	number += 1

	if count == 100:
		print("100th prime reached.")

	if count == 1000:
		print("...1000th one now...")

	if count == 5000:
		print("...5000th...")

	if count == 9000:
		print("...NEARLY THERE...")

	if count == 10001:
		setting = False
		print("{number} is the number {count} prime!".format(number=str(number-1), count=str(count)))
