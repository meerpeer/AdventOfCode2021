import statistics

with open("input_test.txt") as file:
	input_line = file.readlines()
	values = [int (i) for i in input_line[0].split(',')]

values.sort()
place = statistics.median(values)
fuel = 0
crabs_in_place = 0

print("median: ", place)
for crab in values:
	if crab == place:
		crabs_in_place +=1

print("crabs already in place: ", crabs_in_place)

while crabs_in_place < len(values):
	for i in range(len(values)):
		if values[i] != place:
			if values[i] > place:
				values[i] -= 1
			else:
				values[i] += 1
			if values[i] == place:
				crabs_in_place += 1
				print(values[i])
			fuel += abs(place - values[i])
			#print(crabs_in_place)
print (values)
print(fuel)