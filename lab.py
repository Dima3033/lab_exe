n1=int(input('Введіть розміри висота - '))
for i in range(n1):
    for j in range(n1):
        if i == 0 or i == n1-1:
            print(f'* ', end=' ')
        else:
            if j == 0 or j == n1 - 1:
                print(f'* ', end=" ")
            else:
                print(f'  ', end=" ")
    print()
