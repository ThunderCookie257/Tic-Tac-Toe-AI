# This is my tic-tac-toe game
# Board is represented as an array with positions being empty, X or O

# Working game class between player and computer 
# Computer AI utilizes minimax algorithm to get best move 
class game:
    def __init__(self):
        # The board:
        self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        # Game Variables
        self.winner = ""
        self.someWon = False
        self.stillSpace = True
        self.game_On = True
        self.run()

    # prints the state of the board 
    def printBoard(self):
        print(self.board[0],"|", self.board[1],"|", self.board[2])
        print(" _ ","_ "," _ ")
        print(self.board[3],"|", self.board[4],"|", self.board[5])
        print(" _ ","_ "," _ ")
        print(self.board[6],"|", self.board[7],"|", self.board[8])

    # checks state of board 
    def checkState(self):
        # Are there any open spaces
        if ' ' in self.board:
            self.stillSpace = True 
        else: 
            self.stillSpace = False
        
        # Check if somebody won 
        if self.stillSpace:
            self.checkWin()
            if self.someWon:
                self.game_On = False
        else:
            self.checkWin()
            self.game_On = False

    # checks win conditions 
    def checkWin(self):
        # top row 
        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            if self.board[0] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[0] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[0] == ' ':
                self.someWon = False;
        # middle row 
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            if self.board[3] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[3] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[3] == ' ':
                self.someWon = False;
        # bottom row
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            if self.board[6] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[6] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[6] == ' ':
                self.someWon = False;
        # first column
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            if self.board[0] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[0] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[0] == ' ':
                self.someWon = False;
        # second column
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            if self.board[1] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[1] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[1] == ' ':
                self.someWon = False;
        # third column
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            if self.board[2] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[2] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[2] == ' ':
                self.someWon = False;
        # first diag
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            if self.board[0] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[0] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[0] == ' ':
                self.someWon = False;
        # second diag
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            if self.board[2] == 'X':
                self.someWon = True
                self.winner = "Player wins"
            elif self.board[2] == 'O':
                self.someWon = True
                self.winner = "Computer wins"
            elif self.board[2] == ' ':
                self.someWon = False;
        # no matches
        else:
            if self.stillSpace:
                self.someWon = False
            else:
                self.someWon = True
                self.winner = "It's a tie"

    # runs the game loop 
    def run(self):
        self.printBoard()
        print("You will be X, computer will be O")
        print("Enter the position in which you would like to place your X")
        print("Top left is 0, bottom right is 8, go row by row")
        while self.game_On:
            player = input("Enter your position ")
            if self.board[int(player)] == ' ':
                self.board[int(player)] = 'X'
            else:
                print("Error, invalid input")
                break
            comp = self.bestMove()
            self.board[int(comp)] = 'O'
            self.printBoard()
            self.checkState()
        print("Game over:")
        print(self.winner)

    # Below is the minimax algorithm implementation:

    # Modified checkWin that determines who is winning (10 for player, 0 for tie, -10 for computer)
    def evaluate(self):
            # top row 
        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            if self.board[0] == 'X':
                return 10;
            elif self.board[0] == 'O':
                return -10
        # middle row 
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            if self.board[3] == 'X':
                return 10;
            elif self.board[3] == 'O':
                return -10
        # bottom row
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            if self.board[6] == 'X':
                return 10
            elif self.board[6] == 'O':
                return -10
        # first column
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            if self.board[0] == 'X':
                return 10
            elif self.board[0] == 'O':
                return -10
        # second column
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            if self.board[1] == 'X':
                return 10
            elif self.board[1] == 'O':
                return -10
        # third column
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            if self.board[2] == 'X':
                return 10
            elif self.board[2] == 'O':
                return -10
        # first diag
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            if self.board[0] == 'X':
                return 10
            elif self.board[0] == 'O':
                return -10
        # second diag
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            if self.board[2] == 'X':
                return 10
            elif self.board[2] == 'O':
                return -10
        # no matches
        else:
            return 0

    # Returns true if board isnt full
    def moreMoves(self):
        if ' ' in self.board:
            return True
        return False
    
    # Minimax algorithm that determines the value of the board considering all possible situations
    def minimax(self, depth, isMax):
        score = self.evaluate()

        # If minimizer or maximizer has won, return their score 
        if score == 10 or score == -10:
            return score
        
        # If there are no moves left, its a tie 
        if not self.moreMoves():
            return 0
        
        # Maximizer's move 
        if (isMax):
            best = -1000
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    best = max(best, self.minimax(depth + 1,not isMax))
                    self.board[i] = ' '
            return best
        # Minimizer's move 
        else:
            best = 1000
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    best = min(best, self.minimax(depth + 1,not isMax))
                    self.board[i] = ' '
            return best

    # Returns the best move for the computer 
    def bestMove(self):
        bestVal = 1000
        bestMove = -1

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                moveVal = self.minimax(0,True)
                self.board[i] = ' '
                if moveVal < bestVal:
                    bestMove = i
                    bestVal = moveVal
        
        return bestMove

game()