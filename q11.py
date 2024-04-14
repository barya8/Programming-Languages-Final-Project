cumulative_sum_of_squares_of_even = lambda lists: list(map(lambda sublist: (lambda even_squared: sum(even_squared))(list(map(lambda num: num**2, filter(lambda x: x % 2 == 0, sublist)))), lists))

# Example usage:
input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = cumulative_sum_of_squares_of_even(input_list)
print(result)
