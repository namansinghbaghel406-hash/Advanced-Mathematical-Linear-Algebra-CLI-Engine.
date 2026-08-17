# 🔬 Advanced Scientific & Matrix Calculator CLI

A modular, production-grade command-line scientific calculator built in Python with a rich interactive terminal interface, AST-based expression evaluation, session memory, and a NumPy-powered linear algebra engine.

---

## ✨ Features

* **Interactive Rich Terminal UI**: Styled menus, colored status banners, and dedicated result panels powered by `rich`.
* **NumPy Linear Algebra Suite**:
  * Matrix multiplication ($A \times B$)
  * Determinants ($\det(A)$) & Inverses ($A^{-1}$)
  * Transpose ($A^T$)
  * Eigenvalues & Eigenvectors
  * Solving linear systems ($Ax = B$)
  * Vector statistics (mean, std, variance, norm)
* **Trigonometric Suite**: Sine, Cosine, Tangent, and Arc-trigonometric functions (degree-based).
* **Arithmetic & Power Operations**: Standard operations, modulo, cube root, and power support.
* **Logarithmic & Exponential Suite**: Base-10 ($\log_{10}$), natural log ($\ln$), binary log ($\log_2$), and exponential ($e^x$).
* **Safe AST Expression Parser**: Evaluates mathematical strings and custom variables safely without using `eval()`.
* **Session Memory & History**: Memory registers (`M+`, `M-`, `MR`, `MC`) with calculation logging.
* **Automated Unit Tests**: 10+ comprehensive unit tests built with `pytest`.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<YOUR-USERNAME>/scientific-calculator.git
   cd scientific-calculator