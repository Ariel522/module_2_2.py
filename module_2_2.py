first = int(input('first: '))
second = int(input('second: '))
third = int(input('third: '))
if first == second and first == third:
    print('Все', 3, 'числа равны между собой')
elif first == second or first == third or second == third:
    print(2, 'числа равны между собой')
else:
    print('Обнаружено', int(not(1)), 'равных между собой чисел')
