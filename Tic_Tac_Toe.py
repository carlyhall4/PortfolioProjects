"""
Course: Introduction to Python Programming
"""
#%%
def author():
    '''
    return your name
    '''
    return 'Caroline Hall'
#%%
import random
import copy
# %%
def DrawBoard(Board):
    print(Board)
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board    
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''
#%% 
def IsSpaceFree(Board, i ,j):
    if Board[i][j] == ' ':
        return True
    else:
        return False
    
    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        return True  if Board[i][j] is empty ' '
        return False if Board[i][j] is not empty
        return False if i or j is invalid (e.g. i = -1 or 100)
    '''
#%%
def GetNumberOfChessPieces(Board):
    totalnumber=0
    for i in range(0,3):
        for j in range(0,3):
            if Board[i][j]!= ' ':
                totalnumber+=1
    
    return totalnumber
        
    '''
    Parameters: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
#%%
def IsBoardFull(Board):
    if GetNumberOfChessPieces(Board)==9:
        return True
    else:
        return False
    
    
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
#%%
def IsBoardEmpty(Board):
    if GetNumberOfChessPieces(Board)==0:
        return True
    else:
        return False
    
    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''
#%%
def UpdateBoard(Board, Tag, Choice):
    Board[Choice[0]][Choice[1]] = Tag
    
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag
    '''
#%%
def HumanPlayer(Tag, Board):
    condition =True
    
    print("Please enter the row and the column.")
    while condition:
        try:
            print("Row:")
            row=input()
            row=int(row)
            print("Column:")
            col=input()
            col=int(col)
            
        except:
            print("Sorry, you did not enter a number. Try again.")
            
        if (IsSpaceFree(Board, row, col))==False:
            print("Sorry, that place is taken. Please enter a different spot.")
        elif (row>2 or col>2):
            print("Sorry, but the spot you entered is invalid")
        else:
            condition=False
    
    ChoiceOfHumanPlayer = (row,col)
    return ChoiceOfHumanPlayer

    
    
    '''
    Parameters:        
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
#%%
def ComputerPlayer(Tag, Board):
    NewBoard=copy.deepcopy(Board)
    ChoiceOfComputerPlayer=()
    check=False
    
    for r in range(3):
        for c in range(3):
            if IsBoardEmpty(NewBoard) == True:
                ChoiceOfComputerPlayer = (0,0)
                check = True
                break
            
            ##horizontal cases:
            if ((NewBoard[r][c]=='O' and NewBoard[r][(c+1)%2]=='O' and IsSpaceFree(NewBoard, r, 2-c))
            or (NewBoard[r][c]=='X' and NewBoard[r][(c+1)%2]=='X' and IsSpaceFree(NewBoard, r, 2-c))):
                ChoiceOfComputerPlayer = (r,2-c)
                check = True
                break 
            if ((NewBoard[r][c]=='O' and NewBoard[r][2-c]=='O' and IsSpaceFree(NewBoard, r, (c+1)%2))
            or (NewBoard[r][c]=='X' and NewBoard[r][2-c]=='X' and IsSpaceFree(NewBoard, r, (c+1)%2))):
                ChoiceOfComputerPlayer = (r,(c+1)%2)
                check = True
                break
            
            ##vertical cases:
            if ((NewBoard[r][c]=='O' and NewBoard[(r+1)%2][c]=='O' and IsSpaceFree(NewBoard, 2-r, c))
            or (NewBoard[r][c]=='X' and NewBoard[(r+1)%2][c]=='X' and IsSpaceFree(NewBoard, 2-r, c))):
                ChoiceOfComputerPlayer = (2-r,c)
                check = True
                break
            if ((NewBoard[r][c]=='O' and NewBoard[2-r][c]=='O' and IsSpaceFree(NewBoard, (r+1)%2, c))
            or (NewBoard[r][c]=='X' and NewBoard[2-r][c]=='X' and IsSpaceFree(NewBoard, (r+1)%2, c))):
                ChoiceOfComputerPlayer = ((r+1)%2,c)
                check = True
                break
            
            ##diagonal cases:
            if ((r==c and NewBoard[r][r]=='O' and NewBoard[(r+1)%2][(r+1)%2]=='O' and IsSpaceFree(NewBoard, 2-(c+r), 2-(c+r)))
            or (r==c and NewBoard[r][r]=='X' and NewBoard[r][r]=='X' and IsSpaceFree(NewBoard, 2-(c+r), 2-(c+r)))):
                ChoiceOfComputerPlayer=(2-(c+r), 2-(c+r))
                check = True
                break
            
            ## (this diagonal case was just done manually because it was confusing):
            if ((NewBoard[0][2]=='O' and NewBoard[2][0]=='O' and IsSpaceFree(NewBoard,1,1))
            or (NewBoard[0][2]=='X' and NewBoard[2][0]=='X' and IsSpaceFree(NewBoard,1,1))):
                ChoiceOfComputerPlayer=(1,1)
                check=True
                break
            if ((NewBoard[1][1]=='O' and NewBoard[2][0]=='O' and IsSpaceFree(NewBoard, 0, 2))
            or (NewBoard[1][1]=='X' and NewBoard[2][0]=='X' and IsSpaceFree(NewBoard, 0, 2))):
                ChoiceOfComputerPlayer=(0,2)
                check=True
                break
            if ((NewBoard[0][2]=='O' and NewBoard[1][1]=='O' and IsSpaceFree(NewBoard, 2, 0))
            or (NewBoard[0][2]=='O' and NewBoard[1][1]=='O' and IsSpaceFree(NewBoard, 2, 0))):
                ChoiceOfComputerPlayer=(2,0)
                check=True
                break
    

    if check ==False:
        while(True):
            row=random.randint(0,2)
            col=random.randint(0,2)
            if IsSpaceFree(Board, row, col) == True:
                ChoiceOfComputerPlayer= (row, col)
                break
 
    return ChoiceOfComputerPlayer
    
    
        
    
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if it is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''
#%%
def Judge(Board):
    
    if ((Board[0][0] =='X' and Board[0][1] == 'X' and Board[0][2] == 'X') ##horizontal case 1
    or (Board[1][0] =='X' and Board[1][1] == 'X' and Board[1][2] == 'X') ##horizontal case 2
    or (Board[2][0] =='X' and Board[2][1] == 'X' and Board[2][2] == 'X') ##horizontal case 3
    or (Board[0][0] =='X' and Board[1][0] == 'X' and Board[2][0] == 'X') ##vertical case 1
    or (Board[0][1] =='X' and Board[1][1] == 'X' and Board[2][1] == 'X') ##vertical case 2
    or (Board[0][2] =='X' and Board[1][2] == 'X' and Board[2][2] == 'X') ##vertical case 3
    or (Board[0][0] =='X' and Board[1][1] == 'X' and Board[2][2] == 'X') ##diagonal case 1
    or (Board[0][2] =='X' and Board[1][1] == 'X' and Board[2][0] == 'X')): ##diagonal case 2
        outcome = 1
    
    elif ((Board[0][0] =='O' and Board[0][1] == 'O' and Board[0][2] == 'O') ##horizontal case 1
    or (Board[1][0] =='O' and Board[1][1] == 'O' and Board[1][2] == 'O') ##horizontal case 2
    or (Board[2][0] =='O' and Board[2][1] == 'O' and Board[2][2] == 'O') ##horizontal case 3
    or (Board[0][0] =='O' and Board[1][0] == 'O' and Board[2][0] == 'O') ##vertical case 1
    or (Board[0][1] =='O' and Board[1][1] == 'O' and Board[2][1] == 'O') ##vertical case 2
    or (Board[0][2] =='O' and Board[1][2] == 'O' and Board[2][2] == 'O') ##vertical case 3
    or (Board[0][0] =='O' and Board[1][1] == 'O' and Board[2][2] == 'O') ##diagonal case 1
    or (Board[0][2] =='O' and Board[1][1] == 'O' and Board[2][0] == 'O')): ##diagonal case 2
        outcome = 2
    
    elif IsBoardFull(Board)==True:
        outcome = 3
        
    else:
        outcome = 0
    
    return outcome
    
    
    '''
    Parameters:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
        (2) if no one wins, then check if it is a tie
                i.e. if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''
#%%
def ShowOutcome(Outcome, NameX, NameO):
    if Outcome == 0:
        print("The game is still in progress")
    elif Outcome == 1:
        print(NameX, "wins!")
    elif Outcome == 2:
        print(NameO, "wins!")
    else:
        print("It is a tie.")
    
    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
#%% read but do not modify this function
def Which_Player_goes_first():
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.  
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print("Computer player goes first")
        PlayerX = ComputerPlayer        
        PlayerO = HumanPlayer     
    else:
        print("Human player goes first")
        PlayerO = ComputerPlayer        
        PlayerX = HumanPlayer           
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Wellcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order of the players
    PlayerX, PlayerO = Which_Player_goes_first()
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # (1)  get the choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get the choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # your code starts from here
    condition =True
    while condition:
        ChoiceX=PlayerX('X',Board)
        UpdateBoard(Board, 'X', ChoiceX)
        DrawBoard(Board)
        outcome = Judge(Board)
        ShowOutcome(outcome, NameX, NameO)
        if outcome != 0:
            break
        ChoiceO=PlayerO('O',Board)
        UpdateBoard(Board, 'O', ChoiceO)
        DrawBoard(Board)
        outcome = Judge(Board)
        ShowOutcome(outcome, NameX, NameO)
        if outcome != 0:
            break
    
    
    
#%% play the game many rounds until the user wants to quit
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print("GameOver")

if __name__ == '__main__':
    PlayGame()
