n = int(input('Введите количество элементов: '))
Ai = input("Введите элементы через пробел: ").split()
A = list(map(int, Ai))
if len(A) != n or n == 0:
    print('Введенные элементы не соответствуют заявленному количеству')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = X - A[0]
    index = 0
    for i in range(1, n):
        count = X - A[i]
        if count < min:
            min = count
            index = i
    print(f'Число {A[index]} в списке наиболее близко по величине к числу {X}')
