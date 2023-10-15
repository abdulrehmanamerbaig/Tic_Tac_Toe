def play_game(tic_tac):
    display_board(tic_tac)
    while tic_tac.count('_'):
        location = int(input(f'Enter Location to place O at Tic Tac Toe: '))
        while tic_tac[location] != '_':
            location = int(input(f'This Location is occupied\nPlease choose another location: '))
        tic_tac[location] = 'O'
        display_board(tic_tac)
        print ("Agent Move")
        state_representation = min_max('X', tic_tac[ : ])
        
        tic_tac = state_representation[1].copy()
        display_board(tic_tac)
        if check('X', tic_tac) == 1:
            print ("Agent has won the game")
            return
        elif check('O', tic_tac) == -1:
            print ("User has won the game")
            return
    
    print ('Game has drawn.')

def min_max(player, state):
    state_representations = []
    for i in range(len(state)):
        if state[i] == '_':
            temp = state[ : ]
            temp[i] = player
            winner_representation = examine(temp)
            if winner_representation != 0:
                state_representations.append( [winner_representation, temp] )
            
            elif player == 'X':
                if temp.count('_') > 0:
                    res = min_max('O', temp)
                    state_representations.append([res[0], temp])
                else:
                    state_representations.append([examine(temp), temp])


            elif player == 'O':
                if temp.count('_') > 0:
                    res = min_max('X', temp)
                    state_representations.append([res[0], temp])
                else:
                    state_representations.append([examine(temp), temp])

    
    if player == 'O':
        return min(state_representations, key = lambda x:x[0])
    elif player == 'X':
        return max(state_representations, key = lambda x:x[0])


def check(player, state):
    flag = True
    for j in range(3): #* Top-Left to Bottom-Right (diagonal)
        if state[(2 * j) + (j * 2)] != player:
            flag = False
            break
    if flag and player == 'X':
        return 1
    elif flag and player == 'O':
        return -1

    flag = True
    for j in range(1, 4): #* Top-Right to Bottom-Left (diagonal)
        if state[(2 * j)] != player:
            flag = False
            break
    if flag and player == 'X':
        return 1
    elif flag and player == 'O':
        return -1

    for i in range(3): #* horizontal
        flag = True
        for j in range(3): 
            if state[(i * 2) + i + j] != player:
                flag = False
                break
        if flag:
            break

    if flag and player == 'X':
        return 1
    elif flag and player == 'O':
        return -1

    for j in range(3): #* vertical
        flag = True
        for i in range(3): 
            if state[(i * 2) + i + j] != player:
                flag = False
                break
        if flag:
            break

    if flag and player == 'X':
        return 1
    elif flag and player == 'O':
        return -1

    return 0

def examine(state):
    #! For Agent
    if check('X', state) == 1:
        return 1
    
    #! For Human
    elif check('O', state) == -1:
        return -1
    
    return 0

def display_board(state):
    for i in range(len(state)):
        if i % 3 == 0: print ()
        print (state[i], end = " ")
    print ()

if __name__ == "__main__":
    tic_tac = ['X'] + ['_' for _ in range(8)]
    play_game(tic_tac)