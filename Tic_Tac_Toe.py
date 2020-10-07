
### *** TIC TAC TOE GAME *** ###


import sys as s
import os



###To clear the screen

def clear():
    '''Clear the output screen'''
    os.system('cls')


###Reset Board

    #for repaly

def reset_board():
    '''Reset the board'''
    global board
    board=['']*10


###For Repaly

def replay():
    reset_board()
    main_game()
    

###Dispaly the Board
    


def display_board(board):
    
    '''Displays the board'''
    
    print("    |   |    ")
    print(board[1]+'   | '+board[2]+' |  '+board[3])
    print("    |   |    ")
    print("-------------")
    print("    |   |    ")
    print(board[4]+'   | '+board[5]+' |  '+board[6])
    print("    |   |    ")
    print("-------------")
    print(board[7]+'   | '+board[8]+' |  '+board[9])
    print("    |   |    ")
    print("    |   |    ")
    
### Win Check
    
def win_check(board,player):
    
    '''check horizontal , vertical and Diagonal for win'''
    
    if(board[1]==board[2]==board[3]==player) or \
      (board[4]==board[5]==board[6]==player) or \
      (board[7]==board[8]==board[9]==player) or \
      (board[1]==board[4]==board[7]==player) or \
      (board[2]==board[5]==board[8]==player) or \
      (board[3]==board[6]==board[9]==player) or \
      (board[1]==board[5]==board[9]==player) or \
      (board[7]==board[5]==board[3]==player):
        
        return True
    
    else:
        return False
    

###Player Input for Selecting X or O


def player_input():
    
    '''asking player to choose 'X' or 'O' '''
    
    marker=''
    
    #asking for player 1 to choose X or O
    
    while marker != 'X' and marker != 'O':
        
        marker = input("Player 1: choose 'X' or 'O' : ")
        
    #Assigning Player 2 , the opposite marker
        
    player1=marker
    
    if player1=='X':
        player2='O' 
        
    else:
        player2='X'
        
    return (player1,player2)

###Choose Position for mark

def choose_position(board):

    '''choose the position in board'''
    position =0
    
    while position not in [1,2,3,4,5,6,7,8,9]:
        position=int(input("Make your move : (1-9) -> "))
    return position

### Finding new position if entered position is not valid

def find_new_position(board):
    
    '''find new position if position is already occuiped'''
    
    position=0

    while position not in [1,2,3,4,5,6,7,8,9]:
        
        print(" Enter valid position... (1-9) : ")
        position=int(input("Make your move : (1-9) -> "))
    return position


### Placing the Mark

def place_marker(board,marker,position):

    '''placing mark in the board'''
    
    board[position]=marker

### Cheching Board is Full or Not
    
def full_board_check(board):

    '''checks the board is full '''
    
    if " " in board:
        return False
    else: 
        return True

    
### Checking entered position is Valid or Not
    
    #listing valid position
def void_list(board):

    '''listing the available positions'''
    
    temp=[]

    for i in range(0,10):
        if board[i]==' ':
            temp.append(i)
            
    return temp
   
   #checking position is free or not
from copy import deepcopy

def is_available(position,board):

    '''checks the position is available'''
    void_temp=[]
    void_temp2=void_list(board)
    for i in range(0,10):
        if position in void_temp2:
            return True
    
    
##################################################
#################  MAIN  #########################

def main_game():


    clear()

    print('\n\n  ***WELCOME TO TIC TAC TOE GAME***  \n\n')


    board=[' ']*10
    board[0]='0'


    ##selection  of X or O
    
    player1_mark,player2_mark=player_input()
    print('\nplayer 1 -> '+player1_mark)
    print('Player 2 -> '+player2_mark)

    print('\n \n')

    

    turn='Player 1'
    print("  ** player 1 will go first **  \n")

    play_game=input("READY TO PLAY? Enter Y for yes or  Any other key to exit : ")

    if play_game=='Y' or 'y':
        game_status=True

    else:
        game_status=False
        print(" * Byee * ")
        s.exit()

    for i in range(1,1000):


    ##Player 1

        if i%2!=0:
            clear()
            print(" ** Player 1 TURN ** \n\n")
            display_board(board)
            print('\n\n')
            position=choose_position(board)
        
            while not is_available(position,board) and position in [1,2,3,4,5,6,7,8,9]:
                print("** Position not available **\n")
                position=find_new_position(board)
        
            place_marker(board,player1_mark,position)
            clear()
            print(" ** Player 1 TURN ** \n\n")
            display_board(board)
            print('\n\n')

            if full_board_check(board):
                clear()
                display_board(board)
                print('\n\n')
                print("  * TIE GAME *  ")
                rpl=input("\n\n  ** REPLAY?? ** \n\n press Y for yes or any Key to exit...\n ->")
                if rpl=="Y":
                    replay()
                else:
                    print("Byee...")
                    s.exit()
        

            if win_check(board,player1_mark):
                clear()
                print(" ** Player 1 TURN ** \n\n")
                display_board(board)
                print('\n\n')
                print(" * Player 1 Wins !! * ")
                rpl2=input("\n\n  ** REPLAY?? ** \n\n press Y for yes or any Key to exit...\n ->")
                if rpl2=="Y" or 'y':
                    replay()
                else:
                    print("Byee...")
                    s.exit()
            
            
            

    ## Player 2
                

        else:
        
            clear()
            print(" ** Player 2 TURN ** ")
            print('\n\n')
            display_board(board)
            print('\n\n')
            position=choose_position(board)

            while not is_available(position,board) and position in [1,2,3,4,5,6,7,8,9]:
            
                print("** Position not available **\n")
                position=find_new_position(board)
        

            place_marker(board,player2_mark,position)
            clear()
            print(" ** Player 2 TURN ** \n\n")
            display_board(board)
            print('\n\n')

            if full_board_check(board):
                clear()
                display_board(board)
                print('\n\n')
                print("  * TIE GAME *  ")
                rpl3=input("\n\n  ** REPLAY?? ** \n\n press Y for yes or any Key to exit...\n ->")
                if rpl3=="Y" or 'y':
                    replay()
                else:
                    print("Byee...")
                    s.exit()

            if win_check(board,player1_mark):
                clear()
                print(" ** Player 2 TURN ** \n\n")
                display_board(board)
                print('\n\n')
                print(" * Player 2 Wins!! * \n")
                rpl4=inputinput("\n\n  ** REPLAY?? ** \n\n press Y for yes or any Key to exit...\n -> ")
                if rpl4=="Y" or 'y':
                    replay()
                else:
                    print("Byee...")
                    s.exit()
            

main_game()
            
        

        
            
        
        
        
        

    



            
            
                
            
        
    

