def evaluate_expression(expression, variables):
    """
    This function evaluates a simple arithmetic expression with integers
    :param expression: the expression to evaluate
    :param variables: the vars that already exist in case of an expression that involves them.
    :return:
    this function returns the evaluation of the expression
    """
    # Evaluate a simple arithmetic expression with integers
    try:
        return eval(expression, {}, variables)
    except Exception as e:
        print(f"Error evaluating expression: {expression}")
        print(e)
        return None

def interpret(script):
    """
    this function receives a script and start to interpret into the variables and expressions.
    :param script: the code that the user enters.
    :return: the function returns the final variables from the script.
    """
    variables = {}
    lines = script.split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '=' in line:
            parts = line.split('=', 1)  # Split only once
            var_name = parts[0].strip()
            expression = parts[1].strip()
            variables[var_name] = evaluate_expression(expression, variables)
        elif 'if' in line:
            condition, true_block, false_block = line.split(':')
            condition = condition.strip().replace('if', '').strip()
            true_block = true_block.strip()
            false_block = false_block.strip()
            if evaluate_expression(condition, variables):
                interpret(true_block)
            else:
                interpret(false_block)
        else:
            print(f"Unknown command: {line}")

    return variables

def user_ui():
    """
    this function prints to the console the variables for the convenience of the user.
    """
    for key in variables:
        if ':' not in key:
            print(key, '=', variables[key])
        else:
            newkey = key.split(':')[1].strip()
            print(newkey, '=', variables[key])

# test script
script = """
a = 10
b = 20
c = a * b
if c>1: a=a+b
"""
variables = interpret(script)
user_ui()

