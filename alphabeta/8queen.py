import random

# Fitness Function
def fitness(chromosome):
    conflicts = 0

    for i in range(8):
        for j in range(i + 1, 8):

            if chromosome[i] == chromosome[j]:
                conflicts += 1

            elif abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1

    return 28 - conflicts


# Generate Initial Population
def generate_population(size):
    population = []

    for _ in range(size):
        chromosome = random.sample(range(8), 8)
        population.append(chromosome)

    return population


# Tournament Selection
def selection(population):
    tournament = random.sample(population, 3)
    return max(tournament, key=fitness)


# One-Point Crossover
def crossover(parent1, parent2):

    point = random.randint(1, 6)

    child = parent1[:point]

    for gene in parent2:
        if gene not in child:
            child.append(gene)

    return child


# Swap Mutation
def mutation(chromosome):

    i, j = random.sample(range(8), 2)

    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

    return chromosome


# Replace Weakest Chromosome
def replace(population, child):

    weakest = min(population, key=fitness)

    population.remove(weakest)

    population.append(child)


# Print Chessboard
def print_board(chromosome):

    print("\nChessboard:\n")

    for row in range(8):

        for col in range(8):

            if chromosome[col] == row:
                print("Q", end=" ")
            else:
                print("X", end=" ")

        print()


# Main Program
population = generate_population(50)

generation = 0

while True:

    generation += 1

    best = max(population, key=fitness)

    if fitness(best) == 28:

        print("Solution Found!\n")
        print("Best Chromosome:")
        print(best)

        print_board(best)

        print("\nGeneration:", generation)

        break

    parent1 = selection(population)
    parent2 = selection(population)

    child = crossover(parent1, parent2)

    child = mutation(child)
    replace(population, child)