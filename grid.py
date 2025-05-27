import constantes as c
class Grid:
    def __init__(self, width=c.GRID_WIDTH, height=c.GRID_HEIGHT):
        
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
    
    def initialize_grid(self):
        for i in range(len(c.ENEMY_PATH) - 1):
            x1, y1 = c.ENEMY_PATH[i]
            x2, y2 = c.ENEMY_PATH[i + 1]
            col1, row1 = x1 // c.CELD, y1 // c.CELD
            col2, row2 = x2 // c.CELD, y2 // c.CELD
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        if row1 == row2:
            for col in range(min(col1, col2), max(col1, col2) + 1):
                self.grid[row1][col] = 1
        elif col1 == col2:
            for row in range(min(row1, row2), max(row1, row2) + 1):
                self.grid[row][col1] = 1

    def set_value(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value

    def get_value(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])

grid= Grid(c.GRID_WIDTH, c.GRID_HEIGHT)
grid.initialize_grid()
grid.__str__()