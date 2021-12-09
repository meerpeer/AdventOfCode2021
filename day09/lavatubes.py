def check_all_adjecent(lines, i, c):
	if i > 0:
		if lines[i][c] >= lines[i - 1][c]:
			return 0
	if i < (len(lines) - 1):
		if lines[i][c] >= lines[i + 1][c]:
			return 0
	if c > 0:
		if lines[i][c] >= lines[i][c - 1]:
			return 0
	if c < (len(lines[i]) - 2):
		if lines[i][c] >= lines[i][c + 1]:
			return 0
	return 1

total_sum = 0

with open("input_test.txt") as file:
	lines = file.readlines()
	for i in range(len(lines)):
		for c in range(len(lines[i]) - 1):
			if check_all_adjecent(lines, i, c):
				total_sum += int(lines[i][c]) + 1
				#lines[i][c] = 'x'
		print(lines[i])
print
print("part one: ", total_sum)