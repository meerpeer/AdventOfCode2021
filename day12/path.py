from collections import defaultdict

connections = defaultdict(list)

data = []

with open("test") as file:
	lines = file.readlines()
	for line in lines:
		data.append(list(map(str, line.split('-'))))
	for connection in data:
		connections[connection[0]].append(connection[1].split('\n')[0])
		connections[connection[1].split('\n')[0]].append(connection[0])

for connection in connections:
	print(connection, connections.get(connection))




#for day 12
#tuple, dictonary
#dictoanry has a key, you can couple this to all the values