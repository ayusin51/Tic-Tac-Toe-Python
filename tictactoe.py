#! /bin/env python3
# coding: utf-8

# In[1]:

# Tic Tac Toe game


# In[2]:

#from __future__ import print_function


# In[29]:

#from IPython.display import clear_output
def display_board(board):
    '''
        Function to print the board.
    '''
    #clear_output()
    print ('\n'*100)
    print("Player 1 : x \t Player 2 : o")
    print ("\n\n  {x}  |   {y}   |  {z}".format(x = board[1], y = board[2], z = board[3]))
    print ("_____'_______'_____")
    print ("     '       '     ")
    print ("  {x}  |   {y}   |  {z}".format(x = board[4], y = board[5], z = board[6]))
    print ("_____'_______'_____")
    print ("     '       '     ")
    print ("  {x}  |   {y}   |  {z}\n\n".format(x = board[7], y = board[8], z = board[9]))
    


# In[54]:


def player_input():
    '''
        Function that can take in a player input
        and assign their marker as x or o. 
    '''
    inp = input("Enter your choice Player : ")
    inp = inp.lower()
    while (inp != 'x' and inp != 'o'):
        inp = str(input("Enter valid option : ")).lower()
    
    if (inp == 'x'):
        return ('x', 'o')
    return ('o', 'x')
    


# In[55]:

def place_marker(board, marker, position):
    '''
        Function that takes, in the board list object,
        a marker ('X' or 'O'),and a desired position
        (number 1-9) and assigns it to the board.
    '''
    board[position] = marker


# In[56]:

def win_check(board,mark):
    '''
        Function that takes in a board and a mark (X or O),
        and then checks to see if that mark has won
    '''
    if (board[1] == board[2] == board[3] == mark or
        board[4] == board[5] == board[6] == mark or
        board[7] == board[8] == board[9] == mark or
        board[1] == board[4] == board[7] == mark or
        board[2] == board[5] == board[8] == mark or
        board[3] == board[6] == board[9] == mark or
        board[1] == board[5] == board[9] == mark or
        board[3] == board[5] == board[7] == mark):
        
        return True
    return False


# In[57]:

import random
def choose_first():
    '''
        Function that uses the random module
        to randomly decide which player goes first. 
    '''
    global player
    player = random.randint(0, 1)


# In[58]:

def space_check(board, position):
    '''
        Function that returns a boolean indicating
        whether a space on the board is freely available.
    '''
    if (board[position] != 'x' and board[position] != 'o'):
        return True
    return False


# In[59]:

def full_board_check(board):
    '''
        Function that checks if the board is full
        and returns a boolean value. True if full,
        False otherwise.
    '''
    for i in range(1, 10):
        if(board[i] != 'x' and board[i] != 'o'):
            return False
    return True


# In[64]:

def player_choice(board):
    '''
        Function that asks for a player's next position
        (as a number 1-9) and then uses the space_check()
        function to check if its a free position. If it is,
        then return the position for later use.
    '''
    inp = int(input("Enter next position : "))
    while (inp not in range(1, 10) or not space_check(board, inp)):
        inp = int(input("Enter valid position : "))
    if (space_check(board, inp)):
        return inp
    


# In[65]:

def replay():
    '''
        Function that asks the player if they want to play
        again and returns a boolean True if they do want
        to play again.
    '''
    print ("Do You Want To  Plain Again (y/n) : ")
    inp = input()
    if (inp == 'y'):
        return True
    return False


# In[ ]:

print('Welcome to Tic Tac Toe!')

while True:
    
    Board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print ("Player ", turn, " will go first")
    
    game_on = True

    while game_on:
        #Player 1 Turn
        print ("Player 1 : {x}, Player 2 : {y}".format(x = player1_marker, y = player2_marker))
        if turn == 1:
            display_board(Board)
            print ("Player 1 : ")
            pos = player_choice(Board)
            place_marker(Board, player1_marker, pos)
            
            if win_check(Board, player1_marker):
                display_board(Board)
                print("Congo Player 1, You won the game")
                game_on = False
                
            else :
                if full_board_check(Board):
                    display_board(Board)
                    print ("The game is drawww !!")
                else :
                    turn = 2

        else:
            # Player2's turn.
            display_board(Board)
            print ("Player 2 : ")
            pos = player_choice(Board)
            place_marker(Board, player2_marker, pos)
            
            if win_check(Board, player2_marker):
                display_board(Board)
                print("Congo Player 2, You won the game")
                game_on = False
                
            else :
                if full_board_check(Board):
                    display_board(Board)
                    print ("The game is drawww !!")
                else :
                    turn = 1
            
            
            

    if not replay():
        break


# In[ ]:




# In[ ]:



