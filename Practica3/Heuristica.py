
player_x, player_o = 'x', 'o'
 

def isMovesLeft(tablero) :
 
    for i in range(3) :
        for j in range(3) :
            if (tablero[i][j] == '_') :
                return True
    return False
 

def evaluate(b) :
  
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
            if (b[row][0] == player_x) :
                return 10
            elif (b[row][0] == player_o) :
                return -10
 

    for col in range(3) :
      
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
         
            if (b[0][col] == player_x) :
                return 10
            elif (b[0][col] == player_o) :
                return -10

    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
     
        if (b[0][0] == player_x) :
            return 10
        elif (b[0][0] == player_o) :
            return -10
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
     
        if (b[0][2] == player_x) :
            return 10
        elif (b[0][2] == player_o) :
            return -10

    return 0
 

def minimax(tablero, depth, isMax) :
    score = evaluate(tablero)

    if (score == 10) :
        return score
 
    if (score == -10) :
        return score
 
    if (isMovesLeft(tablero) == False) :
        return 0
 
 
    if (isMax) :    
        best = -1000
 
        for i in range(3) :        
            for j in range(3) :
              
                # 
                if (tablero[i][j]=='_') :
                 
                    tablero[i][j] = player_x
 
                   
                 
                    best = max( best, minimax(tablero,
                                              depth + 1,
                                              not isMax) )
 
                    
                    tablero[i][j] = '_'
        return best
 
   
    else :
        best = 1000
 
        # Traverse all cells
        for i in range(3) :        
            for j in range(3) :
              
                
                if (tablero[i][j] == '_') :
                 
                   
                    tablero[i][j] = player_o
 
                    
                    best = min(best, minimax(tablero, depth + 1, not isMax))
 
                    
                    tablero[i][j] = '_'
        return best

def findBestMove(tablero) :
    bestVal = -1000
    bestMove = (-1, -1)
 
    
    for i in range(3) :    
        for j in range(3) :
         
            if (tablero[i][j] == '_') :
             
             
                tablero[i][j] = player_x
 
                moveVal = minimax(tablero, 0, False)
 
  
                tablero[i][j] = '_'
 
            
                if (moveVal > bestVal) :               
                    bestMove = (i, j)
                    bestVal = moveVal
 
    print("The value of the best Move is :", bestVal)
    print()
    return bestMove
# Driver code
tablero = [
    [ 'x', 'o', 'x' ],
    [ 'o', 'o', 'x' ],
    [ '_', '_', '_' ]
]
 
bestMove = findBestMove(tablero)
 
print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])