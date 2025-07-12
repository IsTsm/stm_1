a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))

if a > b:
    print(f'{a} больше, чем {b}')
elif a < b:
    print(f'{b} больше, чем {a}')
else:
    print('числа равны')
