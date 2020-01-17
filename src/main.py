from knapsack import *
from individual import *
from item import *
from GA import *
from random import randint
from dynamicSolver import dySolve


POP_SIZE = 100
NUM_GENS = 500
NUM_ITEMS = 20
MAX_ITEM_VALUE = 100
MAX_ITEM_WEIGHT = 50
MAX_TOTAL_WEIGHT = 10 * NUM_ITEMS
SELECTION_RATE = 0.2
MUTATION_RATE = 0.15


def main():
    knapsack = Knapsack(NUM_ITEMS, MAX_ITEM_VALUE, MAX_ITEM_WEIGHT)

    # get optimal solution using ortools dynamic knapsack solver
    optSol = dySolve(knapsack, MAX_TOTAL_WEIGHT)

    gen = 0
    # Setup initial population 
    pop = initialisePop(NUM_ITEMS, POP_SIZE)

    # Get fitness of initial pop

    for _ in range(NUM_GENS):
        gen += 1
        fitnessFunction(pop, knapsack.items, MAX_TOTAL_WEIGHT)
        printPop(pop, gen)

        # Selection
        numToSelect = len(pop) * SELECTION_RATE
        selectedIndvs = tournSelect(pop, numToSelect)

        # Crossover
        pop = crossover(selectedIndvs, len(pop))

        # Mutation
        numToMutate = int(len(pop) * MUTATION_RATE)
        mutate(pop, numToMutate, NUM_ITEMS)

    # Dynamic Programming Solution
    print("")
    print("Dynamic Programming Solution: " + str(optSol))


if __name__ == '__main__':
    main()