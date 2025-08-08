# Arithmetic Formatter Project - By: David Kachroo

This public repository contains my solution for the **"Build an Arithmetic Formatter"** project from the **freeCodeCamp Scientific Computing with Python** certification.

## Project Overview
The `arithmetic_arranger` function formats a list of arithmetic problems vertically and side-by-side, following specific spacing and alignment rules. It also includes an optional parameter to display the answers.

### Features:
- Arranges up to **5 arithmetic problems** vertically and side-by-side.
- Supports **addition (+)** and **subtraction (-)** only.
- Performs input validation:
  - Returns an error for too many problems.
  - Returns an error for unsupported operators.
  - Ensures all operands contain only digits.
  - Limits operands to a maximum of 4 digits.
- Right-aligns numbers and includes proper spacing.
- Optionally displays the answers when `solve=True`.

### Example Usage:
```python
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
