a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
c = input('Выберите операцию +, -, *, /')

if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '*':
    result = a * b
elif c == '/':
    if b != 0:
        result = a / b
    else:
        result = 'Ошибка: деление на ноль'

else:
    result = 'Ошибка: неизвестная операция'
print(f'{a} {c} {b} = {result}')
