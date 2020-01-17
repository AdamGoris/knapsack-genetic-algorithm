from item import *
from random import randint

class Knapsack:
    def __init__(self, numItems, maxVal, maxWeight):
        self.items = []
        for _ in range(numItems):
            value = randint(1, maxVal)
            weight = randint(1, maxWeight)
            self.items.append(Item(value, weight))
            
"""
#ITEM LIST USED IN TESTING:
        self.items.append(Item(79, 10))
        self.items.append(Item(67, 15))
        self.items.append(Item(43, 3))
        self.items.append(Item(17, 19))
        self.items.append(Item(50, 23))
        self.items.append(Item(36, 41))
        self.items.append(Item(21, 6))
        self.items.append(Item(69, 47))
        self.items.append(Item(56, 36))
        self.items.append(Item(73, 16))
        self.items.append(Item(50, 13))
        self.items.append(Item(96, 16))
        self.items.append(Item(92, 13))
        self.items.append(Item(98, 32))
        self.items.append(Item(87, 14))
        self.items.append(Item(36, 17))
        self.items.append(Item(95, 47))
        self.items.append(Item(73, 5))
        self.items.append(Item(34, 19))
        self.items.append(Item(89, 50))
"""
