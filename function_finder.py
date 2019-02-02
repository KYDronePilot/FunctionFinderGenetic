"""
Main script for running and finding functions.

"""
import json

from src.nucleus import Nucleus
from src.equation_tree import EquationTree
from src.chromosome import Chromosome
from src.math_functions import *

# Configuration file.
VALUES_FILE = 'values.json'
# Mapping of math function names to themselves.
MATH_FUNCTIONS = {
    'Add': Add,
    'Subtract': Subtract,
    'Multiply': Multiply,
    'Divide': Divide
}


class Main:
    """
    Main class for managing operations.

    Attributes:
        population_size (int): The number of chromosomes in a population.
        generations (int): The number of generations to create.
        function_prob (int): Probability of a function being selected when growing a tree.
        terminal_prob (int): Probability of a terminal symbol being selected when growing a tree.
        values (list): The possible terminal values to select from.
        ind_vars (list): The independent variables and their values to consider.
        dep_vals (list): Dependent values to consider (matches with each independent variable value)
        terminal_symbols (frozenset): The set of possible terminal symbols (values and independent variables).
        functions (frozenset): The set of possible functions that can be selected from.
        max_depth (int): Max depth of the tree.
        tournament_size (int): The tournament size to use when performing selection.
        nucleus (Nucleus): The nucleus which manages all the chromosomes.

    """

    def __init__(self):
        self.population_size = 0
        self.generations = 0
        self.function_prob = 0
        self.terminal_prob = 0
        self.values = []
        self.ind_vars = []
        self.dep_vals = []
        self.terminal_symbols = frozenset()
        self.functions = frozenset()
        self.max_depth = 0
        self.tournament_size = 0
        self.nucleus = None

    def load_attributes(self):
        """
        Load in attributes from the JSON config.

        """
        with open(VALUES_FILE) as data:
            raw = json.load(data)
        self.population_size = raw['population_size']
        self.generations = raw['generations']
        self.function_prob = raw['function_prob']
        self.terminal_prob = raw['terminal_prob']
        self.values = raw['value_set']
        self.max_depth = raw['max_depth']
        self.tournament_size = raw['tournament_size']
        # Create independent variable object for each.
        for var in raw['independent_variables']:
            # Get the values for that symbol.
            values = [ind_vals[var] for ind_vals in raw['independent_values']]
            ind_var = IndependentVariable(var, values)
            self.ind_vars.append(ind_var)
        self.dep_vals = raw['dependent_values']
        self.terminal_symbols = frozenset(self.values + self.ind_vars)
        function_list = [MATH_FUNCTIONS[function] for function in raw['function_set']]
        self.functions = frozenset(function_list)

    def configure_equation_tree(self):
        """
        Configure constants in the equation tree class.

        """
        EquationTree.FUNCTION_SET = self.functions
        EquationTree.FUNCTION_PROB = self.function_prob
        EquationTree.TERMINAL_SET = self.terminal_symbols
        EquationTree.TERMINAL_PROB = self.terminal_prob
        EquationTree.MAX_DEPTH = self.max_depth

    def init_nucleus(self):
        """
        Initialize the nucleus.

        """
        # Create it and generate the population.
        self.nucleus = Nucleus(
            self.population_size,
            self.ind_vars,
            self.dep_vals,
            self.tournament_size
        )
        self.nucleus.generate_population()

    def evolve(self):
        """
        Evolve the nucleus.

        Returns:
            bool: True if optimal individual found, False if not.

        """
        return self.nucleus.evolve(self.generations)


if __name__ == '__main__':
    main = Main()
    # Load in from config file.
    main.load_attributes()
    # Configure the Equation Tree class.
    main.configure_equation_tree()
    # Start the nucleus.
    main.init_nucleus()
    # Evolve.
    rc = main.evolve()
    # Print message declaring whether an ideal individual was found or not.
    if rc:
        print('An ideal individual was found.')
    else:
        print('No ideal individual was found.')
    # Print the best individual.
    main.nucleus.sort()
    print('Error: ', main.nucleus.population[0].error)
    print(main.nucleus.population[0].equation.render())
    main.nucleus.plot_learning()
