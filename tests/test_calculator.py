"""
Comprehensive Unit Test Suite for the Scientific Calculator & Matrix Engine.
"""

import pytest
import math
import numpy as np

from src.calculator.core import ScientificEngine
from src.calculator.parser import SafeMathEvaluator
from src.calculator.memory import CalculatorMemory
from src.calculator.matrix_engine import MatrixEngine


# =========================================================================
# 1. Arithmetic & Power Tests
# =========================================================================
def test_arithmetic():
    assert ScientificEngine.add(10, 5) == 15
    assert ScientificEngine.subtract(10, 5) == 5
    assert ScientificEngine.multiply(4, 5) == 20
    assert ScientificEngine.divide(20, 4) == 5.0
    assert ScientificEngine.power(2, 3) == 8


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        ScientificEngine.divide(10, 0)


# =========================================================================
# 2. Trigonometric Tests
# =========================================================================
def test_trigonometry():
    assert ScientificEngine.sin(30) == 0.5
    assert ScientificEngine.cos(60) == 0.5
    assert ScientificEngine.tan(45) == 1.0


# =========================================================================
# 3. Logarithmic & Exponential Tests
# =========================================================================
def test_logarithms():
    assert ScientificEngine.log10(100) == 2.0
    assert math.isclose(ScientificEngine.ln(math.e), 1.0)
    assert ScientificEngine.log2(8) == 3.0


# =========================================================================
# 4. Memory & History Tests
# =========================================================================
def test_memory_operations():
    mem = CalculatorMemory()
    assert mem.get_recall() == 0.0
    mem.memory_add(50)
    assert mem.get_recall() == 50.0
    mem.memory_sub(20)
    assert mem.get_recall() == 30.0
    mem.memory_clear()
    assert mem.get_recall() == 0.0


# =========================================================================
# 5. Expression Parser Tests
# =========================================================================
def test_evaluator_expressions():
    evaluator = SafeMathEvaluator()
    assert evaluator.evaluate("2 + 3 * 4") == 14
    assert evaluator.evaluate("sqrt(16) + 2^3") == 12.0
    assert evaluator.evaluate("sin(30)") == 0.5


# =========================================================================
# 6. NumPy Matrix & Vector Tests
# =========================================================================
def test_matrix_determinant():
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    assert MatrixEngine.determinant(A) == -2.0


def test_matrix_multiplication():
    A = np.array([[1.0, 2.0], [3.0, 4.0]])
    B = np.array([[2.0, 0.0], [1.0, 2.0]])
    expected = np.array([[4.0, 4.0], [10.0, 8.0]])
    np.testing.assert_array_almost_equal(MatrixEngine.multiply(A, B), expected)


def test_solve_linear_system():
    # 2x + y = 8, x - y = 1 => x = 3, y = 2
    A = np.array([[2.0, 1.0], [1.0, -1.0]])
    B = np.array([8.0, 1.0])
    solution = MatrixEngine.solve_linear_system(A, B)
    np.testing.assert_array_almost_equal(solution, np.array([3.0, 2.0]))


def test_vector_stats():
    v = np.array([10.0, 20.0, 30.0])
    stats = MatrixEngine.vector_stats(v)
    assert stats["mean"] == 20.0
    assert stats["sum"] == 60.0