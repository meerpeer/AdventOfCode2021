
inputs = []
outputs = []
with open("input_test.txt") as file:
	lines = file.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].split('\n')[0]
		inputs.append(lines[i].split('|')[0].split(" ")[0:10])
		outputs.append(lines[i].split('|')[1].split(" ")[1:10])


for i in range(len(outputs)):
	print ("input = ", inputs[i])
	print ("output = ", outputs[i])
	print(" ")
	a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	c = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	d = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	e = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	f = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	g = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
	for input in inputs:
		if len(input) == 2:
			c.remove(input[0])
			c.remove(input[1])
		if len(input) == 3:
			print()


# 	for i in output:
# 		print(i)
# 		if len(i) in {2, 3, 7, 4}:
# 			print()


#print(outputs)