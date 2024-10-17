import time, pygame
from pygame.locals import *
import tetris as t
import geneticAlgorithm as ga
# Set up the screen size
size = [640, 480]
screen = pygame.display.set_mode((size[0], size[1]))

# Function to play the game with a given individual from the genetic algorithm
def play(individual, gameSpeed, pieceMax = 500, quickGame=False):
    t.FPS = int(gameSpeed)
    t.main()  # Initialize the Tetris game

    board = t.getBlankBoard()
    lastFallTime = time.time()
    score = 0
    completedLine = 0
    level, fallFreq = t.calculateLevelAndFallFreq(completedLine)

    fallingPiece = t.getNewPiece()
    nextPiece = t.getNewPiece()
    individual.calculateBestMove(board, fallingPiece, nextPiece)

    piecesPlayed = 0
    linesDestroyed = [0, 0, 0, 0]  # Combos

    alive = True
    won = False

    while alive:  # Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Game exited by user")
                exit()

        if fallingPiece is None:
            fallingPiece = nextPiece
            nextPiece = t.getNewPiece()

            # Decide the best move based on the individual's weights
            individual.calculateBestMove(board, fallingPiece, nextPiece, quickGame)

            piecesPlayed += 1

            lastFallTime = time.time()

            if not t.isValidPosition(board, fallingPiece):
                alive = False

        if quickGame or time.time() - lastFallTime > fallFreq:
            if not t.isValidPosition(board, fallingPiece, adjY=1):
                t.addToBoard(board, fallingPiece)
                numLines = t.removeCompleteLines(board)
                if numLines == 1:
                    score += 40*level
                    linesDestroyed[0] += 1
                elif numLines == 2:
                    score += 100*level
                    linesDestroyed[1] += 1
                elif numLines == 3:
                    score += 300*level
                    linesDestroyed[2] += 1
                elif numLines == 4:
                    score += 1200*level
                    linesDestroyed[3] += 1
                completedLine += numLines
                level, fallFreq = t.calculateLevelAndFallFreq(completedLine)
                fallingPiece = None
            else:
                fallingPiece['y'] += 1
                lastFallTime = time.time()

        if not quickGame:
            drawOnScreen(board, score, level, nextPiece, fallingPiece)

        if piecesPlayed >= pieceMax:
            alive = False
            won = True

    gameState = [piecesPlayed, linesDestroyed, score, won]
    return gameState

# Function to draw the game state on the screen
def drawOnScreen(board, score, level, nextPiece, fallingPiece):
    t.DISPLAYSURF.fill(t.BGCOLOR)
    t.drawBoard(board)
    t.drawStatus(score, level)
    t.drawNextPiece(nextPiece)
    if fallingPiece is not None:
        t.drawPiece(fallingPiece)

    pygame.display.update()
    t.FPSCLOCK.tick(t.FPS)

def read_from_file():
    with open('weights.txt', 'r') as file:
        lines = file.readlines()
    return [int(line.strip()) for line in lines]

# Main function to run the game
if __name__ == '__main__':
    initialWeights = read_from_file()

    print(initialWeights)
    individual = ga.Individual(initialWeights)
    
    print(play(individual, 500, pieceMax=float('inf')))
