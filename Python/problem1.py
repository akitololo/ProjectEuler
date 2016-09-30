def sum_multiples_of_3_and_5_below(number):
	final_sum = 0
	for integer in range(number):
		if (integer % 3 == 0) or (integer % 5 == 0):
			final_sum += integer
	print(final_sum)

sum_multiples_of_3_and_5_below(1000)
