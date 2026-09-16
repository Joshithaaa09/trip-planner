import ast
import operator
import re

from crewai.tools import tool


class CalculatorTools:

    @staticmethod
    @tool("Make a calculation")
    def calculate(operation: str) -> str:
        """
        Perform safe mathematical calculations.

        Supported operations include addition, subtraction,
        multiplication, division, powers, modulo, and parentheses.
        """

        try:

            if not isinstance(operation, str):
                return "Error: Calculation must be provided as text."

            operation = operation.strip()

            if not operation:
                return "Error: Empty calculation."

            # Only allow mathematical characters.
            if not re.fullmatch(
                r"[0-9+\-*/().% ]+",
                operation
            ):
                return (
                    "Error: Invalid characters in mathematical expression."
                )

            allowed_operators = {

                ast.Add: operator.add,

                ast.Sub: operator.sub,

                ast.Mult: operator.mul,

                ast.Div: operator.truediv,

                ast.Pow: operator.pow,

                ast.Mod: operator.mod,

                ast.USub: operator.neg,

                ast.UAdd: operator.pos,
            }

            tree = ast.parse(
                operation,
                mode="eval"
            )

            def evaluate(node):

                if isinstance(
                    node,
                    ast.Expression
                ):
                    return evaluate(node.body)

                if isinstance(
                    node,
                    ast.Constant
                ):
                    if isinstance(
                        node.value,
                        (int, float)
                    ):
                        return node.value

                    raise ValueError(
                        "Invalid constant."
                    )

                if isinstance(
                    node,
                    ast.Num
                ):
                    return node.n

                if isinstance(
                    node,
                    ast.BinOp
                ):

                    left = evaluate(
                        node.left
                    )

                    right = evaluate(
                        node.right
                    )

                    operation_function = (
                        allowed_operators.get(
                            type(node.op)
                        )
                    )

                    if operation_function is None:
                        raise ValueError(
                            "Unsupported operator."
                        )

                    return operation_function(
                        left,
                        right
                    )

                if isinstance(
                    node,
                    ast.UnaryOp
                ):

                    operand = evaluate(
                        node.operand
                    )

                    operation_function = (
                        allowed_operators.get(
                            type(node.op)
                        )
                    )

                    if operation_function is None:
                        raise ValueError(
                            "Unsupported operator."
                        )

                    return operation_function(
                        operand
                    )

                raise ValueError(
                    "Invalid mathematical expression."
                )

            result = evaluate(tree)

            return str(result)

        except ZeroDivisionError:
            return "Error: Division by zero."

        except (
            SyntaxError,
            ValueError,
            TypeError
        ) as error:

            return f"Error: {error}"

        except Exception:
            return "Error: Invalid mathematical expression."
