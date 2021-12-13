lines = open("input.txt").read().splitlines()

openings = ['(', '[', '{', '<']
closings = [')', ']', '}', '>']
p1_values = [3, 57, 1197, 25137]
p2_values = [1, 2, 3, 4]

uncorrupted = []

corrupted_total = 0
fixed_scores = []
for i in range(len(lines)):
	fixed_score = 0
	current_openings = []
	corrupt = False
	for c in range(len(lines[i])):
		if lines[i][c] in openings:
			current_openings.append(openings.index(lines[i][c]))
		else:
			if closings.index(lines[i][c]) != current_openings[len(current_openings) - 1]:
				corrupt = True
				corrupted_total += p1_values[closings.index(lines[i][c])]
				break
			current_openings.pop()	
	if not corrupt:
		for k in range(len(current_openings)):
			fixed_score *= 5 
			fixed_score += p2_values[current_openings[len(current_openings) - k - 1]]
		fixed_scores.append(fixed_score)


print("part 1: ", corrupted_total)
print("part 2: ", sorted(fixed_scores)[int(len(fixed_scores)/2)])