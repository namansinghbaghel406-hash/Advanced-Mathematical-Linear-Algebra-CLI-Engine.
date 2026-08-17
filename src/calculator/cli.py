"""
Interactive Menu-Driven Scientific Calculator CLI.
Provides numbered sub-menus, clear result boxes, and expression evaluation.
"""

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    from .core import ScientificEngine
    from .memory import CalculatorMemory
    from .parser import SafeMathEvaluator
except ImportError:
    from core import ScientificEngine
    from memory import CalculatorMemory
    from parser import SafeMathEvaluator

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()
memory = CalculatorMemory()
evaluator = SafeMathEvaluator(memory_ref=memory)


def show_result(title: str, expr: str, res: any):
    """Displays calculation results in a clean highlighted box and logs them."""
    memory.record_history(expr, res)
    memory.set_ans(res)
    console.print()
    console.print(
        Panel(
            f"[bold yellow]{expr}[/bold yellow]  =  [bold green]{res}[/bold green]",
            title=f"✓ {title}",
            border_style="green",
            expand=False,
        )
    )
    Prompt.ask("[dim]Press Enter to continue...[/dim]")


def show_main_menu():
    table = Table(title="🔬 SCIENTIFIC CALCULATOR - MAIN MENU", border_style="bright_blue")
    table.add_column("Key", style="bold yellow", width=6, justify="center")
    table.add_column("Category / Mode", style="bold white")
    table.add_column("Description", style="dim")

    table.add_row("1", "Trigonometric Mode", "sin, cos, tan, asin, acos, atan")
    table.add_row("2", "Arithmetic Mode", "Add, Subtract, Multiply, Divide, Modulo, Power")
    table.add_row("3", "Logarithmic & Exponential", "log10, ln, log2, e^x, sqrt, cbrt")
    table.add_row("4", "Direct Expression Evaluator", "Type complete math formulas directly")
    table.add_row("5", "Memory & History", "View past logs, memory recall, clear memory")
    table.add_row("0", "Exit", "Close the calculator")

    console.print(table)


# =========================================================================
# 1. TRIGONOMETRIC SUB-MENU
# =========================================================================
def handle_trigonometry():
    while True:
        table = Table(title="📐 TRIGONOMETRIC OPERATIONS (Angles in Degrees)", border_style="cyan")
        table.add_column("Key", style="bold yellow", width=6, justify="center")
        table.add_column("Function", style="white")

        table.add_row("1", "sin(θ)")
        table.add_row("2", "cos(θ)")
        table.add_row("3", "tan(θ)")
        table.add_row("4", "asin(x)  [Inverse Sin]")
        table.add_row("5", "acos(x)  [Inverse Cos]")
        table.add_row("6", "atan(x)  [Inverse Tan]")
        table.add_row("0", "⬅ Back to Main Menu")

        console.print(table)
        choice = Prompt.ask("[bold green]Select Option[/bold green]").strip()

        if choice == "0":
            break

        try:
            if choice in ("1", "2", "3"):
                angle = float(Prompt.ask("Enter angle in degrees (θ)"))
                if choice == "1":
                    res = ScientificEngine.sin(angle)
                    show_result("Sine", f"sin({angle}°)", res)
                elif choice == "2":
                    res = ScientificEngine.cos(angle)
                    show_result("Cosine", f"cos({angle}°)", res)
                elif choice == "3":
                    res = ScientificEngine.tan(angle)
                    show_result("Tangent", f"tan({angle}°)", res)

            elif choice in ("4", "5", "6"):
                val = float(Prompt.ask("Enter value (x)"))
                if choice == "4":
                    res = ScientificEngine.asin(val)
                    show_result("ArcSine", f"asin({val})", f"{res}°")
                elif choice == "5":
                    res = ScientificEngine.acos(val)
                    show_result("ArcCosine", f"acos({val})", f"{res}°")
                elif choice == "6":
                    res = ScientificEngine.atan(val)
                    show_result("ArcTangent", f"atan({val})", f"{res}°")
            else:
                console.print("[bold red]Invalid option. Please choose 0-6.[/bold red]")

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")


# =========================================================================
# 2. ARITHMETIC SUB-MENU
# =========================================================================
def handle_arithmetic():
    while True:
        table = Table(title="➕ ARITHMETIC OPERATIONS", border_style="magenta")
        table.add_column("Key", style="bold yellow", width=6, justify="center")
        table.add_column("Operation", style="white")

        table.add_row("1", "Addition (a + b)")
        table.add_row("2", "Subtraction (a - b)")
        table.add_row("3", "Multiplication (a * b)")
        table.add_row("4", "Division (a / b)")
        table.add_row("5", "Power (base ^ exp)")
        table.add_row("6", "Modulo (a % b)")
        table.add_row("0", "⬅ Back to Main Menu")

        console.print(table)
        choice = Prompt.ask("[bold green]Select Option[/bold green]").strip()

        if choice == "0":
            break

        try:
            if choice in ("1", "2", "3", "4", "5", "6"):
                a = float(Prompt.ask("Enter first number (a)"))
                b = float(Prompt.ask("Enter second number (b)"))

                if choice == "1":
                    res = ScientificEngine.add(a, b)
                    show_result("Addition", f"{a} + {b}", res)
                elif choice == "2":
                    res = ScientificEngine.subtract(a, b)
                    show_result("Subtraction", f"{a} - {b}", res)
                elif choice == "3":
                    res = ScientificEngine.multiply(a, b)
                    show_result("Multiplication", f"{a} * {b}", res)
                elif choice == "4":
                    res = ScientificEngine.divide(a, b)
                    show_result("Division", f"{a} / {b}", res)
                elif choice == "5":
                    res = ScientificEngine.power(a, b)
                    show_result("Power", f"{a} ^ {b}", res)
                elif choice == "6":
                    res = ScientificEngine.modulo(a, b)
                    show_result("Modulo", f"{a} % {b}", res)
            else:
                console.print("[bold red]Invalid option. Please choose 0-6.[/bold red]")

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")


