count = 2
number = 5
setting = True

while setting:
	for i in range(2, number):
		if (number % i) == 0:
			break
	else:
		count += 1

	number += 1

	if count == 10001:
		setting = False
		print("{number} is the number {count} prime!".format(number=str(number-1), count=str(count)))
