map =[[0 for x in range(0, 1000)] for y in range(0,1000)]
# for x in range(0, 1000):
# 	print(map[x])
unsplit = []
first = []
second = []
printed = False

with open("input.txt") as file:
	for line in file:
		unsplit = line.split()
		first = unsplit[0].split(',')
		second = unsplit[2].split(',')
		if first[0] == second [0]:
			i = 0
		#	print("x's are same", first[0], second[0])
		#	print("y's: first: ", first[1], " second : ", second[1])
			if int(first[1]) > int(second [1]):
		#		print("first - i = ", int(first[1]) - i)
				while ((int(first[1]) - i) >= int(second[1])):
					map[int(first[1]) - i][int(first[0])] += 1
		#			print("first - i = ", int(first[1]) - i)
					i += 1
			else:
		#		print("first + i = ", int(first[1]) + i)
				while ((int(first[1]) + i) <= int(second[1])):
					map[int(first[1]) + i][int(first[0])] += 1
					i += 1
		elif first[1] == second [1]:
			i = 0
			if int(first[0]) > int(second[0]):
				while ((int(first[0]) - i) >= int(second[0])):
					map[int(first[1])][int(first[0]) - i] += 1
					i += 1
			else:
				while ((int(first[0]) + i) <= int(second[0])):
					map[int(first[1])][int(first[0]) + i] += 1
					i += 1
		# diagonal
		else:
			#south east: x1 < x2 and y1 < y2
			if int(first[0]) < int(second[0]) and int(first[1]) < int(second[1]):
				x_range = range(int(first[0]), int(second[0]) + 1)
				y_range = range(int(first[1]), int(second[1]) + 1)
			#north east
			elif int(first[0]) < int(second[0]) and int(first[1]) > int(second[1]):
				x_range = range(int(first[0]), int(second[0]) + 1)
				y_range = range(int(first[1]), int(second[1]) - 1, -1)
			#north west
			elif int(first[0]) > int(second[0]) and int(first[1]) > int(second[1]):
				x_range = range(int(second[0]), int(first[0]) + 1)
				y_range = range( int(second[1]), int(first[1]) + 1)
			#south west
			else:
				x_range = range(int(first[0]), int(second[0]) - 1, -1)
				y_range = range(int(first[1]), int(second[1]) + 1)
			for index, x in enumerate(x_range):
				map[y_range[index]][x] += 1
total = 0
for row in map:
	print (row)
	for nr in row:
		if nr > 1:
			total += 1
print (total)

#2296 = too low

# for part 1: 5585
# for part 2: 17193