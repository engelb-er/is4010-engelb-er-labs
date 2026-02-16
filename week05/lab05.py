"""
Lab 05 - Refactor Challenge (Part 2)

Refactored with defensive programming and exception handling.
"""

from typing import Any, Dict, List


# Original data
users: List[Dict[str, Any]] = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False},
]


def calculate_average_age(user_records: List[Dict[str, Any]]) -> float:
    """
    Calculate the average age across users with valid integer ages.

    Parameters
    ----------
    user_records : list of dict
        List of user dictionaries.

    Returns
    -------
    float
        The average age of valid integer ages.
        Returns 0.0 if calculation cannot be performed.
    """
    try:
        if not user_records:
            raise ValueError("User list is empty.")

        total_age = 0
        valid_age_count = 0

        for user in user_records:
            age = user.get("age")

            if not isinstance(age, int):
                continue

            total_age += age
            valid_age_count += 1

        if valid_age_count == 0:
            raise ZeroDivisionError("No valid integer ages found.")

        return total_age / valid_age_count

    except ValueError:
        print("Error: cannot calculate average age of an empty list.")
        return 0.0

    except ZeroDivisionError:
        print("Error: no valid integer ages available to calculate average.")
        return 0.0


def get_active_user_emails(user_records: List[Dict[str, Any]]) -> List[str]:
    """
    Get email addresses for active users.

    Parameters
    ----------
    user_records : list of dict
        List of user dictionaries.

    Returns
    -------
    list of str
        Email addresses of active users.
        Returns empty list if error occurs.
    """
    active_emails: List[str] = []

    try:
        if not user_records:
            raise ValueError("User list is empty.")

        for user in user_records:
            try:
                if user["is_active"] and user["email"]:
                    active_emails.append(user["email"])
            except KeyError:
                print("Warning: user record missing 'is_active' or 'email' key. Skipping.")
                continue

        return active_emails

    except ValueError:
        print("Error: cannot retrieve emails from an empty list.")
        return []


if __name__ == "__main__":
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
