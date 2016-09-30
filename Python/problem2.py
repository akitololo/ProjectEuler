fibonacci_nums = [1,2]

def fibonacci_to(num_of_additions):
	for i in range(num_of_additions):
		next_num = fibonacci_nums[i]+fibonacci_nums[i+1]
		fibonacci_nums.append(next_num)

def fibonacci_filter():
	even_fibonacci_sum = 0
	filtered_fibonacci_nums = [num for num in fibonacci_nums if num <= 4000000]
	print(filtered_fibonacci_nums)
	for filtered_num in filtered_fibonacci_nums:
		if filtered_num % 2 == 0:
			even_fibonacci_sum += filtered_num
	print(even_fibonacci_sum)

fibonacci_to(100)
fibonacci_filter()