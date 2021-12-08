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
		x1 = unsplit[0].split(',')[0]
		x2 = unsplit[2].split(',')[0]
		y1 = unsplit[0].split(',')[1]
		y2 = unsplit[2].split(',')[1]
		if x1 == x2:
			i = 0
		#	print("x's are same", x1, x2)
		#	print("y's: first: ", y1, " second : ", y2)
			if int(y1) > int(y2):
		#		print("first - i = ", int(y1) - i)
				while ((int(y1) - i) >= int(y2)):
					map[int(y1) - i][int(x1)] += 1
		#			print("first - i = ", int(y1) - i)
					i += 1
			else:
		#		print("first + i = ", int(y1) + i)
				while ((int(y1) + i) <= int(y2)):
					map[int(y1) + i][int(x1)] += 1
					i += 1
		elif y1 == y2:
			i = 0
			if int(x1) > int(x2):
				while ((int(x1) - i) >= int(x2)):
					map[int(y1)][int(x1) - i] += 1
					i += 1
			else:
				while ((int(x1) + i) <= int(x2)):
					map[int(y1)][int(x1) + i] += 1
					i += 1
		# diagonal
		else:
			#south east: x1 < x2 and y1 < y2
			if int(x1) < int(x2) and int(y1) < int(y2):
				x_range = range(int(x1), int(x2) + 1)
				y_range = range(int(y1), int(y2) + 1)
			#north east
			elif int(x1) < int(x2) and int(y1) > int(y2):
				x_range = range(int(x1), int(x2) + 1)
				y_range = range(int(y1), int(y2) - 1, -1)
			#north west
			elif int(x1) > int(x2) and int(y1) > int(y2):
				x_range = range(int(x2), int(x1) + 1)
				y_range = range( int(y2), int(y1) + 1)
			#south west
			else:
				x_range = range(int(x1), int(x2) - 1, -1)
				y_range = range(int(y1), int(y2) + 1)
			for index, x in enumerate(x_range):
				map[y_range[index]][x] += 1
total = 0
for row in map:
	#print (row)
	for nr in row:
		if nr > 1:
			total += 1
print (total)

#2296 = too low

# for part 1: 5585
# for part 2: 17193