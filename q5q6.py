MAX_RESULT_LENGTH = 10
MAX_CODE_LENGTH = 1000
MAX_VARIABLES = 50
MAX_VARIABLE_NAME_LENGTH = 20

def evaluate_expression(expression, variables):
    """
    This function evaluates a simple arithmetic expression with integers
    :param expression: the expression to evaluate
    :param variables: the vars that already exist in case of an expression that involves them.
    :return:
    this function returns the evaluation of the expression
    """
    try:
        result = eval(expression, {}, variables)
        if isinstance(result, int) and len(str(result)) > MAX_RESULT_LENGTH:
            raise ValueError("Overflow Error")
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def is_valid_variable_name(name):
    return name and len(name) <= MAX_VARIABLE_NAME_LENGTH

def interpret(script, variables=None):
    """
    this function receives a script and start to interpret into the variables and expressions.
    :param script: the code that the user enters.
    :return: the function returns the final variables from the script.
    """
    if len(script) > MAX_CODE_LENGTH:
        print("Error: Program code exceeds maximum length")
        return {}

    if variables is None:
        variables = {}

    lines = script.split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '=' in line and 'if' not in line:
            parts = line.split('=', 1)  # Split only once
            var_name = parts[0].strip()
            expression = parts[1].strip()
            if not is_valid_variable_name(var_name):
                print(f"Error: Invalid variable name '{var_name}'")
                return {}
            if len(variables) >= MAX_VARIABLES:
                print("Error: Variable limit exceeded")
                return {}
            variables[var_name] = evaluate_expression(expression, variables)
        elif 'if' in line:
            parts = line.split(':')
            condition = parts[0].strip().replace('if', '').strip()
            true_block = parts[1].strip()
            false_block = parts[2].strip() if len(parts) > 2 else ""
            if evaluate_expression(condition, variables):
                interpret(true_block, variables)
            elif false_block:
                interpret(false_block, variables)
        else:
            print(f"Unknown command: {line}")

    return variables

# Test the interpreter
script = """
a = 10
b = 20
c = a + b
if c > 20: d = c - 10 : d = c * 2
if d == 30: e = 1 : e = 0
"""
variables = interpret(script)
print(variables)
