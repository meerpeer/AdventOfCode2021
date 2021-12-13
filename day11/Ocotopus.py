grid = []
flashes = 0

with open("input") as file:
	lines = file.readlines()
	for line in lines:
		grid.append(list(map(int, line.split('\n')[0])))

def check_flashes(y, x):
	global flashes
	if y >= len(grid) or x >= len(grid[0]) or x < 0 or y < 0:
		return
	if grid[y][x] == 9:
		grid[y][x] = -1
		flashes += 1
		check_flashes(y - 1, x)
		check_flashes(y + 1, x)
		check_flashes(y, x - 1)
		check_flashes(y, x + 1)
		check_flashes(y - 1, x - 1)
		check_flashes(y + 1, x + 1)
		check_flashes(y + 1, x - 1)
		check_flashes(y - 1, x + 1)
	if grid[y][x] >= 0:
		grid[y][x] += 1

for i in range(100):
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			check_flashes(y, x)
	
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == -1:
				grid[y][x] = 0

print ("part 1 : ", flashes)