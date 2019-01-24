"""
A chromosome container for managing a programmatic solution (equation).

"""
import random
from copy import deepcopy
from src.equation_tree import EquationTree
from src.math_functions import *


# Terminal set.
TERMINAL = set(range(-5, 6, 1))


class Chromosome:
    """
    For managing a programmatic solution (equation).

    Attributes:
        equation (EquationTree): The root of an equation tree solution.
        terminal_set (set of IndependentVariable or int or float): Possible terminal items.
        function_set (set of Add or Subtract or Multiply or Divide): Possible function.
        all_items_set (Union terminal_set, function_set) .
        ind_vars (list of IndependentVariable): The independent variables.
        dep_vars (list of int or float): The dependent variables.

    """

    def __init__(self, terminal_set, function_set, all_items_set, ind_vars, dep_vars):
        self.equation = None
        self.terminal_set = terminal_set
        self.function_set = function_set
        self.all_items_set = all_items_set
        self.ind_vars = ind_vars
        self.dep_vars = dep_vars
        # TODO: Add attribute for caching scores.

    def __deepcopy__(self, memodict=None):
        """
        Deepcopy a chromosome.

        Returns: Deep copied chromosome.

        """
        new_chromosome = Chromosome(
            self.terminal_set,
            self.function_set,
            self.all_items_set,
            self.ind_vars,
            self.dep_vars
        )
        new_chromosome.equation = deepcopy(self.equation)
        return new_chromosome

    def grow_equation_tree(self):
        """
        Grow an equation tree for this chromosome.

        """
        self.equation = EquationTree()
        # Make a random selection.
        rand_select = random.sample(self.all_items_set, 1)[0]
        if rand_select in self.terminal_set:
            self.equation.init_terminal(rand_select)
        else:
            self.equation.init_internal(rand_select)
        # Grow the tree.
        self.equation.grow(self.terminal_set, self.function_set, self.all_items_set)

    def score(self):
        """
        Get the score (fitness) of the chromosome (the lower the better).

        Returns: The score of the chromosome.

        """
        # Evaluate for each set of dependent variables.
        error = 0.0
        for i in range(len(self.dep_vars)):
            # Update current independent variable value for each.
            for ind_var in self.ind_vars:
                ind_var.set_current_val(i)
            # Evaluate the expression.
            res = self.equation.evaluate()
            # Calculate and add error.
            error += (res - self.dep_vars[i]) ** 2
        return error

    def reproduce(self, other):
        """
        Reproduce chromosome with another.

        Args:
            other (Chromosome): The other chromosome to reproduce with.

        """
        # Select a random node from both chromosomes.
        self_node = self.equation.random_select()
        other_node = other.equation.random_select()
        # TODO: Complete.












