
outputs = []
with open("input.txt") as file:
	lines = file.readlines()
	for line in lines:
		line = line.split('\n')[0]
		outputs.append(line.split('|')[1].split(" ")[1:10])

certains = 0

for output in outputs:
	for i in output:
		if len(i) in {2, 3, 7, 4}:
			certains += 1


print(certains)