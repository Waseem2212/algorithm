
import random

# Global Variables
TARGET = "HELLO"
POPULATION_SIZE = 100
GENE_POOL = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")

# Step 1: Fitness function
def fitness(individual):
    return sum([1 for i, j in zip(individual, TARGET) if i != j])

# Step 2: Create a random individual
def create_individual():
    return ''.join(random.choices(GENE_POOL, k=len(TARGET)))

# Step 3: Select the best individuals
def selection(population):
    population.sort(key=lambda x: fitness(x))
    return population[:2]

# Step 4: Crossover between two parents
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(TARGET)-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Step 5: Mutation to introduce randomness
def mutate(individual):
    mutation_point = random.randint(0, len(TARGET)-1)
    individual = list(individual)
    individual[mutation_point] = random.choice(GENE_POOL)
    return ''.join(individual)

# Genetic Algorithm function
def genetic_algorithm():
    # Step 6: Initialize the population
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    generation = 0

    while True:
        generation += 1
        print(f"Generation {generation}: {population[0]} Fitness: {fitness(population[0])}")

        # Step 7: Check if the target is found
        if fitness(population[0]) == 0:
            print(f"Solution found in generation {generation}: {population[0]}")
            break

        # Step 8: Select parents
        parents = selection(population)

        # Step 9: Crossover to create children
        child1, child2 = crossover(parents[0], parents[1])

        # Step 10: Mutate the children
        child1 = mutate(child1)
        child2 = mutate(child2)

        # Step 11: Form a new population
        population = parents + [child1, child2] + [create_individual() for _ in range(POPULATION_SIZE-4)]

if __name__ == "__main__":
    genetic_algorithm()
