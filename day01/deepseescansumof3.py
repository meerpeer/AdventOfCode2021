this_sum = 0
next_sum = 0
answer = 0
i = 0

with open("scans.txt") as file:
	numbers = file.readlines()
	nr_nbrs = len(numbers)
	while i < nr_nbrs - 3:
		this_sum = int(numbers[i]) + int(numbers[i + 1]) + int(numbers[i + 2])
		next_sum = int(numbers[i + 1]) + int(numbers[i + 2]) + int(numbers[i + 3])
		if next_sum > this_sum:
			answer += 1
		i += 1
print(answer)