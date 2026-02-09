# Lab 04 – AI Prompts and Responses

## Problem 1 – Finding common items

**Prompt used**

[I’m working on a Python assignment where I have two very large lists of product IDs from two different suppliers. I need to find which product IDs appear in both lists so I know which products I can source from either supplier. The order of the final result does not matter, and performance is important.
Among the basic Python data structures (list, tuple, dictionary, set), which should I use internally to solve this efficiently, and why? Please also briefly explain how you would implement this in a function that takes two lists and returns a list of common IDs.]

**AI response (summary)**

[The best core data structure for this problem is a set.]

---

## Problem 2 – User profile lookup

**Prompt used**

[I have a Python application that loads a list of user profiles from a database. Each user has a unique username, an age, and an email address. Right now, the data is in a list of dictionaries like:
users = [
    {"name": "alice", "age": 30, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "email": "bob@example.com"},
    # ...
]
I frequently need to look up a user’s full profile by their username, and performance is important.
Among the basic Python data structures (list, tuple, dictionary, set), what is the best structure to use for fast lookups by username, and why? How would you structure the data and implement a function find_user_by_name(users, name) to return the user dict or None?]

**AI response (summary)**

[The best data structure here is a dictionary that maps username → user profile.]

---

## Problem 3 – Listing even numbers in order

**Prompt used**

[I’m writing a Python function that takes a list of integers representing sensor readings. I need to return a new collection that contains only the even readings, and they must be in the exact same order they appeared in the original list.
Among the basic Python data structures (list, tuple, dictionary, set), which is most appropriate for the returned collection and why? Also, what is a clean way to implement this function?]

**AI response (summary)**

[The most appropriate data structure for the output is a list.]
