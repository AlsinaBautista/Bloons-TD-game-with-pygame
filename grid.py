import constantes as c
class Grid:
    def __init__(self, grid_width=c.GRID_WIDTH,grid_height=c.GRID_HEIGHT):
        self.height = grid_height   
        self.width = grid_width 
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
    
    def initialize_grid(self):
        for i in range(len(c.ENEMY_PATH) - 1):
            x1, y1 = c.ENEMY_PATH[i]
            x2, y2 = c.ENEMY_PATH[i + 1]
            col1, row1 = x1 // c.CELD, y1 // c.CELD
            col2, row2 = x2 // c.CELD, y2 // c.CELD

            if row1 == row2:
                for col in range(min(col1, col2), max(col1, col2) + 1):
                    self.grid[row1][col] = 1
            elif col1 == col2:
                for row in range(min(row1, row2), max(row1, row2) + 1):
                    self.grid[row][col1] = 1
        for cell in c.OCCUPIED_CELLS:
            x, y = cell[0]
            value = cell[1]
            self.set_value(x, y, value)

    def set_value(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value

    def get_value(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])
    
    def __getitem__(self, index):
        return self.grid[index]

def start_grid():
    
    grid= Grid()
    grid.initialize_grid()

    return grid
def draw_grid(grid):
    for row in grid.grid:
        for value in row:
            if value == 1:
                print('X', end=' ')
            elif value == 2:
                    print('N', end=' ')
            else:
                    print('O', end=' ')
        print()