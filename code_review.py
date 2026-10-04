def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("The list cannot be empty.")

    total = sum(numbers)
    return total / len(numbers)


data = [10, 20, 30, 40, 50]

try:
    result = calculate_average(data)
    print("Result:", result)
except ValueError as error:
    print("Error:", error)
