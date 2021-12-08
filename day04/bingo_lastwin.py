def get_losing():
	bingo_numbers = None
	card = []
	all_cards = []
	with open("input.txt") as file:
		for line in file:
			line = line.strip()
			if bingo_numbers is None:
				bingo_numbers = line.split(",")
			else:
				if line:
					card.append(line.split())
				else:
					if card:
						all_cards.append(card)
					card = []
	all_cards.append(card)

# start checking and marking
	win = False
	card_i = 0
	x = 0
	vertical_check = [0, 0, 0, 0, 0]
	for num in bingo_numbers:
		print("number with winners: ", num)
		while(card_i < len(all_cards)):
			vertical_check = [0, 0, 0, 0, 0]
			for row in all_cards[card_i]:
				#check for horizontal win
				print
				for i in range(0, 5):
					if row[i] == num:
						row[i] = -1
				for nr in row:
					if nr == -1:
						x += 1
					if x == 5:
						win = True
						break
				#check for vertical win
				for i in range(0, 5):
					if row[i] == -1:
						vertical_check[i] += 1
				for check in vertical_check:
					if check == 5:
						win = True
						break
				x = 0
				if win:
					print("last winning card at index ", len(all_cards), " : ", all_cards[card_i])
					#print("with num = ", num)
					all_cards.pop(card_i)
					if len(all_cards) == 0:
						print ("no more cards left")
						return (None)
					win = False
					break
			else:
				card_i += 1
				continue
			card_i = 0
		card_i = 0
	print(len(all_cards))

#not getting the last winning card
get_losing()
#print("losing card:", losing_card)
losing_card = [[-1, '99', -1, -1, -1], [-1, '30', '10', -1, -1], ['98', -1, -1, -1, '25'], ['76', -1, '29', -1, -1], [-1, -1, -1, -1, -1]]
final_sum = 0
for x in range(0, 5):
	for i in range(0, 5):
		if losing_card[x][i] != -1:
			final_sum += int(losing_card[x][i])
print("final_sum: ",final_sum)

#answer too low: 3980
#answer too high: 15006
#not correct 7688
# 11377! last winning card sum = 367 at bingo nr 31


