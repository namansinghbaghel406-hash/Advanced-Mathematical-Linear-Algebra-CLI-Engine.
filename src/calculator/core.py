"""
Core Scientific Mathematical Engine.
Integrates arithmetic, trigonometric, hyperbolic, logarithmic, and exponential operations.
"""

import math
import cmath
from typing import Union

Number = Union[int, float, complex]


class ScientificEngine:
    """Production-grade mathematical computation engine."""

    # Universal & Physical Constants
    CONSTANTS = {
        "pi": math.pi,
        "e": math.e,
        "tau": math.tau,
    }

    # ==========================================
    # 1. ARITHMETIC OPERATIONS
    # ==========================================
    @staticmethod
    def add(a: Number, b: Number) -> Number:
        return a + b

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        return a - b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        return a * b

    @staticmethod
    def divide(a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Math Error: Division by zero is undefined.")
        return a / b

    @staticmethod
    def modulo(a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Math Error: Modulo by zero is undefined.")
        return a % b

    @staticmethod
    def floor_divide(a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Math Error: Floor division by zero is undefined.")
        return a // b

    # ==========================================
    # 2. EXPONENTIAL & POWER OPERATIONS
    # ==========================================
    @staticmethod
    def power(base: Number, exponent: Number) -> Number:
        """Calculates base^exponent."""
        try:
            return base ** exponent
        except OverflowError:
            raise OverflowError("Math Error: Power calculation overflowed numerical limit.")

    @staticmethod
    def exp(x: Number) -> float:
        """Calculates e^x."""
        try:
            return math.exp(x)
        except OverflowError:
            raise OverflowError("Math Error: e^x resulted in an overflow.")

    @staticmethod
    def expm1(x: float) -> float:
        """Calculates e^x - 1 with high precision for small x."""
        return math.expm1(x)

    @staticmethod
    def sqrt(x: Number) -> Number:
        """Calculates square root (returns complex if x < 0)."""
        if isinstance(x, (int, float)) and x < 0:
            return cmath.sqrt(x)
        return math.sqrt(x)

    @staticmethod
    def cbrt(x: float) -> float:
        """Calculates cube root of x."""
        return math.cbrt(x) if hasattr(math, "cbrt") else (x ** (1 / 3))

    # ==========================================
    # 3. LOGARITHMIC OPERATIONS
    # ==========================================
    @staticmethod
    def log10(x: float) -> float:
        """Logarithm base 10: log10(x)."""
        if x <= 0:
            raise ValueError("Domain Error: log10(x) is only defined for x > 0.")
        return math.log10(x)

    @staticmethod
    def ln(x: float) -> float:
        """Natural logarithm (base e): ln(x)."""
        if x <= 0:
            raise ValueError("Domain Error: ln(x) is only defined for x > 0.")
        return math.log(x)

    @staticmethod
    def log2(x: float) -> float:
        """Binary logarithm (base 2): log2(x)."""
        if x <= 0:
            raise ValueError("Domain Error: log2(x) is only defined for x > 0.")
        return math.log2(x)

    @staticmethod
    def log_base(x: float, base: float) -> float:
        """Logarithm with custom base: log_base(x, base)."""
        if x <= 0 or base <= 0 or base == 1:
            raise ValueError("Domain Error: Invalid arguments for custom base logarithm.")
        return math.log(x, base)

    # ==========================================
    # 4. TRIGONOMETRIC OPERATIONS (Degrees)
    # ==========================================
    @staticmethod
    def sin(deg: float) -> float:
        val = math.sin(math.radians(deg))
        return 0.0 if math.isclose(val, 0.0, abs_tol=1e-15) else round(val, 10)

    @staticmethod
    def cos(deg: float) -> float:
        val = math.cos(math.radians(deg))
        return 0.0 if math.isclose(val, 0.0, abs_tol=1e-15) else round(val, 10)

    @staticmethod
    def tan(deg: float) -> float:
        if (deg - 90) % 180 == 0:
            raise ValueError(f"Domain Error: Tangent is undefined at {deg}°.")
        return round(math.tan(math.radians(deg)), 10)

    @staticmethod
    def asin(x: float) -> float:
        """Inverse sin (arcsin) returning degrees."""
        if not -1.0 <= x <= 1.0:
            raise ValueError("Domain Error: asin input must be between -1.0 and 1.0.")
        return round(math.degrees(math.asin(x)), 10)

    @staticmethod
    def acos(x: float) -> float:
        """Inverse cos (arccos) returning degrees."""
        if not -1.0 <= x <= 1.0:
            raise ValueError("Domain Error: acos input must be between -1.0 and 1.0.")
        return round(math.degrees(math.acos(x)), 10)

    @staticmethod
    def atan(x: float) -> float:
        """Inverse tan (arctan) returning degrees."""
        return round(math.degrees(math.atan(x)), 10)

    # ==========================================
    # 5. HYPERBOLIC OPERATIONS
    # ==========================================
    @staticmethod
    def sinh(x: float) -> float:
        return math.sinh(x)

    @staticmethod
    def cosh(x: float) -> float:
        return math.cosh(x)

    @staticmethod
    def tanh(x: float) -> float:
        return math.tanh(x)

    @staticmethod
    def asinh(x: float) -> float:
        return math.asinh(x)

    @staticmethod
    def acosh(x: float) -> float:
        if x < 1.0:
            raise ValueError("Domain Error: acosh(x) is only defined for x >= 1.0.")
        return math.acosh(x)

    @staticmethod
    def atanh(x: float) -> float:
        if not -1.0 < x < 1.0:
            raise ValueError("Domain Error: atanh(x) is only defined for -1 < x < 1.")
        return math.atanh(x)

    # ==========================================
    # 6. COMBINATORICS & UTILITY
    # ==========================================
    @staticmethod
    def factorial(n: int) -> int:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Domain Error: Factorial requires a non-negative integer.")
        if n > 170:
            raise OverflowError("Math Error: Factorial input too large.")
        return math.factorial(n)