from functools import reduce

concatenate = lambda strings: reduce(lambda x, y: x + ' ' + y, strings)

# Example usage:
result = concatenate(['hello', 'bar', 'and','guy'])
print(result) 
