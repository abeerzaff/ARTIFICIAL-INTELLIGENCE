import random

class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0
        self.calculate_fitness()
    
    def calculate_fitness(self):
        weights = [10, 20, 30, 15, 25]
        values = [60, 100, 120, 75, 90]
        total_weight = sum(g * w for g, w in zip(self.genes, weights))
        total_value = sum(g * v for g, v in zip(self.genes, values))
        self.fitness = total_value if total_weight <= 50 else 0

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, generations):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
        self.population = []
        self.initialize_population()

    def initialize_population(self):
        self.population = [Chromosome([random.choice([0, 1]) for _ in range(5)]) for _ in range(self.population_size)]
    
    def selection(self):
        total_fitness = sum(chromosome.fitness for chromosome in self.population)
        pick = random.uniform(0, total_fitness)
        current = 0
        for chromosome in self.population:
            current += chromosome.fitness
            if current >= pick:
                return chromosome
    
    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            point = random.randint(1, len(parent1.genes) - 1)
            child1 = Chromosome(parent1.genes[:point] + parent2.genes[point:])
            child2 = Chromosome(parent2.genes[:point] + parent1.genes[point:])
            return child1, child2
        return parent1, parent2
    
    def mutate(self, chromosome):
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                chromosome.genes[i] = 1 - chromosome.genes[i]
        chromosome.calculate_fitness()

    def evolve(self):
        for _ in range(self.generations):
            new_population = []
            while len(new_population) < self.population_size:
                parent1 = self.selection()
                parent2 = self.selection()
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                new_population.extend([child1, child2])
            self.population = sorted(new_population, key=lambda x: x.fitness, reverse=True)[:self.population_size]

    def get_best_solution(self):
        return max(self.population, key=lambda x: x.fitness)

ga = GeneticAlgorithm(10, 0.01, 0.7, 20)
ga.evolve()
best_solution = ga.get_best_solution()
print("Best solution:", best_solution.genes, "with value:", best_solution.fitness)
import random

class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0
        self.calculate_fitness()
    
    def calculate_fitness(self):
        weights = [10, 20, 30, 15, 25]
        values = [60, 100, 120, 75, 90]
        total_weight = sum(g * w for g, w in zip(self.genes, weights))
        total_value = sum(g * v for g, v in zip(self.genes, values))
        self.fitness = total_value if total_weight <= 50 else 0

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, generations):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
        self.population = []
        self.initialize_population()

    def initialize_population(self):
        self.population = [Chromosome([random.choice([0, 1]) for _ in range(5)]) for _ in range(self.population_size)]
    
    def selection(self):
        total_fitness = sum(chromosome.fitness for chromosome in self.population)
        pick = random.uniform(0, total_fitness)
        current = 0
        for chromosome in self.population:
            current += chromosome.fitness
            if current >= pick:
                return chromosome
    
    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            point = random.randint(1, len(parent1.genes) - 1)
            child1 = Chromosome(parent1.genes[:point] + parent2.genes[point:])
            child2 = Chromosome(parent2.genes[:point] + parent1.genes[point:])
            return child1, child2
        return parent1, parent2
    
    def mutate(self, chromosome):
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                chromosome.genes[i] = 1 - chromosome.genes[i]
        chromosome.calculate_fitness()

    def evolve(self):
        for _ in range(self.generations):
            new_population = []
            while len(new_population) < self.population_size:
                parent1 = self.selection()
                parent2 = self.selection()
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                new_population.extend([child1, child2])
            self.population = sorted(new_population, key=lambda x: x.fitness, reverse=True)[:self.population_size]

    def get_best_solution(self):
        return max(self.population, key=lambda x: x.fitness)

ga = GeneticAlgorithm(10, 0.01, 0.7, 20)
ga.evolve()
best_solution = ga.get_best_solution()
print("Best solution:", best_solution.genes, "with value:", best_solution.fitness)
