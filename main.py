print(f'Сыграем в крестики-нолики')
count = 0
znak=''
igra = [[' ', 0, 1, 2], [0, '-', '-', '-'], [1, '-', '-', '-'], [2, '-', '-', '-']]
for i in range(len(igra)):
    print(*igra[i])
def krestiki():
    global count
    count += 1
    if count % 2 == 0:
        znak = 'O'
    else:
        znak ='X'
    print(f'\nХодит игрок - {znak}  \nВведите номер строки и столбца через пробел')
    i, j = map(int, input().split())
    if i != round(0, 3) or j != round(0, 3):
        print('Введены неверные координаты, введите корректные данные\n')
        count -= 1
        krestiki()
    elif igra[i+1][j+1] != '-':
        print('Ячейка уже занята, введите корректные координаты\n')
        count -= 1
        krestiki()
    else:
        igra[i+1][j+1] = znak
        for i in range(len(igra)):
            print(*igra[i])
def prov_pob():
    if igra[1][1] == igra[2][2] == igra[3][3] and igra[1][1] != "-":
        return igra[1][1]
    if igra[1][3] == igra[2][2] == igra[3][1] and igra[1][3] != "-":
        return igra[1][3]
    for col in range(1, 4):
        if igra[1][col] == igra[2][col] == igra[3][col] and igra[1][col] != "-":
            return igra[1][col]
    for row in igra:
        if row[1] == row[2] == row[3] and row[1] != "-":
            return row[1]
    return None
for kr in range(9):
    if prov_pob() != None:
        print(f'Победитель {prov_pob()}')
        break
    else:
        krestiki()
else:
    print('Победила дружба')