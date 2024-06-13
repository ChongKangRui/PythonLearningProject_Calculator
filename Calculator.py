
def add(x, y):
    return float(x) + float(y)

def subtract(x, y):
    return float(x) - float(y)

def multiply(x, y):
    return float(x) * float(y)

def divide(x, y):
  return float(x) / float(y)


def has_decimal_digits(number):
    str_number = str(number)
    # Check if there is a decimal point and if there are digits after it
    if '.' in str_number:
        fractional_part = str_number.split('.')[1]  # Split on the decimal point and get the fractional part
        return len(fractional_part) > 0  # Check if the fractional part is non-empty
    return False

def EvaluateExpression(operators, operands):
    while '*' in operators or '/' in operators:
        for i, op in enumerate(operators):
            if op == '*' or op == '/':
                if op == '*':
                    result = multiply(operands[i], operands[i + 1])
                else:
                    result = divide(operands[i], operands[i + 1])
                operands[i] = result
                del operands[i + 1]
                del operators[i]
                break

    while '+' in operators or '-' in operators:
        for i, op in enumerate(operators):
            if op == '+' or op == '-':
                if op == '+':
                    result = add(operands[i], operands[i + 1])
                else:
                    result = subtract(operands[i], operands[i + 1])
                operands[i] = result
                del operands[i + 1]
                del operators[i]
                break

    out_StringNumber = str(operands[0])
    if '.' in out_StringNumber:
        fractional_part = out_StringNumber.split('.')

        if fractional_part[1] == "0":
            return fractional_part[0]

    return out_StringNumber

def IsSymbol(char):
    if char.isdigit():
        OutBool = False
    else:
        OutBool = True

    return OutBool

