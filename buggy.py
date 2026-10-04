def calculate_average(numbers):
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]

    average = total / len(numbers)
    return average


def find_max(numbers):
    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


def square_number(number):
    result = number * number
    return result


numbers = [10, 20, 30, 40, 50]

print("Average:", calculate_average(numbers))
print("Maximum:", find_max(numbers))
print("Square:", square_number(5))
