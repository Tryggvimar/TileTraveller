# https://github.com/Tryggvimar/TileTraveller

current_tile = 1.1
s = 'You can travel: '

# fall sem breytir staðsetningu eftir direction
def move(x,y):
    if x == 'N':
        y += 0.1
    elif x == 'S':
        y -= 0.1
    elif x == 'E':
        y += 1
    elif x == 'W':
        y -= 1
    return float(y,1)
    

while current_tile != 3.1:
    if current_tile == 1.1:
        print(s + '(N)orth.')
        direction = ''
        while direction != 'N':
            direction = str(input("Direction: ")).upper()
            if direction == 'N':
                current_tile = move(direction,current_tile)
            else:
                print('Not a valid direction!')

    if current_tile == 1.2:
        print(s + '(N)orth or (E)ast or (S)outh.')
        direction = 'W'
        while direction != 'N' and direction != 'S' and direction != 'E':
            direction = str(input("Direction: ")).upper()
            if direction == 'N' or direction == 'S' or direction == 'E':
                current_tile = move(direction,current_tile)
            else:
                print('Not a valid direction!')

    if current_tile == 1.3:
        print(s + '(E)ast or (S)outh.')
        direction = ''
        while direction != 'E' and direction != 'S':
            direction = str(input("Direction: ")).upper()
            if direction == 'E' or direction == 'S':
                current_tile = move(direction,current_tile)    
            else:
                print('Not a valid direction!')

    if current_tile == 2.1:
        print(s + '(N)orth.')
        direction = ''
        while direction != 'N':
            direction = str(input("Direction: ")).upper()
            if direction == 'N':
                current_tile = move(direction,current_tile)
            else:
                print('Not a valid direction!')

    if current_tile == 2.2:
        print(s + '(S)outh or (W)est.')
        direction = ''
        while direction != 'W' and direction != 'S':
            direction = str(input("Direction: ")).upper()
            if direction == 'S' or direction == 'W':
                current_tile = move(direction,current_tile)
            else:
                print('Not a valid direction!')

    if current_tile == 2.3:
        print(s + '(E)ast or (W)est.')
        direction = ''
        while direction != 'E' and direction != 'W':
            direction = str(input("Direction: ")).upper()
            if direction == 'E' or direction == 'W':
                current_tile = move(direction,current_tile)
            else:
                print('Not a valid direction!')

    if current_tile == 3.2:
        print(s + '(N)orth or (S)outh.')
        direction = ''
        while direction != 'N' and direction != 'S':
            direction = str(input("Direction: ")).upper()
            if direction == 'N' or direction == 'S':
                current_tile = move(direction,current_tile)
            else:
                print('Not a valid direction!')
    
    if current_tile == 3.3:
        print(s + '(S)outh or (W)est.')
        direction = ''
        while direction != 'S' and direction != 'W':
            direction = str(input("Direction: ")).upper()
            if direction == 'S' or direction == 'W':
                current_tile = move(direction,current_tile)
            else:
                print('Not a valid direction!')
print('Victory')