"""
For managing a tree data structure representing equations.

"""
import random


class EquationTree:
    """
    For representing equations as trees.

    Attributes:
        descendents_cnt (int): The number of descendents of this node.
        children (list of EquationTree): The children of this node.

    """

    def __init__(self):
        self.descendents_cnt = 0
        self.children = []

    def is_leaf(self):
        """
        Check if node is a leaf.

        Returns: True if it is a leaf, False if not.

        """
        return len(self.children) == 0

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
