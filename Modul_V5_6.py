# отрисовка поля
def show(field, count_step=0):

    print('  | 0 | 1 | 2 |')
    print('-' * 15)
    for i in range(3):
        row = ' | '.join(field[i])
        s = f'{i} | {row} |'
        print(s)
        print('-' * 15)


# проверяем на выйгрыш
def end(field):

    def win(s):
        return s == 'XXX' or s == 'OOO'

    # проверяем строки
    def check_win_line():
        rez = False
        for i in range(3):
            s = ''.join(field[i])
            if win(s):
                rez = True
                break
        return rez

    #     проверяем столбцы
    def check_win_row():
        rez = False
        for j in range(3):
            s = ''
            for i in range(3):
                s += field[i][j]
            if win(s):
                rez = True
                break
        return rez

    # проверяем диагональ
    def check_win_diag():
        s = ''
        for i in range(3):
            s += field[i][i]
        if win(s):
            return True

        s = ''
        for i in range(3):
            s += field[i][2 - i]
        if win(s):
            return True
        return False

    #   Тут можно было сделать через or, но тогда бы он проверял все три условия
    #     даже если первая проверка прошла успешно
    if check_win_line():
        return True
    elif check_win_row():
        return True
    elif check_win_diag():
        return True
    return False


# Ввод координат
def input_koord(field, symbol):
    while True:
        print('Сейчас играет', symbol)
        rezult = input('Введите номер строки и столбца через пробел: ').split()
        if len(rezult) != 2 or not (rezult[0].isdigit() and rezult[1].isdigit()):
            print('Необходимо ввести две цифры, попробуйте еще раз')
            continue
        line, row = map(int, rezult)
        if not (0 <= line <= 2) or not (0 <= row <= 2):
            print('Необходимо ввести цифры от 0 до 2-х, попробуйте еще раз')
            continue
        if field[line][row] != '-':
            print('В этой клетке уже есть символ')
            continue
        break

    return line, row


def games():
    field = [['-'] * 3 for _ in range(3)]
    show(field)
    counter_step = 1
    while True:
        symbol = 'X' if counter_step % 2 != 0 else 'O'
        line, row = input_koord(field, symbol)
        field[line][row] = symbol
        show(field)
        a = len(set(field[0]))
        if counter_step == 9:
            print('Ничья')
            break
        if end(field):
            print('*' * 24)
            print(f'Выйграл {symbol}')
            break
        counter_step += 1


def start():
    print('*' * 24)
    print('Добро пожаловать!')
    print('Это игра Крестики-нолики')
    print('*' * 24)
    print()


start()
st = True
while st:
    games()
    print()
    st = input("Хотите сыграть еще? '+' - Да, '-' - Нет ") == '+'
