def read_sudoku(filename):
    f = open(filename,'r')
    data = f.read().replace('.','0').replace('\n','')
    f.close()
    grid = []
    temp = []
    for i in range(9**2):
        if i%9 == 0 and i >0:
            grid.append(temp)
            temp =[]
        temp.append(int(data[i]))
    grid.append(temp)
    return grid

def print_sudoku(grid):
    for i in range(9): #СТРОКИ
        if i%3 == 0:
            print('------+-------+-------')
        for j in range(9): #СТОЛБЦЫ
            print(grid[i][j], end=' ')
            if j % 3 == 2 and j != 8:
                print('|',end =' ')
        print()#перенос строки


def check(grid,row,col,num):
    #проверяем - есть ли цифра num в строке с номером row
    for x in range(9):
        if grid[row][x] == num:
            return False #нашли такую цифру - так нельзя
    #проверяем - есть ли цифра num в столбце с номером col
    for y in range(9):
        if grid[col][y] == num:
            return False #нашли такую цифру - так нельзя
    #проверка внутри квадрата
    start_col = col - col % 3 #координата верхнего левого угла квадрата
    start_row = row - row % 3
    for i in range(3): #строки
        for j in range(3):#Столбцы
            if grid[start_row+i][start_col+j] == num:
                return False
    return True #если мы не нашли такую цифру в нашей карте - можно ее ставить. Это хороший ход


def solve_sudoku(grid, row,col): #указываем частично решенную таблицу и координаты относительно которых мы продолжаем решать судоку
    #если координаты - крайний нижний угол таблицы - рекурсия останавливается, все решено
    if row == 8 and col == 8:
        return True
    if grid[row][col] >0: #если клетка запонлена - перепрыгиваем на следующий столбец
        return solve_sudoku(grid,row, col+1)
    if col == 9: #проверили всю строку, переходим на следующие
        row += 1
        col = 0
    #прорверяем можем ли мы вставить в данной строке/Столце/квадрате число от 1 до 9

grid = read_sudoku('sudoku1.txt')
print_sudoku(grid)