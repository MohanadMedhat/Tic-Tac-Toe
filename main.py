#board
#start game
#display board
#turn
#check win, lose or tie
#flip player

#---board
theboard = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']

played = []
position = ''

#---X starts
Current_player = 'X'



    
#---checks if game is still going
def game_going():
    #if board[0] == board[1] == board[2]:
    return True



  #display_board(theboard)

#---played Turns
  

 #---Displays Board
def display_board(board):
    print(board[0], '|', board[1], '|', board[2])
    print(board[3], '|', board[4], '|', board[5]) 
    print(board[6], '|', board[7], '|', board[8])

  

#---Turn Handler
def Turns():
     global position
     global played
     global Current_player
     
      
     position = int(input("pick a position from 1 to 9:")) - 1
      #theboard[position] = Current_player
      #display_board(theboard)
      #played.append(int(position))
      

     if position not in played:
       theboard[position] = Current_player
       display_board(theboard)
       played.append(int(position))
     else:
       print('position not valid, try again !')


     if Current_player == 'X':
        Current_player = 'O'
     else:
        Current_player = 'X'

  


      #print(played)



def start_game():

  while game_going:

    Turns()

   

    


display_board(theboard)

start_game()
