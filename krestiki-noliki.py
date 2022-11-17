def greet():
    print('------------------')
    print(' Приветствуем Вас ')
    print('      в игре      ')
    print(' крестики-нолики'  )
    print('------------------')
    print(' Формат ввода х, у')
    print('   целые числа    ')
    print('    от 0 до 2     ')
    print(' x - номер строки ')
    print(' y - номер столбца')
    
  

maps = [[' '] * 3 for i in range(3)]

def show_maps():
    print(f"  0 1 2")
    for i in range(3):
        print(f"{i} {maps[i][0]} {maps[i][1]} {maps[i][2]}")

    



def ask():
    while True:
        coord = input("Ваш ход: ").split()
        if len(coord) != 2:
            print('Введите 2 координаты')
            continue
        
        x, y = coord
        if not(x.isdigit()) or not(y.isdigit()):
            print('Используйте числа')
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or 0 > y  or y > 2:
            print('Координата вне игрового поля')
            continue
        
        if maps[x][y] != ' ':
            print('Клетка уже занята')
            
        return x, y
def victory():
    v_coord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
               ((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2))]
    for coord in v_coord:
        symbols = []
        for c in coord:
            symbols.append(maps[c[0]][c[1]])
            if symbols == ['X', 'X', 'X']:
                print('Выиграл крестик')
                return True
            if symbols == ['0', '0', '0']:
                print('Выиграл нолик')
                return True
    return False
greet()
n = 0
while True:
    n += 1
    show_maps()
    if n % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')
    x, y = ask()
    if n % 2 == 1:
        maps[x][y] = 'X'
    else:
        maps[x][y] = '0'
    if victory():
        break
    if n == 9:
        print('Ничья')
        break

        



   