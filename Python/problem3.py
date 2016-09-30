def _get_prime_numbers(num):
	prime_num_list = []
	lower = 0
	upper = num + 1

	for number in range(lower, upper):
		if number > 1:
			for i in range(2, number):
				if (number % i) == 0:
					break
			else:
				prime_num_list.append(number)

	return prime_num_list

def _get_largest_prime_factor(wanted_value):
	print("Working")
	prime_numbers = _get_prime_numbers(wanted_value)
	prime_factors = []

	for number in prime_numbers:
		if (wanted_value % number) == 0:
			prime_factors.append(number)
			print(".", end="", flush=True)
	print("\n\n[*]", prime_factors[-1])

_get_largest_prime_factor(600851475143)