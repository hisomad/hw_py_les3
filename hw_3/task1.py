n = int(input('Введите количество элементов: '))
elements = input('Введите элементы через пробел: ').split()
a_num = list(map(int, elements))
if len(a_num) != n:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    x = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(n):
        if a_num[i] == x:
            count += 1
    print(f'Число {x} встречается в списке {count} раз')
