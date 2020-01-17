class Individual:
    def __init__(self, numItems):
        # initially set up a chromosome with length number of items and all bits 0
        self.weight = 0
        self.value = 0
        self.fitness = 0
        self.chromosome = (0,) * numItems 

