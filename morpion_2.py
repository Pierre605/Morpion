import random

grid = []
corners= [0,2]

def make_grid():
	for y in range(3):
		grid.append([])
		for x in range(3):
			grid[y].append("|_|")
	return grid

def print_grid(grid):
	print("   a  b  c")
	for i, elem in enumerate(grid):
		print(i, ('').join(elem))

def letter_to_int(letter):
	if letter == 'a':
		return 0
	elif letter == 'b':
		return 1
	elif letter == 'c':
		return 2

def win_check(grid):
	count_W_R = 0
	count_L_R = 0
	count_W_C = 0
	count_L_C = 0
	x_col = ''
	y_col = ''

	# rows check
	for y in range(3):
		count_W_R = 0
		count_L_R = 0
		for x in range(3):
			if 'X' in grid[y][x]:
				count_W_R +=1
			elif 'O' in grid[y][x]:
				count_L_R +=1
		if count_W_R == 3:
			y_col = y
			print("YOU WIN !")
			return 'END'
		elif count_L_R == 3:
			print("YOU LOSE")
			return 'END'
	print("count_W_R:", count_W_R)
	print("count_L_R:", count_L_R)

	# columns check
	for y in range(3):
		count_W_C = 0
		count_L_C = 0
		for x in range(3):
			if 'X' in grid[x][y]:
				count_W_C +=1
			elif 'O' in grid[x][y]:
				count_L_C +=1
		if count_W_C == 3:
			x_col = y
			print("YOU WIN !")
			return 'END'
		elif count_L_C == 3:
			print("YOU LOSE")
			return 'END'
	print("count_W_C:", count_W_C)
	print("count_L_C:", count_L_C)

	# diags check
	#diag1
	count_diag1_W = 0
	count_diag1_L = 0
	for y in range(3):
		for x in range(3):
			if y == x:
				if 'X' in grid[y][x]:
					count_diag1_W +=1
				elif 'O' in grid[y][x]:
					count_diag1_L +=1
	print("count_diag1_W:", count_diag1_W)
	print("count_diag1_L:", count_diag1_L)
	if count_diag1_W == 3:
		print("YOU WIN !")
		return 'END'
	elif count_diag1_L == 3:
		print("YOU LOSE")
		return 'END'

	#diag2
	count_diag2_W = 0
	count_diag2_L = 0
	for y in range(3):
		for x in range(3+1):
			if y == 3-x-1:
				if 'X' in grid[y][x]:
					count_diag2_W +=1
				elif 'O' in grid[y][x]:
					count_diag2_L +=1
	print("count_diag2_W:", count_diag2_W)
	print("count_diag2_L:", count_diag2_L)
	if count_diag2_W == 3:
		print("YOU WIN !")
		return 'END'
	elif count_diag2_L == 3:
		print("YOU LOSE")
		return 'END'

	# return ''

def defense(grid):

	print("\ndefense !")
	# rows defense
	y_row = ''
	x_col = ''
	count_X_R = 0
	count_X_C = 0

	for y in range(3):
		count_X_R = 0
		for x in range(3):
			if 'X' in grid[y][x]:
				count_X_R +=1
			elif 'O' in grid[y][x]:
				count_X_R -=1
		if count_X_R == 2:
			y_row = y
	print("y_row:", y_row)
	for y in range(3):
		for x in range(3):
			if y == y_row:
				if 'X' not in grid[y][x]:
					grid[y][x] = "|O|"
					return grid
	print("count_X_R:", count_X_R)
	# columns defense
	for y in range(3):
		count_X_C = 0
		for x in range(3):
			if 'X' in grid[x][y]:
				count_X_C +=1
			elif 'O' in grid[x][y]:
				count_X_C -=1
		if count_X_C == 2:
			x_col = y
	print("x_col:", x_col)
	for y in range(3):
		for x in range(3):
			if y == x_col:  
				if 'X' not in grid[x][y]:
					grid[x][y] = "|O|"
					return grid
	print("count_X_C:", count_X_C)
	# diag defense
	#diag1
	count_diag1 = 0
	for y in range(3):
		for x in range(3):
			if y == x:
				if 'X' in grid[y][x]:
					count_diag1 +=1
				elif 'O' in grid[y][x]:
					count_diag1 -=1
	print("count_diag1_def:", count_diag1)
	if count_diag1 == 2:
		for y in range(3):
			for x in range(3):
				if y == x:          
					if 'X' not in grid[y][x]:
						grid[y][x] = "|O|"
						return grid
	#diag2
	count_diag2 = 0
	for y in range(3):
		for x in range(3+1):
			if y == 3-x-1:
				if 'X' in grid[y][x]:
					count_diag2 +=1
				elif 'O' in grid[y][x]:
					count_diag2 -=1
	print("count_diag2_def:", count_diag2)
	if count_diag2 == 2:
		for y in range(3):
			for x in range(3):
				if y == 3-x-1:          
					if 'X' not in grid[y][x]:
						grid[y][x] = "|O|"
						return grid

	check_def = [count_X_R, count_X_C, count_diag1, count_diag2]
	direct_danger = []
	for count in check_def:
		if count == 2:
			direct_danger.append(1)
	print("direct_attck:", direct_danger)
	if len(direct_danger) == 0:
		print("no danger case")
		
		while True:
			random_X = random.choice([0, 1, 2])
			random_Y = random.choice([0, 1, 2])
			if 'X' not in grid[random_X][random_Y]:
				if 'O' not in grid[random_X][random_Y]:
					grid[random_X][random_Y] = "|O|"
					return grid
				else:
					print("Déja occupé")
			else:
				print("Déja occupé")
	
	return grid


