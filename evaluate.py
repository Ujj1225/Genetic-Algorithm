# Take expression string, value for x, y and z as input then output result

import math

functions = [
    "sin",
    "cos",
    "tan",
    "cosh",
    "sinh",
    "tanh",
    "log",
    "acos",
    "asin",
    "atan",
    "asinh",
    "acosh",
    "atanh",
    "e",
    "pi",
]


def evaluate_expression(expression, x_value, y_value, z_value):
    # Replace 'x', 'y' and 'z' with provided values in the expression
    expression = (
        expression.replace("x", str(x_value))
        .replace("y", str(y_value))
        .replace("z", str(z_value))
    )

    for i in functions:
        expression = expression.replace(i, "math." + i)

    # Evaluate the expression
    result = eval(expression)

    return result
