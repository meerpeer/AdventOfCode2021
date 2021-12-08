hor = 0
aim = 0
depth = 0

with open("puzzle_input.txt") as file:
	for line in file:
		if line[0] == 'f':
			hor += int(line[8])
			depth += aim * int(line[8])
		if line[0] == 'd':
			aim += int(line[5])
		if line[0] == 'u':
			aim -= int(line[3])
print(hor * depth)
