#These constants can be used to change player symbols, board size, and number of pieces in a row required to win
#If ROWS=6,COLUMNS=7, and INAROW=4 then it is Regular Connect 4
#If ROWS=COLUMNS=INAROW=3 then it is gravity Tic Tac Toe

P1='[X]'
P2='[O]'
EMPTY='[ ]'
ROWS=6
COLUMNS=7
INAROW=4

def play(board,player):
    choice=0
    while(True):
        while(True):
            try:
                choice=int(input("\tWhich column to drop "+player+"? "))#User input
            except:
                print("\tInput an integer.")#Make sure its int
            if(choice>=1 and choice<=COLUMNS):#Make sure its in list bounds
                break
            else:
                print("\tValid colomns are 1-"+str(COLUMNS))#Error if outside bounds
        choice+=(ROWS-1)*COLUMNS-1#Offsets the choice to the bottom row
        while(True):
            if(choice<0):#Only way is if the column is full
                print("\tThis column is full.")
                break
            elif(board[choice]!=EMPTY):#If the spot is occupied offset upwards
                choice-=COLUMNS
            else:#Only if it was a valid choice
                return choice

def checkWin(board,playSpot):
    won=0
    wins={"diagonal":0,"vertical":0,"alternate diagonal":0,"horizontal":0}
    #Check and store how many in a row in each direction
    dT=checkDiag(board,playSpot)
    vT=checkVert(board,playSpot)
    adT=checkAltDiag(board,playSpot)
    hT=checkHori(board,playSpot)
    if(max(dT,vT,adT,hT)<INAROW):#If none of the directions have met the criteria to win exit (not win womp womp)
        return False
    if(dT>=INAROW):#These ifs update the dictionary and tallies the number of directions won in
        won+=1
        wins["diagonal"]=dT
    if(vT>=INAROW):
        won+=1
        wins["vertical"]=vT
    if(adT>=INAROW):
        won+=1
        wins["alternate diagonal"]=adT
    if(hT>=INAROW):
        won+=1
        wins["horizontal"]=hT
    if(won>1):#Won in multiple directions print win statement in multiple steps
        print("\n\t"+player+" won in the ",end="")
        for w in wins:
            if(wins[w]>0):
                print(w+" with "+str(wins[w]),end="")
                won-=1
            else:
                continue
            if(won>1):#This if elif is for proper grammar
                print(",",end=" ")
            elif(won>0):
                print(", and",end=" ")
        print(".")
    else:#Won in a single direction
        print("\n\t"+player+" won the game with "+str(max(dT,vT,adT,hT))+" in a row!")#Print win statemnt
    printBoard()#Prints winning board
    print()
    return True
    

def checkDiag(board,playSpot):#Searches top left then bottom right diagonal
    player=board[playSpot]
    tally=1#How many are in a row
    away=1#How far away to check
    while(True):
        checkSpot=(playSpot-((away)*COLUMNS+1))
        #if it is not a valid index in the list, is not the same player, and not in the expected column (overflow on to the otherside) then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player) and (checkSpot%COLUMNS==playSpot%COLUMNS-away)):
            break
        tally+=1
        away+=1
    away=1
    while(True):
        checkSpot=(playSpot+((away)*(COLUMNS+1)))
        #if it is not a valid index in the list, is not the same player, and not in the expected column (overflow on to the otherside) then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player) and (checkSpot%COLUMNS==playSpot%COLUMNS+away)):
            break
        tally+=1
        away+=1
    return tally 

def checkVert(board,playSpot):#Searches vertically top then bottom
    player=board[playSpot]
    tally=1#How many are in a row
    away=1#How far away to check
    while(True):
        checkSpot=(playSpot-((away)*COLUMNS))
        #if it is not a valid index in the list, and is not the same player then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player)):
            break
        tally+=1
        away+=1
    away=1
    while(True):
        checkSpot=(playSpot+((away)*(COLUMNS)))
        #if it is not a valid index in the list, and is not the same player then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player)):
            break
        tally+=1
        away+=1
    return tally            

def checkAltDiag(board,playSpot):#Searches top right then bottom left diagonal
    player=board[playSpot]
    tally=1#How many are in a row
    away=1#How far away to check
    while(True):
        checkSpot=(playSpot-((away)*(COLUMNS-1)))
        #if it is not a valid index in the list, is not the same player, and not in the expected column (overflow on to the otherside) then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player) and (checkSpot%COLUMNS==playSpot%COLUMNS+away)):
            break
        tally+=1
        away+=1
    away=1
    while(True):
        checkSpot=(playSpot+((away)*(COLUMNS-1)))
        #if it is not a valid index in the list, is not the same player, and not in the expected column (overflow on to the otherside) then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player) and (checkSpot%COLUMNS==playSpot%COLUMNS-away)):
            break
        tally+=1
        away+=1
    return tally 

def checkHori(board,playSpot):#Searches horizontally left then right
    player=board[playSpot]
    tally=1#How many are in a row
    away=1#How far away to check
    while(True):
        checkSpot=(playSpot-away)
        #if it is not a valid index in the list, is not the same player, and not in the expected column (overflow on to the otherside) then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player) and (checkSpot%COLUMNS==playSpot%COLUMNS-away)):
            break
        tally+=1
        away+=1
    away=1
    while(True):
        checkSpot=(playSpot+away)
        #if it is not a valid index in the list, is not the same player, and not in the expected column (overflow on to the otherside) then stop checking this direction
        if not ((checkSpot>=0 and checkSpot<COLUMNS*ROWS) and (board[checkSpot]==player) and (checkSpot%COLUMNS==playSpot%COLUMNS+away)):
            break
        tally+=1
        away+=1
    return tally

def setBoard():
    for i in range(ROWS):
        for n in range(COLUMNS):
            board[i*COLUMNS+n]=EMPTY
    return

def printBoard():
    print("\t",end="")
    for i in range(COLUMNS):#Prints number header for columns
        print("%2d "%(i+1),end=" ")
    print()
    for i in range(ROWS):#Prints the board
        print("\t",end="")
        for n in range(COLUMNS):
            print(board[i*COLUMNS+n],end=" ")
        print("")
    return

#Effective Main
#These first ifs make sure the game is playable
if((INAROW>ROWS) and (INAROW>COLUMNS)):
    print("\tThis board is impossible to win on.")
    exit()
if((INAROW<2)):
    print("This board is too easy to win on.")
    exit()
if((ROWS<1) or (COLUMNS<1)):
    print("This board does not exist.")
    exit()
board=[EMPTY]*(ROWS*COLUMNS)#Initializes the board
player=P1#Initializes the first player
while True:
    plays=0#Used to keep track if board is full
    while (True):#This while is main game loop, print board, play, update board, check win, check tie, swap players
        printBoard()
        playSpot=play(board,player)
        board[playSpot]=player
        plays+=1
        if checkWin(board,playSpot):
            break
        if(plays>=COLUMNS*ROWS):#check for full board
            print("\n\tThe board is full. It's a tie.")
            printBoard()#Print tie board
            print()
            break
        if player==P1:#Swaps players after a move except win or tie
            player=P2
        else:
            player=P1
    setBoard()#Resets the board to EMPTY