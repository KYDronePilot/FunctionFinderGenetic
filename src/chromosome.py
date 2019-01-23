"""
A chromosome container for managing a programmatic solution (equation).

"""
import random
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

    """

    def __init__(self, terminal_set, function_set, all_items_set):
        self.equation = None
        self.terminal_set = terminal_set
        self.function_set = function_set
        self.all_items_set = all_items_set

    def grow_equation_tree(self, choices):
        """
        Grow an equation tree for this chromosome.

        """
        self.equation = EquationTree()


