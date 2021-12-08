#first check the most common value in in that position
#remove all the values that don't have that bit in that position
# if equally valued keep with a 1 in that position

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



