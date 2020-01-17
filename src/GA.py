from individual import *
from random import random, randint
import random
import copy


def initialisePop(numItems, numInds):
    # set up population with 'numIndividuals' individuals, each with random chromosomes.
    pop = []
    for _ in range(numInds):
        pop.append(Individual(numItems))

    for indv in pop:
        chromo = []
        for _ in range(0, numItems):
            chromo.append(randint(0, 1))
        indv.chromosome = chromo

    return pop


def fitnessFunction(pop, items, maxWeight):
    # sum value and weight, and determine fitness of each individual
    for indv in pop:
        value = 0
        weight = 0
        for idx, bit in enumerate(indv.chromosome):
            if bit == 1:
                value += items[idx].value
                weight += items[idx].weight
        indv.value = value
        indv.weight = weight
        # if weight is valid, fitness is value, else fitness is 0
        if indv.weight <= maxWeight:
            indv.fitness = indv.value
        else:
            indv.fitness = 0


# Select individuals from pop using roulette wheel approach
def select(pop, numToSelect):
    fitSum = sum(indv.fitness for indv in pop)
    selected = []
    while  len(selected) < numToSelect:
        idx = 0
        rand = randint(0, fitSum)
        while rand > 0:
            rand -= pop[idx].fitness
            idx += 1
        idx -= 1
        selected.append(pop[idx])
    return selected


def tournSelect(pop, numToSelect):
    # tournaments are between 3 individuals
    selected = []
    while len(selected) < numToSelect:
        tourn = []
        for _ in range(3):
            tourn.append(pop[randint(0, len(pop)-1)])

        winner = tourn[0]
        for indv in tourn:
            if indv.fitness > winner.fitness:
                winner = indv
        selected.append(winner)
    return selected


def crossover(selected, popSize):
    newPop = copy.deepcopy(selected)
    while len(newPop) < popSize:
        # choose two random parents from the chosen list 
        rand1 = randint(0, len(selected)-1)
        rand2 = randint(0, len(selected)-1)
        par1 = selected[rand1].chromosome
        par2 = selected[rand2].chromosome

        # create child individuals with single point crossover using par1 and par2
        ch = Individual(len(par1))
        ch.chromosome = par1[:len(par1)//2] + par2[len(par2)//2:]
        ch2 = Individual(len(par1))
        ch2.chromosome = par2[:len(par2)//2] + par1[len(par1)//2:]

        # add the children to newPop
        newPop.append(ch)
        if len(newPop) < popSize:
            newPop.append(ch2)
    return newPop


def mutate(pop, numToMutate, numItems):
    # pick numToMutate individuals from the pop to be mutated
    for _ in range(numToMutate):
        #pick random individual
        rand = randint(0, len(pop)-1)
        chromo = pop[rand].chromosome
        for _ in range(int(numItems*0.2)):
            randBit = randint(0, (len(chromo)-1))
            if chromo[randBit] == 1:
                chromo[randBit] = 0
            else:
                chromo[randBit] = 1


def printPop(pop, gen):
    print("Generation: " + str(gen))
    pop = sorted(pop, key=lambda x: x.fitness, reverse=True)
    for indv in pop:
        print(str(indv.chromosome) + " fitness: " + str(indv.fitness) + " weight: " + str(indv.weight))