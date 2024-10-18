import random
# step 1 goal binary string
target = [1, 1, 1, 1, 1]

# step 2 fitness function
def fitness(individual):
    return sum(individual)

# step 3 randomly ek population generate karo
def create_individual():
    return [random.randint(0,1) for _ in range(5)]

# step 4 slection best individuals 
def selection(population):
    return sorted(population, key=fitness, reverse=True)[:2]

# step 4 crossover mixup krna
def crossover(parent1, parent2):
    crossover_point = random.randint(1,4)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# step 6 mutation thoda randomness add krna
def mutate(individual):
    mutation_point = random.randint(0, 4)

    individual[mutation_point] = 1 if individual[mutation_point] == 0 else 0
    # flip bit
    return individual

# genetic  algorithm function
def genetic_algorithm():
    # step 7 initial population create
    population = [create_individual() for _ in range(4)] # start with 4 random indicuals

    generation = 0
    while True:
        generation += 1
        print(f"Generation {generation}: {population}")

        # step 8 check if any individual has reached the target
        if target in population:
            print(f"Solution found in generation { generation}: {target}")
            break

        # step 9  select the best two individuals
        parents = selection(population)

        # step 10 apply crossover to create children
        child1, child2 = crossover(parents[0], parents[1])

        # step 11 apply mutation to children
        child1 = mutate(child1)
        child2 = mutate(child2)

        # step 12 create a new populatin with parents and children
        population = [parents[0],parents[1], child1, child2]

if __name__ == "__main__":
    genetic_algorithm()