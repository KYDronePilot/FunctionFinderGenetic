"""
For managing a tree data structure representing equations.

"""
import random

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

    """

    def __init__(self):
        self.val = None
        self.op = None
        self.descendents_cnt = 0
        self.children = []
        self.is_terminal = False

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

    def grow(self, terminals, functions, both):
        """
        Randomly grow a subtree.

        Args:
            terminals (set): Set of possible terminal values.
            functions (set): Set of possible functions.
            both (set): Union of the above sets.

        """
        # if
        # Generate random children.
        children = []
        # for i in range(self.op)

    def random_select(self):
        """
        Randomly select a node from descendents.

        Returns: Randomly selected node.

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
            return self.val.val
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
        return self.op.render(rendered)