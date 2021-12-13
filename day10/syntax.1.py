lines = open("input_test.txt").read().splitlines()

openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']
p1_values = [3, 57, 1197, 25137]
p2_values = [1, 2, 3, 4]

uncorrupted = []

corrupted_total = 0
fixed_score = 0
for i in range(len(lines)):
	current_openings = []
	corrupt = False
	print(current_openings)
	print(i)
	for c in range(len(lines[i])):
		if lines[i][c] in openings:
			current_openings.append(openings.index(lines[i][c]))
		else:
			if closings.index(lines[i][c]) != current_openings[len(current_openings) - 1]:
				corrupt = True
				corrupted_total += p1_values[closings.index(lines[i][c])]
				break
			current_openings.pop()
	print(current_openings)
	print("-------")		
	if not corrupt:
		len = len(current_openings)
		for k in range(len):
			fixed_score *= 5 
			fixed_score += p2_values[current_openings[len - k - 1]]

print(fixed_score)