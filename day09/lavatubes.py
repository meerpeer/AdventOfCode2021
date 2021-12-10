group_sizes = []
total_sum = 0
matrix = []

def count_groupsize(y, x):
	# Should stop when: (so for recursive we would return here?)
		# 9 is encountered or -1 (which is the spot we mark)
		# if left or top are reached:	y or x are < 0
		# if right is reached:			x > len(matrix[0])
		# if bottem is reached:			y > len(matrix)
	if y < 0 or x < 0 or x >= len(matrix[0]) or y >= len(matrix):
		return
	if matrix[y][x] == 9 or matrix[y][x] == -1:
		return
	# If none of the above, this is a spot in the group, 
		# so mark it with something (-1?)
		# add 1 to this group size count add the last appended groupsize index
	matrix[y][x] = -1
	group_sizes[len(group_sizes) - 1] += 1
	# Check per direction with this same function, it should come back at some point with the return above
	# and then check for the other directions, I don't think it matters which you check first as it always goes back
	count_groupsize(y - 1, x)
	count_groupsize(y, x - 1)
	count_groupsize(y + 1, x)
	count_groupsize(y, x + 1)

def check_all_adjecent(matrix, y, x):
	if y > 0:
		if matrix[y][x] >= matrix[y - 1][x]:
			return 0
	if y < (len(matrix) - 1):
		if matrix[y][x] >= matrix[y + 1][x]:
			return 0
	if x > 0:
		if matrix[y][x] >= matrix[y][x - 1]:
			return 0
	if x < (len(matrix[y]) - 1):
		if matrix[y][x] >= matrix[y][x + 1]:
			return 0
	return 1

with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		line = line.split('\n')[0]
		matrix.append(list(map(int, line)))

for y in range(len(matrix)):
	for x in range(len(matrix[0])):
		if check_all_adjecent(matrix, y, x):
			total_sum += int(matrix[y][x]) + 1
			group_sizes.append(0)
			count_groupsize(y, x)


group_sizes = sorted(group_sizes, reverse=True)
part_two_answer = group_sizes[0] * group_sizes[1] * group_sizes[2]

print("part one: ", total_sum)
print("part 2 :", part_two_answer)
