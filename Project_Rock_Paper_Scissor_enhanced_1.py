# -*- coding: utf-8 -*-
"""
Course: Introduction to Python Programming
Student Name: Caroline Hall
"""
#%% 
import numpy as np

#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10
# %%
def HumanPlayer(GameRecord):
    val = input("Please enter 'rock', 'paper', or 'scissors'. Otherwise, enter 'game' to view the game record, or 'quit' to quit: ")
    if val == "rock":
        ChoiceOfHumanPlayer="rock"
        return ChoiceOfHumanPlayer
    elif val == "paper":
        ChoiceOfHumanPlayer="paper"
        return ChoiceOfHumanPlayer
    elif val == "scissors":
        ChoiceOfHumanPlayer="scissors"
        return ChoiceOfHumanPlayer
    elif val == "game":
        PrintGameRecord(GameRecord)
    elif val == "quit":
        ChoiceOfHumanPlayer="quit"
        return ChoiceOfHumanPlayer
    else:
        print("Invalid Entry")
        


    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfHumanPlayer, a string that can only be rock, paper, scissors, or quit
    Description:
        This function asks the user to make a choice (i.e. input a string)
        This function will NOT return/exit until it gets a valid input from the user
        valid inputs are: rock or r, paper or p, scissors or s, game or g, quit or q
        quit means the user wants to quit the game
        game means the user wants to see the GameRecord
    '''

# %%
def ComputerPlayer(GameRecord):
    human_rock_prob=0
    human_paper_prob=0
    human_scissors_prob=0
        

    if len(GameRecord[0])==0:
        human_rock_prob=1/3
        human_paper_prob=1/3
        human_scissors_prob=1/3

       
    else:
        rock_sum=0
        paper_sum=0
        scissors_sum=0
        total_rounds= len(GameRecord[0])
        
        for n in range(0, len(GameRecord[0])):
            if GameRecord[0][n]=="rock":
                rock_sum+=1
            elif GameRecord[0][n]=="paper":
                paper_sum+=1
            else:
                scissors_sum+=1
        
        human_rock_prob = rock_sum/total_rounds
        human_paper_prob = paper_sum/total_rounds
        human_scissors_prob = scissors_sum/total_rounds
    
    draw = np.random.choice(['rock', 'paper', 'scissors'], 1, p=[human_scissors_prob, human_rock_prob, human_paper_prob])[0] 
    if draw=='rock':
        ChoiceOfComputerPlayer="rock"
    elif draw=='paper':
        ChoiceOfComputerPlayer="paper"
    else:
        ChoiceOfComputerPlayer="scissors"
        
    return ChoiceOfComputerPlayer
    '''
    Parameter: GameRecord (the record of both players' choices and outcomes)
    Return: ChoiceOfComputerPlayer, a string that can only be rock, paper, scissors
    Description:
        ComputerPlayer will randomly make a choice
        ComputerPlayer should not look at the current choice of HumanPlayer
    '''

# %%
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    if (ChoiceOfComputerPlayer==ChoiceOfHumanPlayer):
        Outcome =0
        return Outcome
    elif (ChoiceOfComputerPlayer=="rock" and ChoiceOfHumanPlayer=="scissors"):
        Outcome=1
        return Outcome
    elif (ChoiceOfComputerPlayer=="scissors" and ChoiceOfHumanPlayer=="paper"):
        Outcome=1
        return Outcome
    elif (ChoiceOfComputerPlayer=="paper" and ChoiceOfHumanPlayer=="rock"):
        Outcome=1
        return Outcome
    else:
        Outcome=2
        return Outcome
    '''
    Parameters:
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: Outcome
        Outcome is 0 if it is a draw/tie
        Outcome is 1 if ComputerPlayer wins
        Outcome is 2 if HumanPlayer wins
    Description:
        this function determines the outcome of a game
    '''

# %%
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    
    print("-----------------Outcome-----------------")  
    print("You chose", ChoiceOfHumanPlayer, "and Computer chose", ChoiceOfComputerPlayer, ".")
    if Outcome==0:
        print("It's a draw.")
    elif Outcome==1:
        print("Computer wins.")
    else:
        print("You win!")
    print("-----------------------------------------")  
    
    '''
    Parameters:
        Outcome is from Judge
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
    Return: None
    Description:
        print Outcome, Choices and Players to the console window
        the message should be human readable
    '''

# %%
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):

    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)

    
    '''
    Parameters: 
        GameRecord is the record of both players' choices and and outcomes
        ChoiceOfComputerPlayer is a string from ComputerPlayer
        ChoiceOfHumanPlayer is a string from HumanPlayer
        Outcome is an integer from Judge
    Return: None
    Description:
        this function updates GameRecord, a list of three lists
    '''
# %%
def PrintGameRecord(GameRecord):
    Humanwins=0
    Computerwins=0
    
    for n in range(0, len(GameRecord[2])):
        if GameRecord[2][n]==1:
            Computerwins+=1
        if GameRecord[2][n]==2:
            Humanwins+=1
   
    print("--------------Game Record--------------")  
    print("The number of rounds is", len(GameRecord[0]))
    print("Human wins", Humanwins, "round(s)" )
    print("Computer wins", Computerwins, "round(s)" )
    
    print("Human, Computer")
    n=0
    while (n<=len(GameRecord[0])-1):
        print(GameRecord[0][n], ",", GameRecord[1][n])
        n=n+1
    print("----------------------------------------") 
    '''
    Parameters: GameRecord (the record of both players' choices and outcomes)
    Return: None
    Description: this function prints the record of the game (see the sample run)
        the number of rounds. human wins x rounds. computer wins y rounds.
        the record of choices.
    '''
# %% the game
def PlayGame():
    GameRecord = [[],[],[]]
    ChoiceOfHumanPlayer=""
    
    
    while (ChoiceOfHumanPlayer !="quit"):
        ChoiceOfHumanPlayer = HumanPlayer(GameRecord)
        if ChoiceOfHumanPlayer=="quit":
            break
    
        if ChoiceOfHumanPlayer=="rock" or ChoiceOfHumanPlayer=="paper" or ChoiceOfHumanPlayer=="scissors":
                
            ChoiceOfComputerPlayer = ComputerPlayer(GameRecord)
            
            Outcome = Judge(ChoiceOfComputerPlayer,ChoiceOfHumanPlayer)
            
            PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer)
            
            UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome)
            
    print("------------------Game Over------------------")
                

    
    '''
    This is the "main" function
    In this function, human and computer play the game until the human/user wants to quit
    '''
# %% do not modify anything below
if __name__ == '__main__':
    PlayGame()
