#array with 12 ints for gamma
#check every character in a line and add to corresponding int in gamma
#	- +1 for 1
#	- -1 for 0
#convert if negative to 0 if positive to 1
#join these bros and print it out

totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0

with open("input.txt") as file:
	for line in file:
		for i in range(0, 12):
			if line[i] == "1":
				totals[i] += 1
			else:
				totals[i] -= 1
for x in range(0, 12):
	if totals[x] >= 0:
		totals[x] = 0
	else:
		totals[x] = 1
print ("".join(map(str, totals)))
