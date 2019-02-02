"""
A chromosome container for managing a programmatic solution (equation).

"""
import random
from copy import deepcopy

from src.equation_tree import EquationTree

# Terminal set.
TERMINAL = set(range(-5, 6, 1))


class Chromosome:
    """
    For managing a programmatic solution (equation).

    Attributes:
        equation (EquationTree): The root of an equation tree solution.
        ind_vars (list of IndependentVariable): The independent variables.
        dep_vars (list of int or float): The dependent variables.
        error (float): Cached score of the chromosome.

    """

    def __init__(self, ind_vars, dep_vars):
        self.equation = EquationTree()
        self.ind_vars = ind_vars
        self.dep_vars = dep_vars
        self.error = 0

    def __str__(self):
        return str(self.equation.render())

    def __deepcopy__(self, memodict=None):
        """
        Deepcopy a chromosome.

        Returns: Deep copied chromosome.

        """
        new_chromosome = Chromosome(
            self.ind_vars,
            self.dep_vars
        )
        new_chromosome.equation = deepcopy(self.equation)
        return new_chromosome

    def grow_equation_tree(self):
        """
        Grow an equation tree for this chromosome.

        """
        # Grow the tree.
        self.equation.grow()

    def get_error(self):
        """
        Get the error of the chromosome's equation.

        Returns:
            float: The chromosome's error.

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

    def mutate(self, prob=20):
        """
        Mutate the chromosome with a probability (default is 5:100 (5%)).

        Args:
            prob (int): The probability of a mutation occurring.

        """
        # Exit if probability does not work out.
        if random.randint(1, prob) != 1:
            return
        # Select random node and grow new subtree.
        rand_node = self.equation.random_select()
        # If root node is selected, grow a new tree.
        if rand_node.parent is None:
            self.equation = EquationTree()
            self.grow_equation_tree()
        else:
            new_node = EquationTree()
            rand_node.parent.children[rand_node.parent_i] = new_node
            # Grow a new subtree.
            new_node.grow()

    def crossover(self, other):
        """
        Crossover chromosome with another.

        Args:
            other (Chromosome): The other chromosome to crossover with.

        """
        # Select a random node from both chromosomes.
        self_node = self.equation.random_select()
        other_node = other.equation.random_select()
        # Move self subtree into other, handling if the root node was selected.
        if other_node.parent is None:
            other.equation = self_node
        else:
            other_node.parent.children[other_node.parent_i] = self_node
        # Do the same for other.
        if self_node.parent is None:
            self.equation = other_node
        else:
            self_node.parent.children[self_node.parent_i] = other_node
