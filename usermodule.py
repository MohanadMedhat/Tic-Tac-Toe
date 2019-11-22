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
     
     #print("it's " + Current_player + "'s turn")  
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


#Check win or tie
def check_condition():

  #check rows
  if theboard[0] == theboard[1] == theboard[2] != '-' or theboard[3] == theboard[4] == theboard[5] != '-' or theboard[6] == theboard[7] == theboard[8] != '-':
       print(theboard[0] + ' Has Won!!!')
       return True
  
  #check columns
  if theboard[0] == theboard[3] == theboard[6] != '-' or theboard[1] == theboard[4] == theboard[7] != '-' or theboard[2] == theboard[5] == theboard[8] != '-':
       print(theboard[0] + ' Has Won!!!')
       return True
  

def start_game():

  while game_going:

    Turns()

    if check_condition() == True:
      break


    



   

    


display_board(theboard)

start_game()
