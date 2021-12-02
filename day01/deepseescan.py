last_sum = 0
i = 0

with open("scans.txt") as file:
	for line in file:
		if line > last:
			i += 1
		last = line
print(i)