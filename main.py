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
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

  

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
  if theboard[0] == theboard[1] == theboard[2] != '-':
    print(theboard[0] + ' Has Won!!!')
    return True

  if theboard[3] == theboard[4] == theboard[5] != '-':
    print(theboard[3] + ' Has Won!!!')
    return True

  if theboard[6] == theboard[7] == theboard[8] != '-':
    print(theboard[6] + ' Has Won!!!')
    return True
  
  #check columns
  if theboard[0] == theboard[3] == theboard[6] != '-':
    print(theboard[0] + ' Has Won!!!')
    return True

  if theboard[1] == theboard[4] == theboard[7] != '-':
    print(theboard[1] + ' Has Won!!!')
    return True
    
  if theboard[2] == theboard[5] == theboard[8] != '-':
    print(theboard[2] + ' Has Won!!!')
    return True
  
  #check diagonale
  if theboard[0] == theboard[4] == theboard[8] != '-':
    print(theboard[0] + ' Has Won!!!')
    return True

  if theboard[2] == theboard[4] == theboard[6] != '-':
    print(theboard[0] + ' Has Won!!!')
    return True   

#restarts the game
def play_again():
  play_again = input("Do you want to play again? (Y/N)")

  if play_again == 'Y' or play_again == 'N':
   return play_again


#main start game function
def start_game():

  while game_going:

    Turns()

    if check_condition() == True:
      break

  
    



   

    


display_board(theboard)

start_game()

if play_again() == 'Y':
 
 theboard = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']

 played = []
 position = ''

#---X starts
 Current_player = 'X'
 display_board(theboard)


 start_game()