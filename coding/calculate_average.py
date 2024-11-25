# filename: calculate_average.py

def calculate_average(numbers):
    """
    Calculate the average of a list of integers.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The average of the integers, or 0 if the list is empty.
    """
    # Check if the input list is empty
    if not numbers:
        return 0

    # Calculate the sum of the integers in the list
    total = sum(numbers)

    # Calculate the average by dividing the sum by the count of numbers
    average = total / len(numbers)

    return average


# Test cases
numbers1 = [1, 2, 3, 4, 5]
print(calculate_average(numbers1))  # Expected output: 3.0

numbers2 = []
print(calculate_average(numbers2))  # Expected output: 0

numbers3 = [10]
print(calculate_average(numbers3))  # Expected output: 10.0