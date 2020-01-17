from ortools.algorithms import pywrapknapsack_solver
from item import Item

def dySolve(knapsack, maxWeight):

    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_DYNAMIC_PROGRAMMING_SOLVER, 'test')

    values = []
    weights = [[]]
    capacities = [maxWeight]

    for item in knapsack.items:
        values.append(item.value)
        weights[0].append(item.weight)

    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    return computed_value
