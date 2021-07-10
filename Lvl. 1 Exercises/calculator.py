def calculator(operator, a, b):
    if operator == '+':
        return a + b
    if operator == '-':
        return a - b
    if operator == '*':
        return a * b
    if operator == '/':
        return a / b

a = 9
b = 9
print(calculator('+', a, b))
