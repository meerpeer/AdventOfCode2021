from collections import defaultdict

connections = []
with open("test") as file:
	lines = file.readlines()
	for line in lines:
		connections.append(list(map(str, line.split('-'))))
	for values in connections:
		values[1] = values[1].split('\n')[0]




print(connections)

#for day 12
#tuple, dictonary
#dictoanry has a key, you can couple this to all the values