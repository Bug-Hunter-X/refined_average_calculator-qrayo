def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    if total == 0:
        return 0 #Handle case where sum of elements is 0
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [10,0,20]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of list with zero is: {average_zero}")

my_list_all_zeros = [0,0,0]
average_all_zeros = calculate_average(my_list_all_zeros)
print(f"The average of list with all zeros is: {average_all_zeros}"