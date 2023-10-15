
# ? Below function is the caller of our minimax (alpha-beta pruning) algorithm after prompting user's location.
def play_game(tic_tac):
    display_board(tic_tac)
    while tic_tac.count('_') > 1:
        location = int(input(f'Enter Location to place O at Tic Tac Toe: '))
        while location < 1 or location > 9 or tic_tac[location - 1] != '_':
            if location < 1 or location > 9:
                location = int(input(f'You have entered out of the board location.\nPlease choose another location: '))
            else:
                location = int(input(f'This Location is occupied\nPlease choose another location: '))
        tic_tac[location - 1] = 'O'
        print ("User Move")
        display_board(tic_tac)
        print ("Agent Move")
        state_representation = min_max('X', tic_tac[ : ], float('-inf'), float('inf'))
        
        tic_tac = state_representation[1].copy()
        display_board(tic_tac)
        if check('X', tic_tac) == 10:
            print ("Agent has won the game")
            return
        elif check('O', tic_tac) == -10:
            print ("User has won the game")
            return
    tic_tac[tic_tac.index('_')] = 'X'
    print ('Game has drawn.')

# ? Below function is the implementation of min_max algorithm that generate agent's move efficiently.
def min_max(player, state, alpha, beta):
    
    state_representations = []
    for i in range(len(state)):
        if state[i] == '_':
            temp = state[ : ]
            temp[i] = player
            winner_representation = examine(temp)
            if winner_representation != 0:
                if player == 'X':
                    alpha = max(alpha, winner_representation, alpha, beta)
                elif player == 'O':
                    beta = min(beta, winner_representation)

                state_representations.append( [winner_representation, temp] )
            
            elif player == 'X':
                if temp.count('_') > 0:
                    res = min_max('O', temp, alpha, beta)
                    state_representations.append([res[0], temp])
                    alpha = max(alpha, res[0])
                else:
                    winner_representation = examine(temp)
                    state_representations.append([winner_representation, temp])
                    alpha = max(alpha, winner_representation)

            elif player == 'O':
                if temp.count('_') > 0:
                    res = min_max('X', temp, alpha, beta)
                    state_representations.append([res[0], temp])
                    beta = min(beta, res[0])
                else:
                    winner_representation = examine(temp)
                    state_representations.append([examine(temp), temp])
                    beta = min(beta, winner_representation)
                
            
            if alpha >= beta:
                return [alpha, temp]

    
    if player == 'O':
        return min(state_representations, key = lambda x:x[0])
    elif player == 'X':
        return max(state_representations, key = lambda x:x[0])

# ? Below function will check if the player won the game or not.
def check(player, state):
    flag = True
    for j in range(3): #* Top-Left to Bottom-Right (diagonal)
        if state[(2 * j) + (j * 2)] != player:
            flag = False
            break
    if flag and player == 'X':
        return 10
    elif flag and player == 'O':
        return -10

    flag = True
    for j in range(1, 4): #* Top-Right to Bottom-Left (diagonal)
        if state[(2 * j)] != player:
            flag = False
            break
    if flag and player == 'X':
        return 10
    elif flag and player == 'O':
        return -10

    for i in range(3): #* horizontal
        flag = True
        for j in range(3): 
            if state[(i * 2) + i + j] != player:
                flag = False
                break
        if flag:
            break

    if flag and player == 'X':
        return 10
    elif flag and player == 'O':
        return -10

    for j in range(3): #* vertical
        flag = True
        for i in range(3): 
            if state[(i * 2) + i + j] != player:
                flag = False
                break
        if flag:
            break

    if flag and player == 'X':
        return 10
    elif flag and player == 'O':
        return -10

    return 0

# ? Below function will check which player has won the game or if the game has drawn.
def examine(state):
    #! For Agent
    if check('X', state) == 10:
        return 10
    
    #! For Human
    elif check('O', state) == -10:
        return -10
    
    return 0

# ? Below function (as name states) will display the board in readable format.
def display_board(state):
    for i in range(len(state)):
        if i % 3 == 0 and i != 0: print ()
        print (state[i], end = " ")
    print ('\n')
    

if __name__ == "__main__":
    tic_tac = ['_' for _ in range(9)]
    play_game(tic_tac)


# ! Game Description
# ? The 'X' is the agent's symbol
# ? The 'O' is the user's symbol
# * We are prompting the user's location on the basis of one-based index
# * Since, it is apha-beta pruning we are not searching the whole bunch of other branches which is the key aspect of this strategy.
# ! This game is the interactive one. Just run it and it will handle each kind of handling (If you enter out of bound index and other stuff)