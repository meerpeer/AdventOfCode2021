import statistics

with open("input.txt") as file:
	input_line = file.readlines()
	values = [int (i) for i in input_line[0].split(',')]

values.sort()
fuel = 0
crabs_in_place = 0
min_fuel = 300000000

for i in range(min(values), len(values)):
	fuel = 0
	for crab in values:
		x = abs(crab - i)
		fuel += (x * (x + 1)) // 2
	if fuel < min_fuel:
		min_fuel = fuel
	#print (fuel)

print(min_fuel)