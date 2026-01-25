# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**

> Context: I am working on a Python function that is supposed to calculate the sum of all **even** numbers in a list. However, it is currently giving the wrong result, and I think there is a logical error in the condition inside the loop. Here is the code:
> ```python
> def sum_of_evens(numbers):
>     """Calculate the sum of all even numbers in a list.
>
>     Parameters
>     ----------
>     numbers : list of int
>         A list of integers.
>
>     Returns
>     -------
>     int
>         The sum of all even numbers in the list.
>     """
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```
> Persona: You are a senior Python developer helping a beginner debug their code.
> Task: Identify and fix the bug in this function so that it correctly returns the sum of all **even** numbers in the list. Briefly explain what was wrong and why your fix works.
> Format: First give a short explanation (2–3 sentences), then provide the corrected version of the function in a Python code block.

**AI's Corrected Code:**

```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Check for even numbers
            total += num
    return total

What I Learned:
The bug was in the condition num % 2 == 1, which actually checks for odd numbers instead of even ones. Changing it to num % 2 == 0 made the function behave as intended. This showed me how an AI can quickly spot simple logical mistakes and confirm my understanding of modulo conditions.




What I Learned:
The bug was in the condition num % 2 == 1, which actually checks for odd numbers instead of even ones. Changing it to num % 2 == 0 made the function behave as intended. This showed me how an AI can quickly spot simple logical mistakes and confirm my understanding of modulo conditions.



def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
Persona: You are a senior Python developer who writes clean, idiomatic Python.
Task: Refactor this function to be more Pythonic, clear, and concise. Use better iteration patterns (no manual indexing) and consider using a list comprehension if appropriate. Keep the same behavior and docstring.
Format: Briefly explain your changes, then provide the refactored function in a Python code block.

def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    return [user["name"] for user in users if user["age"] >= 18]
What I Learned:
The original function used index-based looping (for i in range(len(users))), which is harder to read and not idiomatic in Python. The refactored version uses a list comprehension and iterates directly over each user dictionary, which is shorter and clearer. This helped me see how AI can suggest more Pythonic patterns that I might not automatically think of.



My Prompt:
Context: I have a Python function that calculates the area of a rectangle but it has no documentation. It raises a ValueError if either dimension is non-positive. Here is the code:
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
Persona: You are a senior Python developer who follows NumPy-style documentation conventions.
Task: Write a professional NumPy-style docstring for this function. The docstring should clearly describe the purpose of the function, its parameters (including types), the return value, and the ValueError that is raised for invalid inputs.
Format: Respond with only the complete function definition including the new NumPy-style docstring, in a Python code block.

def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    width : float or int
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float
        The area of the rectangle, calculated as ``length * width``.

    Raises
    ------
    ValueError
        If either ``length`` or ``width`` is less than or equal to zero.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

What I Learned:
The AI was able to generate a clear NumPy-style docstring that includes parameters, return type, and raised exceptions. This showed me how helpful AI can be for writing consistent documentation, especially when I already know what the function does but don’t remember the exact formatting conventions.