# =========================================================================
# 3. LOGARITHMIC & EXPONENTIAL SUB-MENU
# =========================================================================
def handle_log_exp():
    while True:
        table = Table(title="📈 LOGARITHMIC & EXPONENTIAL OPERATIONS", border_style="yellow")
        table.add_column("Key", style="bold yellow", width=6, justify="center")
        table.add_column("Function", style="white")

        table.add_row("1", "log10(x)  [Base-10]")
        table.add_row("2", "ln(x)     [Natural Log]")
        table.add_row("3", "log2(x)   [Binary Log]")
        table.add_row("4", "e^x       [Exponential]")
        table.add_row("5", "sqrt(x)   [Square Root]")
        table.add_row("6", "cbrt(x)   [Cube Root]")
        table.add_row("0", "⬅ Back to Main Menu")

        console.print(table)
        choice = Prompt.ask("[bold green]Select Option[/bold green]").strip()

        if choice == "0":
            break

        try:
            val = float(Prompt.ask("Enter value (x)"))
            if choice == "1":
                res = ScientificEngine.log10(val)
                show_result("Logarithm Base-10", f"log10({val})", res)
            elif choice == "2":
                res = ScientificEngine.ln(val)
                show_result("Natural Logarithm", f"ln({val})", res)
            elif choice == "3":
                res = ScientificEngine.log2(val)
                show_result("Binary Logarithm", f"log2({val})", res)
            elif choice == "4":
                res = ScientificEngine.exp(val)
                show_result("Exponential", f"e^{val}", res)
            elif choice == "5":
                res = ScientificEngine.sqrt(val)
                show_result("Square Root", f"sqrt({val})", res)
            elif choice == "6":
                res = ScientificEngine.cbrt(val)
                show_result("Cube Root", f"cbrt({val})", res)
            else:
                console.print("[bold red]Invalid option.[/bold red]")

        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")


# =========================================================================
# 4. DIRECT EXPRESSION MODE
# =========================================================================
def handle_direct_expression():
    console.print(Panel("Type math expressions directly (e.g. 'sin(30) + 2^4', 'x = 10'). Type '0' or 'back' to return.", border_style="blue"))
    while True:
        expr = Prompt.ask("[bold green]expr[/bold green]").strip()
        if expr.lower() in ("back", "0", "exit"):
            break
        if not expr:
            continue
        try:
            res = evaluator.evaluate(expr)
            if isinstance(res, (int, float, complex)):
                show_result("Expression Result", expr, res)
            else:
                console.print(f"[green]{res}[/green]")
        except Exception as e:
            console.print(f"[bold red]Error:[/bold red] {e}")


# =========================================================================
# 5. MEMORY & HISTORY
# =========================================================================
def handle_memory_history():
    hist = memory.get_history()
    if not hist:
        console.print("[yellow]No history available.[/yellow]")
    else:
        table = Table(title="Calculation History (Last 10)", border_style="green")
        table.add_column("#", style="dim", width=4)
        table.add_column("Expression", style="cyan")
        table.add_column("Result", style="bold white")
        for idx, item in enumerate(hist[-10:], 1):
            table.add_row(str(idx), str(item["expression"]), str(item["result"]))
        console.print(table)
    console.print(f"[bold magenta]Last Answer (Ans):[/bold magenta] {memory.get_ans()}")
    console.print(f"[bold magenta]Memory Slot (MR):[/bold magenta] {memory.get_recall()}")
    Prompt.ask("\n[dim]Press Enter to continue...[/dim]")


# =========================================================================
# MAIN APP LOOP
# =========================================================================
def run_cli():
    while True:
        show_main_menu()
        choice = Prompt.ask("\n[bold green]Enter Choice (0-5)[/bold green]").strip()

        if choice == "1":
            handle_trigonometry()
        elif choice == "2":
            handle_arithmetic()
        elif choice == "3":
            handle_log_exp()
        elif choice == "4":
            handle_direct_expression()
        elif choice == "5":
            handle_memory_history()
        elif choice in ("0", "exit", "quit", "q"):
            console.print("[bold red]Session closed. Goodbye![/bold red]")
            sys.exit(0)
        else:
            console.print("[bold red]Invalid option. Please enter 0, 1, 2, 3, 4, or 5.[/bold red]")


if __name__ == "__main__":
    run_cli()