

def main():
	layout =[
		1, 1, 1, 1, 1, 1, 1,
		1, 't', 0, 0, 0, 0, 1,
		1, 1, 1, 0, 0, 0, 1,
		1, 'p', 0, 0, 0, 0, 1,
		1, 1, 1, 0, 0, 0, 1,
		1, 't', 0, 0, 0, 0, 1,
		1, 1, 1, 1, 1, 1, 1,
		]	
	while True:
		
		dimensions = [7, 7]
		display_board(layout, dimensions)
		in_trap =move(layout, dimensions)

def display_board(layout, dimensions):
	length, width = dimensions[0], dimensions[1]

	t=0
	for x in layout:
		if x == 0:
			print('O', end =' ')
		if x == 1:
			print('#', end =' ')
		if x == 'p':
			print('8', end =' ')
		if x == 't':
			print('^', end =' ')
		t+=1
		if t==width:
			print('\n')
			t=0


def move(layout, dimensions):
	length, width = dimensions[0], dimensions[1]
	movement_input = str(input('WSAD:'))

	t=0
	for x in layout:
		if x=='p':
			player_location = t
		t+=1

	print('Playerlocation:', player_location)
	if movement_input == 'w':
		if layout[player_location- width] == 0:
			layout[player_location] = 0
			layout[player_location-width] = 'p'
		elif layout[player_location-width] == 't':
			layout[player_location] = 0
			layout[player_location-width] = 'p'
			return True
	
	if movement_input == 's':
		if layout[player_location+ width] == 0:
			layout[player_location] = 0
			layout[player_location+width] = 'p'
		elif layout[player_location+width] == 't':
			layout[player_location] = 0
			layout[player_location+width] = 'p'
			return True

	if movement_input == 'a':
		if layout[player_location- 1] == 0:
			layout[player_location] = 0
			layout[player_location-1] = 'p'
		elif layout[player_location-1] == 't':
			layout[player_location] = 0
			layout[player_location-1] = 'p'
			return True

	if movement_input == 'd':
		if layout[player_location+1] == 0:
			layout[player_location] = 0
			layout[player_location+1] = 'p'
		elif layout[player_location+1] == 't':
			layout[player_location] = 0
			layout[player_location+1] = 'p'
			return True

	return False

main()