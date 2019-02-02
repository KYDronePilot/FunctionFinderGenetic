"""
Collection of math functions for evaluation of expressions.

"""


class IndependentVariable:
    """
    A dependent variable in an equation.

    Attributes:
        symbol (str): The symbol for the variable.
        vals (tuple of int or float): The possible values of this independent variable.
        cur_val (int or float): The current value of the variable.

    """

    def __init__(self, symbol, vals):
        self.symbol = symbol
        self.vals = vals
        self.cur_val = vals[0]

    def set_current_val(self, ind):
        """
        Update current value to the value at the given index.

        Args:
            ind: The index to use.

        """
        self.cur_val = self.vals[ind]


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
    def render_latex(args):
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

    @staticmethod
    def render(args):
        """
        Render subtree for addition using in-fix notation.

        Args:
            args (list): The values

        Returns: Result

        """
        return '({0} + {1})'.format(
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
    def render_latex(args):
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

    @staticmethod
    def render(args):
        """
        Render subtree for subtraction using in-fix notation.

        Args:
            args (list): The values

        Returns: Result

        """
        return '({0} - {1})'.format(
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
    def render_latex(args):
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

    @staticmethod
    def render(args):
        """
        Render subtree for multiplication in-fix notation.

        Args:
            args (list): The values

        Returns: Result

        """
        return '({0} * {1})'.format(
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
    def render_latex(args):
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

    @staticmethod
    def render(args):
        """
        Render subtree for division in-fix notation.

        Args:
            args (list): The values

        Returns: Result

        """
        return '({0} / {1})'.format(
            args[0],
            args[1]
        )