def win_opportunity(grid):
	y_row = ''
	x_col = ''
	count_O_R = 0
	count_O_C = 0

	for y in range(3):
		count_O_R = 0
		for x in range(3):
			if 'O' in grid[y][x]:
				count_O_R +=1
			elif 'X' in grid[y][x]:
				count_O_R -=1
		if count_O_R == 2:
			y_row = y
	print("y_row:", y_row)
	for y in range(3):
		for x in range(3):
			if y == y_row:
				if 'O' not in grid[y][x]:
					grid[y][x] = "|O|"
					return grid
	print("count_O_R:", count_O_R)

	# columns defense
	for y in range(3):
		count_O_C = 0
		for x in range(3):
			if 'O' in grid[x][y]:
				count_O_C +=1
			elif 'X' in grid[x][y]:
				count_O_C -=1
		if count_O_C == 2:
			x_col = y
	print("x_col:", x_col)
	for y in range(3):
		for x in range(3):
			if y == x_col:  
				if 'O' not in grid[x][y]:
					grid[x][y] = "|O|"
					return grid
	print("count_O_C:", count_O_C)

	# diag defense
	#diag1
	count_diag1 = 0
	for y in range(3):
		for x in range(3):
			if y == x:
				if 'O' in grid[y][x]:
					count_diag1 +=1
				elif 'X' in grid[y][x]:
					count_diag1 -=1
	print("count_diag1_O:", count_diag1)
	if count_diag1 == 2:
		for y in range(3):
			for x in range(3):
				if y == x:          
					if 'O' not in grid[y][x]:
						grid[y][x] = "|O|"
						return grid
	#diag2
	count_diag2 = 0
	for y in range(3):
		for x in range(3+1):
			if y == 3-x-1:
				if 'O' in grid[y][x]:
					count_diag2 +=1
				elif 'X' in grid[y][x]:
					count_diag2 -=1
	print("count_diag2_O:", count_diag2)
	if count_diag2 == 2:
		for y in range(3):
			for x in range(3):
				if y == 3-x-1:          
					if 'O' not in grid[y][x]:
						grid[y][x] = "|O|"
						return grid
	return "NO OP"

def second_move(grid):

	for y in range(3):
		if y == 0:
			for x in range(3):
				if x == 0:
					print('HG')
					if ('X' in grid[y][x+1]) or ('X' in grid[y+1][x]) or ('X' in grid[y+1][x+2]) or ('X' in grid[y+2][x+1]) or ('X' in grid[y][x+2]) or ('X' in grid[y+2][x]):
						grid[1][1] = "|O|"
						return grid
					elif ('X' in grid[y+1][x+1]):
						grid[2][2] = "|O|"
						return grid
					elif ('X' in grid[y+2][x+2]):
						grid[0][2] = "|O|"
						return grid

	return grid

