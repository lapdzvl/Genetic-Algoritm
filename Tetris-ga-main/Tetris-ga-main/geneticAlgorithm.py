import random

import tetris as t

# The Individual class initializes an individual with a null score and a vector of weights.
# This class also implements methods to evaluate each individual's performance (fitness function)
# and calculates the best move (left or right and whether to rotate) in the Tetris game.
class Individual():
    # Constructor: Initializes the individual with a vector of weights and a score set to zero.
    def __init__(self, weights):
        self.weights = weights
        self.score = 0

    # String representation: Returns a formatted string representing the individual's weights.
    def __str__(self):
        s = "   Weights: "
        for i in range(len(self.weights)):
            s += "%5.2f " % (self.weights[i])
        return s

    # Fitness function: Calculates the individual's fitness based on the game state.
    # The fitness is currently set to the score (gameState[2]).
    def fitness(self, gameState):
        self.score = gameState[2]

    # Calculate the best move: Determines the optimal move in the game based on the individual's weights.
    # This method uses the product of the input vector and the weight vector to decide the move.
    def calculateBestMove(self, board, piece, nextPiece, quickGame=False):
        bestX = 0 # X position
        bestRotation = 0 # Piece rotation
        bestY = 0 # Y position
        bestScore = -100000 # Initialize to a low score

        # Calculate initial holes and covers in the Tetris board
        # Iterate through all possible rotations and positions to find the best move
        for rotation in range(len(t.PIECES[piece['shape']])):
            for x in range(-2, t.BOARDWIDTH - 2):
                # Calculate move information
                moveInfo = t.calculateMoveInfo(board, piece, x, rotation)
                if moveInfo[0]: # If the move is valid
                    # Calculate the score for this move
                    moveScore1 = 0
                    for i in range(1, 5):
                        moveScore1 += self.weights[i - 1] * moveInfo[i]

                    #next piece
                    newBoard = moveInfo[5]
                    # Calculate initial holes and covers in the Tetris board
                    # Iterate through all possible rotations and positions to find the best move
                    for rotation2 in range(len(t.PIECES[nextPiece['shape']])):
                        for x2 in range(-2, t.BOARDWIDTH - 2):
                            # Calculate move information
                            nextMoveInfo = t.calculateMoveInfo(newBoard, nextPiece, x2, rotation2)
                            if nextMoveInfo[0]: # If the move is valid
                                # Calculate the score for this move
                                moveScore2 = 0
                                for i in range(1, 5):
                                    moveScore2 += self.weights[i - 1] * nextMoveInfo[i]
                                moveScore = moveScore1 + moveScore2
                                # Update the best move if this score is higher
                                if moveScore > bestScore:
                                    bestScore = moveScore
                                    bestX = x
                                    bestRotation = rotation
                                    bestY = piece['y'] # For faster play

        # Set the piece's position and rotation to the best found
        if quickGame:
            piece['y'] = bestY
        else:
            piece['y'] = -2
        piece['x'] = bestX
        piece['rotation'] = bestRotation
        return bestX, bestRotation

# The Generation class manages a collection of individuals (individuos).
# It is responsible for initializing the individuals, performing selection,
# and applying genetic operations like crossover and mutation.
class Generation:
    # Constructor: Initializes a generation with a specified number of individuals and weights.
    def __init__(self, numInd, numWeights=4):
        individuals = []

        # Create initial individuals with random weights
        initialWeights = [-1, 1, -1, -1]
        individual = Individual(initialWeights)
        individuals.append(individual)
        for _ in range(1,numInd):
            initialWeights = [2 * random.random() - 1 for _ in range(numWeights)]
            individual = Individual(initialWeights)
            individuals.append(individual)

        self.individuals = individuals

    # String representation: Prints details of all individuals in the generation.
    def __str__(self):
        for i, individual in enumerate(self.individuals):
            print(f"Individual {i}:\n{individual}")
        return ''

    # Selection: Selects the best-performing individuals based on their scores.
    def selection(self, numSelect, best_individuals, score_averages_generations):
        # Sort individuals by their scores and keep the best ones
        self.individuals = sorted(self.individuals, key=lambda ind: ind.score, reverse=True)

        # Calculate and print average and best scores
        totalScore = sum(ind.score for ind in self.individuals)
        averageScore = totalScore / len(self.individuals)
        print("\n Average Score: ", averageScore)
        score_averages_generations.append(averageScore)

        bestTotalScore = max(ind.score for ind in self.individuals)
        best_individuals.append(bestTotalScore)
        print("Best Score: ", bestTotalScore, "\n")

        # Keep only the top-performing individuals
        self.individuals = self.individuals[:numSelect]
        return self

    # Reproduction: Generates new individuals from the best ones using crossover and mutation.
    def reproduce(self, population, crossoverChance=0.5, mutationChance=0.15):
        while len(self.individuals) < population:
            # Duplicate and mutate individuals
            for k in range(0, len(self.individuals), 2):
                if len(self.individuals) >= population:
                    break
                individual1 = Individual(self.individuals[k].weights[:])
                individual2 = Individual(self.individuals[k + 1].weights[:])

                # Perform crossover and mutation
                self.genCrossOver(individual1, individual2, crossoverChance)
                self.genMut(individual1, mutationChance)
                self.genMut(individual2, mutationChance)

                # Add new individuals to the generation
                self.individuals.append(individual1)
                if len(self.individuals) < population:
                    self.individuals.append(individual2)

        return self

    # genCrossOver: Performs crossover between two individuals.
    def genCrossOver(self, individual1, individual2, crossoverChance):
        for i in range(len(individual1.weights)):
            if random.random() < crossoverChance:
                # Swap weights between the individuals
                individual1.weights[i], individual2.weights[i] = individual2.weights[i], individual1.weights[i]

    # genMut: Performs mutation on an individual.
    def genMut(self, individual, mutationChance):
        for i in range(len(individual.weights)):
            if random.random() < mutationChance:
                # Apply mutation by modifying the weight value
                individual.weights[i] += 2 * random.random() - 1

# Further game logic and integration with the genetic algorithm are implemented below.
# This includes setting up the Pygame environment, running the game loop,
# processing user input, updating the game state, rendering the game, and
# applying the genetic algorithm to optimize gameplay.