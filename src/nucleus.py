"""
Module for managing the population of chromosomes.

"""

import os.path
import random
from copy import deepcopy
from datetime import datetime

import matplotlib.pyplot as plt

from src.chromosome import Chromosome

# Directory to save plots.
PLOT_DIR = 'plots'


class Nucleus:
    """
    Manages a population of chromosomes.

    Attributes:
        population_size (int): The size of the population (must be divisible by 4).
        population (list of Chromosome)
        ind_vars (list): The independent variables.
        dep_vars (list): Dependent variable values.
        samples (list): Sample of the best individual of each generation.
        tournament_size (int): The tournament size to use when performing the selection process.

    """

    def __init__(self, population_size, ind_vars, dep_vars, tournament_size):
        """
        Raises:
            ValueError: If population size not divisible by 4.

        """
        # Raise error if size is not divisible by 4.
        if population_size % 4 != 0:
            raise ValueError('Population size not divisible by 4.')
        self.population_size = population_size
        self.population = []
        self.ind_vars = ind_vars
        self.dep_vars = dep_vars
        self.samples = []
        self.tournament_size = tournament_size

    def generate_population(self):
        """
        Generate the population of Chromosomes.

        """
        for i in range(self.population_size):
            new_chromosome = Chromosome(
                self.ind_vars,
                self.dep_vars
            )
            # Grow the equation.
            new_chromosome.grow_equation_tree()
            self.population.append(new_chromosome)

    def evolve(self, generations):
        """
        Evolve the nucleus, stopping if the error drops below a threshold.

        Args:
            generations (int): The number of generations to evolve.

        Returns:
            bool: True if error dropped below threshold, False if not.

        """
        self.calculate_error()
        for i in range(generations):
            self.reproduce()
            # Find the best individual.
            self.calculate_error()
            best = min(self.population, key=lambda x: x.error)
            # Add best error to samples.
            self.samples.append(best.error)
            # If best is below threshold, exit.
            if best.error < 1.0e-5:
                return True
        return False

    def plot_learning(self, resolution=100):
        """
        Plot the learning curve (changing best error of each generation).

        """
        self.sort()
        # Get the divisor to limit the number of samples.
        step = len(self.samples) // resolution
        if step == 0:
            step = 1
        # Get samples.
        x = list(range(0, len(self.samples), step))
        y = [self.samples[i] for i in x]
        # Setup plot.
        plt.grid(True)
        plt.title('Function Finder Learning Curve: {0}'.format(str(self.population[0])))
        plt.xlabel('Samples every {0} generations'.format(step))
        plt.ylabel('Least error')
        plt.plot(x, y)
        # Save plot.
        timestamp = datetime.now().strftime('%m-%d-%Y_%I-%M-%S-%p')
        name = 'learning_curve_{0}.png'.format(timestamp)
        save_dir = os.path.join(os.path.abspath(PLOT_DIR), name)
        plt.savefig(save_dir, dpi=200)

    def sort(self):
        """
        Sort the population according to error (increasing).

        """
        self.population.sort(key=lambda x: x.error)

    def calculate_error(self):
        """
        Calculate the error of each chromosome.

        """
        for chromosome in self.population:
            try:
                chromosome.error = chromosome.get_error()
            except ZeroDivisionError:
                chromosome.error = float('inf')

    def tournament(self, k):
        """
        Perform the tournament selection process on the population.

        Args:
            k (int): The number of individuals to participate in the tournament (must be divisible by 2).

        Raises:
            ValueError: If selection size not divisible by 2.

        Returns:
            list[Chromosome]: The n/2 winners of the tournament.

        """
        if k % 2 != 0:
            raise ValueError('Selection size not divisible by 2.')
        # Get participants.
        participants = random.sample(self.population, k)
        # Get the winners.
        winners = []
        for i in range(k // 2):
            if participants[i * 2].error < participants[i * 2 + 1].error:
                winners.append(participants[i * 2])
            else:
                winners.append(participants[i * 2 + 1])
        return winners

    @staticmethod
    def get_winner(chromosome_1, chromosome_2):
        """
        Get chromosome with lesser error.

        Args:
            chromosome_1 (Chromosome): The first chromosome.
            chromosome_2 (Chromosome): The second chromosome.

        Returns:
            Chromosome: The chromosome with the lesser error value.

        """
        if chromosome_1.error < chromosome_2.error:
            return chromosome_1
        return chromosome_2

    def alt_reproduce(self):
        """
        Alternate reproduction process.

        """
        # Shuffle the population.
        random.shuffle(self.population)
        new_population = []
        for i in range(self.population_size // 4):
            # Select two chromosomes with lesser error out of current 4 to be parents.
            par_1 = self.get_winner(self.population[i * 4], self.population[i * 4 + 1])
            par_2 = self.get_winner(self.population[i * 4 + 2], self.population[i * 4 + 3])
            # Deepcopy the winners, creating 2 children-to-be.
            child_1 = deepcopy(par_1)
            child_2 = deepcopy(par_2)
            # Crossover, making them children.
            child_1.crossover(child_2)
            # Mutate them.
            child_1.mutate()
            child_2.mutate()
            # Add parents and children to the new population.
            new_population += [par_1, par_2, child_1, child_2]
        # Update the population.
        self.population = new_population

    def reproduce(self):
        """
        Reproduce the population.

        """
        # Update error calculation before reproducing.
        self.calculate_error()
        new_population = []
        for i in range(self.population_size // 4):
            # Perform the tournament selection process.
            winners = self.tournament(self.tournament_size)
            # Deepcopy the winners, creating 2 children-to-be.
            child_1 = deepcopy(winners[0])
            child_2 = deepcopy(winners[1])
            # Mutate them.
            child_1.mutate()
            child_2.mutate()
            # Crossover, making them children.
            child_1.crossover(child_2)
            # Add parents and children to the new population.
            new_population += winners + [child_1, child_2]
        # Update the population.
        self.population = new_population
