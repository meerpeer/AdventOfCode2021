
# Helper functions
def contains_more(str1, str2, set):
	str1_cmp_nr = 0
	str2_cmp_nr = 0
	for c in set:
		if c in str1:
			str1_cmp_nr += 1
	for c in set:
		if c in str2:
			str2_cmp_nr += 1
	if str1_cmp_nr > str2_cmp_nr:
		return str1
	return str2

def is_number(str1, str2):
	if len(str1) is not len(str2):
		return 0
	for c in str1:
		if c not in str2:
			return 0
	return 1

def contains_all(str, set):
	for c in set:
		if c not in str:
			return 0
	return 1

inputs = []
outputs = []
with open("input.txt") as file:
	lines = file.readlines()
	for i in range(len(lines)):
		lines[i] = lines[i].split('\n')[0]
		inputs.append(lines[i].split('|')[0].split(" ")[0:10])
		outputs.append(lines[i].split('|')[1].split(" ")[1:10])

final_sum = 0

for i in range(len(outputs)):
	# print ("input = ", inputs[i])
	# print ("output = ", outputs[i])
	numbers = [""] * 10
	len_5s = []
	len_6s = []

	#find 1,4, 7 and 8. put the rest in their length arrays
	for input in inputs[i]:
		if len(input) == 2:
			numbers[1] = input
		if len(input) == 3:
			numbers[7] = input
		if len(input) == 4:
			numbers[4] = input
		if len(input) == 7:
			numbers[8] = input
		if len(input) == 5:
			len_5s.append(input)
		if len(input) == 6:
			len_6s.append(input)

	# in the len 5's array:
	# 	find 3 using 1
	# 	find 5 using 4
	#	last len(5) is 2
	for input in len_5s:
		if contains_all(input, numbers[1]):
			numbers[3] = input
			len_5s.remove(input)
			break
	if contains_more(len_5s[0], len_5s[1], numbers[4]) == len_5s[0]:
		numbers[5] = len_5s[0]
		numbers[2] = len_5s[1]
	else:
		numbers[5] = len_5s[1]
		numbers[2] = len_5s[0]

	# in the len 6 array
	#	find 9 with 4
	#	find 0 with 1
	#	last one is 6
	for input in len_6s:
		if contains_all(input, numbers[4]):
			numbers[9] = input
			len_6s.remove(input)
			break
	for input in len_6s:
		if  contains_all(input, numbers[1]):
			numbers[0] = input
		else:
			numbers[6] = input
	# print("numbers in order", numbers)
	# print(" ")

	number_str = ""
	for output in outputs[i]:
		for x in range(len(numbers)):
			if(is_number(output, numbers[x])):
				number_str += str(x)

	print("numberstr", number_str)
	final_sum += int(number_str)
print(final_sum)