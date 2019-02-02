"""
For managing a tree data structure representing equations.

"""
import random
from copy import deepcopy

from src.math_functions import Add, Subtract, Multiply, Divide, IndependentVariable


class EquationTree:
    """
    For representing equations as trees.

    Attributes:
        val (int or float): The value at this node (if applicable).
        op (Add or Subtract or Multiply or Divide): The operator performed at this node (if applicable).
        descendents_cnt (int): The number of descendents of this node.
        children (list of EquationTree): The children of this node.
        is_terminal (bool): Whether the node is terminal or not.
        parent (EquationTree): The parent of this node.
        parent_i (int): The index of this child in the parent's children list.
        depth (int): The depth of this node.

    Notes:
        TERMINAL_SET, FUNCTION_SET, and

    """
    # Possible terminal items and probability of being selected for a node.
    TERMINAL_SET = frozenset()
    TERMINAL_PROB = 0
    # Possible functions and probability of being selected for a node.
    FUNCTION_SET = frozenset()
    FUNCTION_PROB = 0
    # Max Tree depth.
    MAX_DEPTH = 0

    def __init__(self):
        self.val = None
        self.op = None
        self.descendents_cnt = 0
        self.children = []
        self.is_terminal = False
        self.parent = None
        self.parent_i = None
        self.depth = 0

    def __str__(self):
        """
        Show the operation being done or the value at the node.

        Returns: Understandable text.

        """
        if self.val is None:
            return self.op.LABEL
        if isinstance(self.val, IndependentVariable):
            return 'Independent variable: {0}'.format(self.val.symbol)
        return 'Value: {0}'.format(self.val)

    def __deepcopy__(self, memodict=None):
        """
        Recursively deepcopy the subtree.

        Returns: Deep copied subtree.

        """
        new_node = EquationTree()
        new_node.val = self.val
        new_node.op = self.op
        new_node.descendents_cnt = self.descendents_cnt
        new_node.is_terminal = self.is_terminal
        new_node.parent = self.parent
        new_node.parent_i = self.parent_i
        new_node.depth = self.depth
        new_node.children = [deepcopy(child) for child in self.children]
        return new_node

    def init_terminal(self, val):
        """
        Initialize a terminal node.

        Args:
            val (int or float or IndependentVariable): The value at the node.

        """
        self.val = val
        self.is_terminal = True

    def init_internal(self, op):
        """
        Initialize an internal node.

        Args:
            op: The operator.

        """
        self.op = op
        self.is_terminal = False

    @staticmethod
    def pick_terminal():
        """
        Randomly choose whether or not a terminal symbol should be used with given probability.

        Returns:
            bool: True if a terminal symbol should be used or False if an internal symbol should be used.

        """
        # Get random value out of sum of probabilities.
        total = EquationTree.FUNCTION_PROB + EquationTree.TERMINAL_PROB
        rand_val = random.randint(1, total)
        # If value falls between 1 and function probability, pick function symbol.
        if rand_val <= EquationTree.FUNCTION_PROB:
            return False
        # Else, pick terminal symbol.
        return True

    def grow(self):
        """
        Randomly grow a subtree.

        Returns:
            int: The number of descendents of the subtree, including self.

        """
        self.descendents_cnt = 0
        # Set the depth of the node.
        if self.parent is not None:
            self.depth = self.parent.depth + 1
        # Pick either a terminal or function symbol (must choose terminal if max depth exceeded).
        if self.pick_terminal() or self.depth >= EquationTree.MAX_DEPTH:
            rand_select = random.sample(EquationTree.TERMINAL_SET, 1)[0]
            self.init_terminal(rand_select)
            return 1
        rand_select = random.sample(EquationTree.FUNCTION_SET, 1)[0]
        self.init_internal(rand_select)
        # Generate children.
        for i in range(self.op.PARAM_CNT):
            new_child = EquationTree()
            new_child.parent = self
            new_child.parent_i = i
            self.children.append(new_child)
            self.descendents_cnt += new_child.grow()
        return self.descendents_cnt + 1

    def random_select(self):
        """
        Randomly select a node from descendents.

        Returns:
            EquationTree: Randomly selected node.

        """
        # Number of descendents for each child (including the child).
        ind_desc = [child.descendents_cnt + 1 for child in self.children]
        # Make accumulative list of individual descendents so the last entry is the total.
        desc_accum = []
        total = 0
        for desc in ind_desc:
            desc_accum.append(desc + total)
            total += desc
        # Randomly select a number between 0 (representing this node) and the total.
        rand_val = random.randint(0, total)
        # Select self if 0.
        if rand_val == 0:
            return self
        # Find the node to select.
        for i in range(len(self.children) - 1):
            if rand_val <= desc_accum[i]:
                return self.children[i].random_select()
        return self.children[-1].random_select()

    def evaluate(self):
        """
        Evaluate a subtree.

        Returns: The numerical result of evaluation.

        """
        if isinstance(self.val, IndependentVariable):
            return self.val.cur_val
        if self.is_terminal:
            return self.val
        # Evaluate.
        vals = [child.evaluate() for child in self.children]
        return self.op.eval(vals)

    def render_latex(self):
        """
        Render the Latex code for this subtree.

        Returns: Latex code for expression subtree.

        """
        if isinstance(self.val, IndependentVariable):
            return self.val.symbol
        if self.is_terminal:
            return self.val
        rendered = [child.render_latex() for child in self.children]
        return self.op.render_latex(rendered)

    def render(self):
        """
        Render the equation using in-fix notation.

        Returns:
            str: The equation in in-fix notation.

        """
        if isinstance(self.val, IndependentVariable):
            return self.val.symbol
        if self.is_terminal:
            return self.val
        rendered = [child.render() for child in self.children]
        return self.op.render(rendered)
