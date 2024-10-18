import game, random
import geneticAlgorithm as ga
import matplotlib.pyplot as plt

def main(numGenerations, numIndividuals, bestIndividualsToKeep):

    # Initialize the first generation with the specified number of individuals
    generation = ga.Generation(numIndividuals)    

    best_individuals = []
    fitness_averages_per_generation = []
    weights = [2*random.random() - 1 for _ in range(4)]
    best = ga.Individual(weights)
    best_score = 0
    gameSpeed = 500
    for j in range(numGenerations):
        print('\n')
        print(' - - - - Thế hệ hiện tại: {} - - - - '.format(j+1))
        print('\n')

        # Evaluate each individual in the generation
        for i in range(numIndividuals):
            gameState = game.play(generation.individuals[i], gameSpeed, pieceMax=500, quickGame=True)
            generation.individuals[i].fitness(gameState)
            if gameState[2] > best_score:
                best_score = gameState[2]
                best = generation.individuals[i]
            print("Individual: " + str(i + 1) + " score:" + str(generation.individuals[i].score) + str(generation.individuals[i]))
        generation.selection(bestIndividualsToKeep, best_individuals, fitness_averages_per_generation)

        # Reproduce to create a new generation
        generation.reproduce(numIndividuals)

    return best_individuals, fitness_averages_per_generation, best

def save_to_file(lst):
    with open('weights.txt', 'w') as file:
        for item in lst:
            file.write(f'{item}\n')

if __name__ == '__main__':
    numGenerations = int(input("Số thế hệ: "))
    numIndividuals = int(input("Số cá thể: "))
    bestIndividualsToKeep = int(input("Số cá thể tốt nhất được giữ lại: "))

    best_individuals, fitness_averages_per_generation, best = main(numGenerations, numIndividuals, bestIndividualsToKeep)
    
    save_to_file(best.weights)

    #Print and plot the best fitness scores and averages per generation
    print("Best Individuals:")
    print(best_individuals)
    plt.subplot(211)
    plt.title('Fitness of the Best Individuals per Generation')
    plt.plot(best_individuals)
    plt.ylabel("Fitness of the Best Individuals")
    plt.xlabel("Generations")

    plt.subplot(212)
    print("Average Fitness per Generation:")
    print(fitness_averages_per_generation)
    plt.title('Average Fitness of Individuals per Generation')
    plt.plot(fitness_averages_per_generation)
    plt.ylabel("Average Fitness per Generation")
    plt.xlabel("Generations")
    plt.subplots_adjust(top=0.89, bottom=0.11, left=0.12, right=0.95, hspace=0.85, wspace=0.35)

    plt.show()