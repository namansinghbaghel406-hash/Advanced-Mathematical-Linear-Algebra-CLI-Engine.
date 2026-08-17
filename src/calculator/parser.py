"""
AST-based expression parser mapping mathematical operations.
"""

import ast
import operator
from typing import Dict, Any, Union
from .core import ScientificEngine

Number = Union[int, float, complex]


class SafeMathEvaluator:
    """Safely evaluates user input expressions without security risks."""

    _BINARY_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
    }

    _UNARY_OPS = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def __init__(self, memory_ref=None):
        self.memory = memory_ref
        self.variables: Dict[str, Any] = dict(ScientificEngine.CONSTANTS)

        # Complete mapped function registry
        self.functions = {
            # Arithmetic & Power
            "sqrt": ScientificEngine.sqrt,
            "cbrt": ScientificEngine.cbrt,
            "exp": ScientificEngine.exp,
            "pow": ScientificEngine.power,
            "abs": abs,
            "round": round,
            "fact": ScientificEngine.factorial,

            # Logarithms
            "log": ScientificEngine.log10,      # Default log is base-10
            "log10": ScientificEngine.log10,
            "ln": ScientificEngine.ln,          # Natural logarithm
            "log2": ScientificEngine.log2,
            "logb": ScientificEngine.log_base,  # Custom base: logb(x, base)

            # Trigonometric
            "sin": ScientificEngine.sin,
            "cos": ScientificEngine.cos,
            "tan": ScientificEngine.tan,
            "asin": ScientificEngine.asin,
            "acos": ScientificEngine.acos,
            "atan": ScientificEngine.atan,

            # Hyperbolic
            "sinh": ScientificEngine.sinh,
            "cosh": ScientificEngine.cosh,
            "tanh": ScientificEngine.tanh,
            "asinh": ScientificEngine.asinh,
            "acosh": ScientificEngine.acosh,
            "atanh": ScientificEngine.atanh,
        }

    def evaluate(self, expression: str) -> Any:
        sanitized = expression.strip().replace("^", "**")

        # Variable assignments (e.g. x = 25)
        if "=" in sanitized and not any(op in sanitized for op in ("==", "<=", ">=")):
            var_name, expr = sanitized.split("=", 1)
            var_name = var_name.strip()
            if not var_name.isidentifier():
                raise ValueError(f"Invalid variable name: '{var_name}'")
            val = self._evaluate_ast(ast.parse(expr.strip(), mode="eval").body)
            self.variables[var_name] = val
            return f"Variable '{var_name}' = {val}"

        tree = ast.parse(sanitized, mode="eval")
        return self._evaluate_ast(tree.body)

    def _evaluate_ast(self, node: ast.AST) -> Any:
        if isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.Name):
            name = node.id
            if name in self.variables:
                return self.variables[name]
            if name == "ans" and self.memory:
                return self.memory.get_ans()
            if name == "mr" and self.memory:
                return self.memory.get_recall()
            raise ValueError(f"Unknown identifier: '{name}'")

        elif isinstance(node, ast.BinOp):
            left = self._evaluate_ast(node.left)
            right = self._evaluate_ast(node.right)
            op = self._BINARY_OPS.get(type(node.op))
            if not op:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op(left, right)

        elif isinstance(node, ast.UnaryOp):
            operand = self._evaluate_ast(node.operand)
            op = self._UNARY_OPS.get(type(node.op))
            if not op:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            return op(operand)

        elif isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Dynamic function calls are disabled.")
            func_name = node.func.id
            if func_name not in self.functions:
                raise ValueError(f"Unknown function: '{func_name}()'")
            args = [self._evaluate_ast(arg) for arg in node.args]
            return self.functions[func_name](*args)

        raise ValueError(f"Disallowed expression node: {type(node).__name__}")