import random

# -----------------------------
# Fitness Function
# -----------------------------
def fitness(chromosome):
    conflicts = 0
    n = len(chromosome)

    for i in range(n):
        for j in range(i + 1, n):

            # Same row
            if chromosome[i] == chromosome[j]:
                conflicts += 1

            # Same diagonal
            elif abs(chromosome[i] - chromosome[j]) == abs(i - j):
                conflicts += 1

    max_pairs = n * (n - 1) // 2
    return max_pairs - conflicts


# -----------------------------
# Generate Population
# -----------------------------
def generate_population(size, n):
    population = []

    for _ in range(size):
        chromosome = random.sample(range(n), n)
        population.append(chromosome)

    return population


# -----------------------------
# Tournament Selection
# -----------------------------
def selection(population):
    tournament = random.sample(population, 3)
    return max(tournament, key=fitness)


# -----------------------------
# One Point Crossover
# -----------------------------
def crossover(parent1, parent2):

    point = random.randint(1, len(parent1) - 2)

    child = parent1[:point]

    for gene in parent2:
        if gene not in child:
            child.append(gene)

    return child


# -----------------------------
# Swap Mutation
# -----------------------------
def mutation(chromosome):

    i, j = random.sample(range(len(chromosome)), 2)

    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]

    return chromosome


# -----------------------------
# Replace Weakest
# -----------------------------
def replace(population, child):

    weakest = min(population, key=fitness)

    population.remove(weakest)

    population.append(child)


# -----------------------------
# Print Chessboard
# -----------------------------
def print_board(chromosome):

    n = len(chromosome)

    print("\nChessboard:\n")

    for row in range(n):

        for col in range(n):

            if chromosome[col] == row:
                print("Q", end=" ")
            else:
                print("X", end=" ")

        print()


# -----------------------------
# Main Program
# -----------------------------
n = int(input("Enter value of N: "))

population_size = 50
max_generation = 1000

population = generate_population(population_size, n)

generation = 0

max_fitness = n * (n - 1) // 2

while generation < max_generation:

    generation += 1

    best = max(population, key=fitness)

    if fitness(best) == max_fitness:

        print("\nSolution Found!\n")
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

else:
    print("No solution found.")