def third_move(grid):
	y_row = ''
	x_col = ''
	count_R = 0
	count_C = 0
	print("\nthird move")

	# rows attack
	for y in range(3):
		count_R = 0
		for x in range(3):
			if 'O' in grid[y][x]:
				count_R +=1
			elif 'X' in grid[y][x]:
				count_R +=1
		if count_R == 3:
			break
	print("count_R:", count_R)
	if count_R == 3:
		if 'X' in grid[2][2]:
			grid[2][0] = "|O|"
			return grid
		if 'X' in grid[2][0]:
			grid[2][2] = "|O|"
			return grid
		if 'X' not in grid[2][2] and 'X' not in grid[2][0]:
			grid[2][0] = "|O|"
			return grid

	# columns attack
	for y in range(3):
		count_C = 0
		for x in range(3):
			if 'O' in grid[x][y]:
				count_C +=1
			elif 'X' in grid[x][y]:
				count_C +=1
		if count_C == 3:
			break
	print("count_C:", count_C)
	if count_C == 3:
		if 'X' in grid[2][2]:
			grid[0][2] = "|O|"
			return grid
		if 'X' in grid[0][2]:
			grid[2][2] = "|O|"
			return grid
		if ('X' not in grid[2][2]) and ('X' not in grid[0][2]):
			grid[0][2] = "|O|"
			return grid

	# diag attack
	#diag1
	count_diag1 = 0
	for y in range(3):
		for x in range(3):
			if y == x:
				if 'O' in grid[y][x]:
					count_diag1 +=1
				elif 'X' in grid[y][x]:
					count_diag1 +=1
	print("count_diag1:", count_diag1)
	if count_diag1 == 3:
		if 'X' in grid[0][2]:
			grid[2][0] = "|O|"
			return grid
		if 'X' in grid[2][0]:
			grid[0][2] = "|O|"
			return grid
	#diag2
	count_diag2 = 0
	for y in range(3):
		for x in range(3+1):
			if y == 3-x-1:
				if 'O' in grid[y][x]:
					count_diag2 +=1
				elif 'X' in grid[y][x]:
					count_diag2 +=1
	print("count_diag2:", count_diag2)
	if count_diag2 == 3:
		if 'X' in grid[0][0]:
			grid[2][2] = "|O|"
			return grid
		if 'X' in grid[2][2]:
			grid[0][0] = "|O|"
			return grid

	return 'NO FULL'



def algo_player_hand(grid):
	count_X = 0
	for y in range(3):
		for x in range(3):
			if 'X' in grid[y][x]:
				count_X +=1
	print("count_X:", count_X)

	if count_X == 1:
		grid  = second_move(grid)
		print_grid(grid)
		

	if count_X == 2:
		check = win_check(grid)
		if check == 'END':
			print_grid(grid)
			print("GAME END")
			return 'bye'
		else:
			if win_opportunity(grid) == "NO OP":
				grid_2 = third_move(grid)
				if grid_2 == "NO FULL":
					grid = defense(grid)
					check = win_check(grid)
					print_grid(grid)
					if check == 'END':
						print("GAME END")
						return 'bye'
				else:
					check = win_check(grid_2)
					print_grid(grid_2)
					if check == 'END':
						print("GAME END")
						return 'bye'
			else:
				check = win_check(grid)
				print_grid(grid)
				if check == 'END':
					print("GAME END")
					return 'bye'


	if count_X >= 3 and count_X < 4:
		check = win_check(grid)
		print_grid(grid)
		if check == 'END':
			print("GAME END")
			return 'bye'
		else:
			if win_opportunity(grid) == "NO OP":
				grid = defense(grid)
				check = win_check(grid)
				print_grid(grid)
				if check == 'END':
					print("GAME END")
					return 'bye'
			else:
				check = win_check(grid)
				print_grid(grid)
				if check == 'END':
					print("GAME END")
					return 'bye'
	
	if count_X == 4:
		check = win_check(grid)
		print_grid(grid)
		if check == 'END':
			print("GAME END")
			return 'bye'
		else:
			grid = defense(grid)
			check = win_check(grid)
			print_grid(grid)
			if check == 'END':
				print("GAME END")
				return 'bye'
			else:
				print("EGALITE")
				return 'bye'


def game_hand():
	grid = make_grid()
	grid[0][0] = "|O|"
	print_grid(grid)

	while True:
		input_move_1 = input("Rentrez les coordonnées de votre pion, une à la fois: ")
		if input_move_1 in ['a', 'b', 'c']:
			print(f"Colonne {input_move_1}")
			input_move_1 = letter_to_int(input_move_1)
			input_move = input("Selectionnez la ligne 1, 2 ou 3: ")
			if input_move in ['0', '1', '2']:
				for y in range(3):
					for x in range(3):
						if y == input_move_1 and x == int(input_move):
							if 'X' not in grid[int(x)][y]:
								if 'O' not in grid[int(x)][y]:
									grid[int(x)][y] = "|X|"
									game = algo_player_hand(grid=grid)
									if game == 'bye':
										return 'THE END'
								else:
									print("Déja occupé")
							else:
								print("Déja occupé")
			else:
				print("Wrong Line number !")

		elif input_move_1 in ['0', '1', '2']:
			print(f"Ligne {input_move_1}")
			input_move = input("Selectionnez la colonne a, b ou c: ")
			if input_move in ['a', 'b', 'c']:
				input_move = letter_to_int(input_move)
				for y in range(3):
					for x in range(3):
						if y == input_move and x == int(input_move_1):
							if 'X' not in grid[int(x)][y]:
								if 'O' not in grid[int(x)][y]:
									grid[int(x)][y] = "|X|"
									game = algo_player_hand(grid=grid)
									if game == 'bye':
										return 'THE END'
								else:
									print("Déja occupé")
							else:
								print("Déja occupé")
			else:
				print("Wrong Column letter !")
		else:
			print("Wrong entry !")


game_hand()
    