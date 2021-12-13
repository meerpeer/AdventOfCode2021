grid = [[0 for x in range(1310 + 1)] for y in range (894 + 1)]
#grid = [[0 for x in range(11)] for y in range (15)]
folds = [[]] #start at 1 with the folding
highest_y = 0
highest_x = 0

with open("input") as file:
	for line in file:
		if line[0].isdigit():
			x = int(line.split(',')[0])
			y = int(line.split(',')[1].split('\n')[0])
			grid[y][x] = 1
			highest_y = max(y, highest_y)
			highest_x = max(x, highest_x)
		elif line.__contains__("fold along "):
			folds.append(line.split('fold along ')[1].split('='))
			folds[len(folds) - 1][1] = folds[len(folds) - 1][1].split('\n')[0]

foldstep = 0

for i in range(1, len(folds)):
	n = 0
	foldstep += 1
	if(folds[foldstep][0] == 'x'):
		fold_amount = int(folds[foldstep][1])
		for x in range(fold_amount, len(grid[0])):
			for y in range(len(grid)):
				if grid[y][x] == 1:
					grid[y][x - (n * 2)] = 1
			n += 1
		for y in range(len(grid)):
			while len(grid[y]) != fold_amount:
				grid[y].pop(len(grid[y]) - 1)
	if(folds[foldstep][0] == 'y'):
		fold_amount = int(folds[foldstep][1])
		for y in range(fold_amount, len(grid)):
			for x in range(len(grid[0])):
				if grid[y][x] == 1:
					grid[y - (n * 2)][x] = 1
			n += 1
		while len(grid) != fold_amount:
			grid.pop(len(grid) - 1)

string = ""
count_dot = 0
for y in range(len(grid)):
	for x in grid[y]:
		if x == 1:
			count_dot += 1
			string += str('█')
		else:
			string += str(" ")	
	string += "\n"
print(string)
print(count_dot)

#98 not right

