def count_even_numbers(numbers):
    return [num % 2 == 0 for num in numbers]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = count_even_numbers(numbers)
print(result)
