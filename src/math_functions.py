"""
Collection of math functions for evaluation of expressions.

"""

import math


class IndependentVariable:
    """
    A dependent variable in an equation.

    Attributes:
        symbol (str): The symbol for the variable.
        val (int or float): The current value of the variable.

    """

    def __init__(self, symbol):
        self.symbol = symbol
        self.val = None


class Add:
    """
    For adding two arguments.

    """
    # Operation label.
    LABEL = 'Addition'
    # Number of parameters.
    PARAM_CNT = 2

    @staticmethod
    def eval(args):
        """
        Add two arguments.

        Args:
            args (list): The values

        Returns: Result

        """
        return args[0] + args[1]

    @staticmethod
    def render(args):
        """
        Get Latex code for addition.

        Args:
            args (list): The values

        Returns: Result

        """
        return ' \\left( {0} + {1} \\right) '.format(
            args[0],
            args[1]
        )


class Subtract:
    """
    For subtracting two arguments.

    """
    # Operation label.
    LABEL = 'Subtraction'
    # Number of parameters.
    PARAM_CNT = 2

    @staticmethod
    def eval(args):
        """
        Subtract two arguments.

        Args:
            args (list): The values

        Returns: Result

        """
        return args[0] - args[1]

    @staticmethod
    def render(args):
        """
        Get Latex code for subtraction.

        Args:
            args (list): The values

        Returns: Result

        """
        return ' \\left( {0} - {1} \\right) '.format(
            args[0],
            args[1]
        )


class Multiply:
    """
    For multiplying two arguments.

    """
    # Operation label.
    LABEL = 'Multiplication'
    # Number of parameters.
    PARAM_CNT = 2

    @staticmethod
    def eval(args):
        """
        Multiply two arguments.

        Args:
            args (list): The values

        Returns: Result

        """
        return args[0] * args[1]

    @staticmethod
    def render(args):
        """
        Get Latex code for multiplication.

        Args:
            args (list): The values

        Returns: Result

        """
        # If values are not both numbers, juxtaposition can be used.
        if (
                (isinstance(args[0], int) or isinstance(args[0], float)) ^
                (isinstance(args[1], int) or isinstance(args[1], float))
        ):
            return '{0} {1}'.format(
                args[0],
                args[1]
            )
        # Else, use times sign.
        return ' {0} \\times {1} '.format(
            args[0],
            args[1]
        )


class Divide:
    """
    For dividing two arguments.

    """
    # Operation label.
    LABEL = 'Division'
    # Number of parameters.
    PARAM_CNT = 2

    @staticmethod
    def eval(args):
        """
        Divide two arguments.

        Args:
            args (list): The values

        Returns: Result

        """
        return args[0] / args[1]
    
    @staticmethod
    def render(args):
        """
        Get Latex code for division.

        Args:
            args (list): The values

        Returns: Result

        """
        return ' \\frac{{{0}}}{{{1}}} '.format(
            args[0],
            args[1]
        )

# 
# class Math:
#     """
#     Some math functions for evaluation.
# 
#     """
# 
#     @staticmethod
#     def add(args):
#         """
#         Add two arguments.
# 
#         Args:
#             args (list): List of numerical args.
# 
#         Returns: Result.
# 
#         """
#         return args[0] + args[1]
# 
#     @staticmethod
#     def subtract(args):
#         """
#         Subtract two arguments.
# 
#         Args:
#             args (list): List of numerical args.
# 
#         Returns: Result.
# 
#         """
#         return args[0] - args[1]
# 
#     @staticmethod
#     def multiply(args):
#         """
#         Multiply two arguments.
# 
#         Args:
#             args (list): List of numerical args.
# 
#         Returns: Result.
# 
#         """
#         return args[0] * args[1]
# 
#     @staticmethod
#     def divide(args):
#         """
#         Divide two arguments.
# 
#         Args:
#             args (list): List of numerical args.
# 
#         Returns: Result.
# 
#         """
#         return args[0] / args[1]






