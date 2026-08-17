"""
State and memory register management for the calculator.
"""

from typing import List, Dict, Union

Number = Union[int, float, complex]


class CalculatorMemory:
    """Manages memory slots and calculation history."""

    def __init__(self):
        self._memory_val: float = 0.0
        self._last_answer: float = 0.0
        self._history: List[Dict[str, Union[str, float]]] = []

    def get_ans(self) -> float:
        return self._last_answer

    def set_ans(self, val: Number) -> None:
        self._last_answer = float(val) if isinstance(val, (int, float)) else val

    def get_recall(self) -> float:
        return self._memory_val

    def memory_add(self, val: Number) -> float:
        self._memory_val += float(val)
        return self._memory_val

    def memory_sub(self, val: Number) -> float:
        self._memory_val -= float(val)
        return self._memory_val

    def memory_clear(self) -> None:
        self._memory_val = 0.0

    def record_history(self, expr: str, result: Number) -> None:
        self._history.append({"expression": expr, "result": result})

    def get_history(self) -> List[Dict[str, Union[str, float]]]:
        return self._history.copy()

    def clear_history(self) -> None:
        self._history.clear()