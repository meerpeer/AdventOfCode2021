hor = 0
depth = 0

with open("puzzle_input.txt") as file:
	for line in file:
		if line[0] == 'f':
			hor += int(line[8])
		if line[0] == 'd':
			depth += int(line[5])
		if line[0] == 'u':
			depth -= int(line[3])

print(hor * depth)
