
# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**

> **Context:** I am working on a Python function that is supposed to calculate the sum of all **even** numbers in a list. However, it is currently giving the wrong result, and I think there is a logical error in the condition inside the loop. Here is the code:
> ```python
> def sum_of_evens(numbers):
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```
> **Persona:** You are a senior Python developer helping a beginner debug their code.  
> **Task:** Identify and fix the bug so the function correctly returns the sum of all **even** numbers.  
> **Format:** Give a short explanation, then provide corrected code in a Python code block.

**AI’s Corrected Code:**

```python
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Correct condition
            total += num
    return total
```

**What I learned:**  
The bug was in the condition `num % 2 == 1`, which actually checks for odd numbers. Changing it to `num % 2 == 0` fixed the logic so the function correctly adds even values.


---

## Problem 2: Refactoring

**My Prompt:**

> **Context:** I am working on a Python function that returns the names of users who are 18 or older. The function works, but it is not Pythonic because it uses manual indexing. Here is the code:
> ```python
> def get_names_of_adults(users):
>     results = []
>     for i in range(len(users)):
>         if users[i]['age'] >= 18:
>             results.append(users[i]['name'])
>     return results
> ```
> **Persona:** You are a senior Python developer who writes clean, readable, and idiomatic Python code.  
> **Task:** Refactor the function to be more Pythonic by removing manual indexing and simplifying the logic.  
> **Format:** A brief explanation followed by the refactored code in a Python code block.

**AI’s Corrected Code:**

```python
def get_names_of_adults(users):
    return [user["name"] for user in users if user["age"] >= 18]
```

**What I learned:**  
The original code used index-based looping, which is not Pythonic. The AI replaced it with a list comprehension that directly iterates through user dictionaries, making the code simpler and easier to read.


---

## Problem 3: Documenting

**My Prompt:**

> **Context:** I have a function that calculates the area of a rectangle but has no documentation. It raises a ValueError when given invalid inputs. Here is the code:
> ```python
> def calculate_area(length, width):
>     if length <= 0 or width <= 0:
>         raise ValueError("Length and width must be positive numbers.")
>     return length * width
> ```
> **Persona:** You are a senior Python developer who writes professional NumPy-style docstrings.  
> **Task:** Write a complete NumPy-style docstring describing the function, its parameters, return value, and exceptions.  
> **Format:** Provide the full function definition including the docstring in a Python code block.

**AI’s Corrected Code:**

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be positive.
    width : float or int
        The width of the rectangle. Must be positive.

    Returns
    -------
    float
        The area of the rectangle, computed as ``length * width``.

    Raises
    ------
    ValueError
        If either ``length`` or ``width`` is less than or equal to zero.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:**  
AI can quickly generate accurate NumPy-style docstrings that describe parameters, return values, and exceptions. This helped reinforce how to structure professional documentation.
```

---
