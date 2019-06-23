#!/usr/local/bin/python3

import os
import random

def main():
	# Init user

	# Clear screen
	os.system('clear')

	# Greet
	print()
	print("Hello! My name is Mr. Money. Welcome to the world of Moustache.")
	print()
	print("Erm... Could you tell me your name?")
	print()
	username = input("Name: ")
	print()
	print(f"Oh! Your name is {username}. It's nice meeting you. You're ten years old now, and that means it's time for you, like all children, to go out on a capitalist adventure of your \
own. It seems only yesterday that I left my mother and father to pursue greed to the utmost extent.")
	print()

	# Choose class
	classes = [{
		'name': 'knight',
		'money': 5000
	},{
		'name': 'archer',
		'money': 10000
	},{
		'name': 'wizard',
		'money': 15000
	},{
		'name': 'fairy',
		'money': 20000
	}]

	# Ensure acceptable answer choice
	choice = None
	while choice not in range(4):
		print("You can be any type of capitalist you want. So? Which is it?!")
		print("0) Knight")
		print("1) Archer")
		print("2) Wizard")
		print("3) Fairy")
		print()
		choice = input("Choose 0/1/2/3: ")
		if choice.isdigit():
			choice = int(choice)

	# Get class info
	className = classes[choice]['name']
	money = classes[choice]['money']
	#formattedMoney = '{:,}'.format(str(money))
	print()
	print(f"Oh! You chose the {className} class, just like your father!")
	print(f"Unfortunately, this class has no special abilities,")
	print(f"but since I feel bad for ya, I'll start you off with ${money}.")
	print("Go on, get!")

	# Init user
	user = {
		'username': username,
		'className': className,
		'money': money
	}

	# Start game
	print()
	print("[Press ENTER to begin your journey]")
	input()
	os.system('clear')
	print()

	# Populate challenges
	challenges = [None] * 100

	# Challenges 1-60: Adding, Absolute difference, Multiplying, and Squaring
	for i in range(60):
		if i % 2 == 0:
			if (i / 2) % 2 == 0:
				# Add
				x = random.randint(0, 100)
				y = random.randint(0, 100)
				challenges[i] = {
					'x': x,
					'y': y,
					'challenge': f'Evaluate {x} + {y}',
					'answer': x + y
				}
			else:
				# Absolute difference
				x = random.randint(0, 100)
				y = random.randint(0, 100)
				challenges[i] = {
					'x': x,
					'y': y,
					'challenge': f'Evaluate |{x} - {y}|',
					'answer': abs(x - y)
				}
		else:
			if ((i + 1) / 2) % 2 == 0:
				# Multiply
				x = random.randint(0, 20)
				y = random.randint(0, 20)
				challenges[i] = {
					'x': x,
					'y': y,
					'challenge': f'Evaluate {x} * {y}',
					'answer': x * y
				}
			else:
				# Square / Cube
				x = random.randint(0, 10)
				y = random.randint(0, 3)
				answer = x ** y
				challenges[i] = {
					'x': x,
					'y': y,
					'challenge': f'Evaluate {x} ** {y}',
					'answer': x ** y
				}

	# Declare questions and answers
	chemicals = [None] * 10
	symbols = [None] * 10

	historyQuestions = [None] * 10
	historyAnswers = [None] * 10

	weirdQuestions = [None] * 10
	weirdAnswers = [None] * 10

	chemicals = ["carbon", "boron", "beryllium", "cesium", "lead", "mercuy", "iron", "copper", "gold", "ytterbium"]
	symbols = ["C", "B", "Be", "Cs", "Pb", "Hg", "Fe", "Cu", "Au", "Yt"]

	historyQuestions = ["When was the War of 1812?",
						"Who killed John F. Kennedy?",
						"What did Lincoln sign at the end of the Civil War? (omit 'The')",
						"Who founded the Congress of Racial Equality?",
						"What is the term for Ronald Reagan's economic policy?",
						"Who is the founder of Standard Oil?",
						"What was the Market Revolution-era nickname for Cincinatti?",
						"Which Supreme Court case established judicial review?",
						"Which Supreme Court case established the elastic clause?",
						"What was the name of the first permanent English settlement established in Virginia in 1607?"
						]
	historyAnswers = [	'1812',
						'Lee Harvey Oswald',
						'Emancipation Proclamation',
						'James Farmer',
						'Reaganomics',
						'John D. Rockefeller',
						'Porkopolis',
						'Marbury v. Madison',
						'McCulloch v. Maryland',
						'Jamestown'
						]

	weirdQuestions = [	"Type six six times",
						"Type a right chevron",
						"Type an octothorpe",
						"Type an ampersand",
						"Spell the state that's hard to spell",
						"Type the beginning to a secure URL",
						"Type the name of the band that performs 'Dust in the Wind'",
	 					"Type the name of the Pokemon #123",
						"Type the name of what scissors beats",
						"Type this whole sentence backwards forwards"]

	weirdAnswers = ['sixsixsixsixsixsix', '>', '#', '&', 'Mississippi', 'https://', 'Kansas', 'Scyther', 'rock', 'Type this whole sentence backwards forwards']

	# Challenges 1-60: Chemistry, History, Trivia, and Random
	for i in range(60, 100):
		index = random.randint(0,9)
		if i % 2 == 0:
			if (i / 2) % 2 == 0:
				# Chemistry symbol => name
				challenges[i] = {
					'challenge': f'Which chemical has the symbol {symbols[index]}?',
					'answer': chemicals[index]
				}
			else:
				# Chemistry name => symbol
				challenges[i] = {
					'challenge': f"What is the chemical symbol for {chemicals[index]}?",
					'answer': symbols[index]
				}
		else:
			if ((i + 1) / 2) % 2 == 0:
				# History
				challenges[i] = {
					'challenge': historyQuestions[index],
					'answer': historyAnswers[index]
				}
			else:
				# Weird
				challenges[i] = {
					'challenge': weirdQuestions[index],
					'answer': weirdAnswers[index]
				}


    # Explain setting
	print("Woah! You take one step outside of your hometown and find yourself standing on a magnificent parking lot with one hundred squares.")
	print("At the 100th square, there is a bright white light. You look down. You are standing on the 0th square.")
	print("An Old Hobo compels you to do the following and to ALWAYS USE CORRECT CAPITALIZATION:")
	print()

	# Run through challenges
	currentSquare = 0
	turns = 0

	while True:
		i = currentSquare
		# Print current challenge and check answer
		inp = ''
		while inp == '':
			print(f"'{challenges[i]['challenge']}'\n")
			inp = input()
		if i < 60 and inp.isnumeric():
			inp = int(inp)
		# Right answer, progress forward
		if inp == challenges[i]['answer']:
			print(f"\nYou sure are one smart {user['className']}, {user['username']}.")
			moveForward = random.randint(1, 10)
			moneyWon = random.randint(1, 2000)
			if moveForward + currentSquare > 99:
				moveForward = 99 - currentSquare
				print(f"Move on to the end and take ${moneyWon} for your troubles")
				print(f"Old Hobo forced you forwards {moveForward} spaces.")
			else:
				print(f"Move ahead {moveForward} spaces and take ${moneyWon} for your troubles.")
				print(f"Old Hobo forced you forwards {moveForward} spaces.")
				currentSquare += moveForward
			print(f"Old Hobo slipped ${moneyWon} into your wallet.")
			user['money'] += moneyWon
		# Wrong answer
		else:
			print(f"\nYou sure are stupid, {user['username']}, just like your father!")
			print(f"The answer was {challenges[i]['answer']}!")
			moveBackward = random.randint(0, 15)
			moneyLost = random.randint(0, 4000)
			if moveBackward > currentSquare:
				print("Old Hobo angrily forced you backwards to the beginning.")
				currentSquare = 0
			else:
				print(f"Old Hobo angrily forced you backwards {moveBackward} spaces.")
				currentSquare -= moveBackward
			print(f"Old Hobo removed ${moneyLost} from your wallet.")
			user['money'] -= moneyLost
			# 10% chance bribe
			if random.randint(0,10) == 0:
				print("Would you like to pay $6,000 to move back? (y)")
				# Take bribe
				if input() == 'y':
					print("Old Hobo removed $6,000 from your wallet.")
					user['money'] -= 6000
					# 50% bribe backfires
					if random.randint(0, 1) == 0:
						print("Oh, a cheater too, I see. I think I'll just take the rest of that money as well.")
						print(f"Old Hobo removed ${user['money']} from your wallet.")
						user['money'] = 0
					else:
						print("Don't tell your mother about this.")
						print(f"Old Hobo forced you forwards {moveBackward} spaces.")
						currentSquare += moveBackward
				# Deny bribe, no penalty
				else:
					print("Old Hobo gives you a warm, paternal smile.")
					print("That'll do, pig. That'll do.")
					print("Old Hobo slipped $0.29 into your bank account.")
					user['money'] += 0.29
		# Log userdata
		print()
		print("=====================")
		print()
		print(f"Money: ${user['money']}")
		print(f"Current square: {currentSquare}")
		print()
		print("=====================")
		print()

		turns += 1


		# Check if game over
		if user['money'] <= 0:
			print("You lost! Don't tell your mother!")
			print("[Press ENTER to fail your parents]")
			input()

			# Finish game
			os.system('clear')
			print()
			print("==========================================")
			print("God, your parents must be so disappointed!")
			print("==========================================")
			print()
			print(f"Username: {user['username']}")
			print()
			print(f"Class: {user['className']}")
			print()
			print(f"Money: ${user['money']}")
			print()
			print(f"Square: {currentSquare}")
			print()
			print(f"Turn Count: {turns}\n\n")

			print("Thank you for playing. This game was created by Michael Dougherty.\n")
			print("[Press ENTER to exit capitalism]")
			input()
			os.system('clear')


		if currentSquare >= 100:
			print("You've seen the white light. Go tell your mother!\n")
			print("[Press ENTER to walk into the light]")
			input()

			# Finish game
			os.system('clear')
			print()
			print("=========================================")
			print("Congratulations! You finished capitalism!")
			print("=========================================")
			print()
			print(f"Username: {user['username']}")
			print()
			print(f"Class: {user['className']}")
			print()
			print(f"Money: ${user['money']}")
			print()
			print(f"Square: {currentSquare}")
			print()
			print(f"Turn Count: {turns}\n\n")

			print("Thank you for playing. This game was created by Michael Dougherty.\n")
			print("[Press ENTER to exit capitalism]")
			input()
			os.system('clear')


if __name__ == "__main__":
	main()
