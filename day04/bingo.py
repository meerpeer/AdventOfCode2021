def get_winning():
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
	i = 0
	x = 0
	vertical_check = [0, 0, 0, 0, 0]
	for num in bingo_numbers:
		for card in all_cards:
			for row in card:
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
					print("bingo num win: ", num)
					return(card)
			vertical_check = [0, 0, 0, 0, 0]

winning_card = get_winning()
print("winning card:", winning_card)
final_sum = 0
for x in range(0, 5):
	for i in range(0, 5):
		if winning_card[x][i] != -1:
			final_sum += int(winning_card[x][i])
print("final_sum: ",final_sum) 

#answer too low: 50854
#answer too high: 61664
#correct answer = 58374 with