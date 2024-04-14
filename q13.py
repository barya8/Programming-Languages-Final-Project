from functools import reduce

num_palindromes_in_sublists = lambda list_of_lists: list(map(lambda sublist: reduce(lambda count, string: count + 1 if string == string[::-1] else count, sublist, 0), list_of_lists))

# Example usage:
input_list = [['aba', 'bar', 'level'], ['hello', 'noon', 'world'], ['racecar', 'madam', 'guy']]
result = num_palindromes_in_sublists(input_list)
print(result) 
