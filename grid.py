import constantes as c
from tower import * 
class Grid:
    def __init__(self, grid_width=c.GRID_WIDTH,grid_height=c.GRID_HEIGHT):
        self.height = grid_height   
        self.width = grid_width 
        self.grid = [[0 for _ in range(self.width +1)] for _ in range(self.height)] #grilla de 0
    
    def initialize_grid(self):
        """
        Initialize the grid with paths and occupied cells.
        Sets the grid values based on the enemy path and occupied cells.
        It marks the path cells with 1, occupied cells with their respective values,
        and leaves the rest as 0.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        for i in range(len(c.ENEMY_PATH) - 1):
            x1, y1 = c.ENEMY_PATH[i]
            x2, y2 = c.ENEMY_PATH[i + 1] #obtiene los x, y del camino de los globos (son pixeles)
            col1, row1 = x1 // c.CELD, y1 // c.CELD
            col2, row2 = x2 // c.CELD, y2 // c.CELD 
            #al usar division entera por el tamano en pixeles de cada casilla me da a que casilla pertenece cada pixel

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
        """
        Set the value of a cell in the grid.
        Updates the grid at the specified coordinates with the given value.
        -------------------------------------------------------------------------
        Arguments:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            value (int): The value to set in the cell.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        if 0 <= x < self.width + 1 and 0 <= y < self.height:
            self.grid[y][x] = value
    
    def get_celd(self, pos):
        #pasa de pixeles a celdas
        """
        Get the cell coordinates based on pixel position.
        Converts pixel coordinates to grid cell coordinates.
        -------------------------------------------------------------------------
        Arguments:
            pos (tuple): The pixel position (x, y).
        -------------------------------------------------------------------------
        Returns:
            tuple: The grid cell coordinates (x, y).
        """
        x, y = pos[0] // c.CELD, pos[1] // c.CELD
        return x, y

    def update_grid(self, tower):
        """
        Update the grid based on the tower's position.
        Checks the type of tower and updates the grid accordingly.
        -------------------------------------------------------------------------
        Arguments:
            tower (Tower): The tower object to update the grid for.
        -------------------------------------------------------------------------
        Returns:
            None
        """
        if isinstance(tower, Cannon): #es como un type, pero para objetos, veo si es de clase Basic
            a, b = tower.pos
            x, y = self.get_celd((a, b))
            self.set_value(x, y, 3)
        elif isinstance(tower, Sniper):
            a, b = tower.pos
            x, y = self.get_celd((a, b))
            self.set_value(x, y, 4)
        elif isinstance(tower, Basic):
            a, b = tower.pos
            x, y = self.get_celd((a, b))
            self.set_value(x, y, 5)
        elif isinstance(tower, Ship):
            a, b = tower.pos
            x, y = self.get_celd((a, b))
            self.set_value(x, y, 6) #estos numeros van a servir para las mejoras
        
    def get_value(self, x, y):
        """
        Get the value of a cell in the grid.
        -------------------------------------------------------------------------
        Arguments:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
        -------------------------------------------------------------------------
        Returns:
            int: The value of the cell, or None if out of bounds.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None

    def __str__(self):
        """
        String representation of the grid.
        Formats the grid into a string for easy visualization.
        -------------------------------------------------------------------------
        Returns:
            str: A string representation of the grid.
        """
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])
    
    def __getitem__(self, index):
        """
        Get the row at the specified index.
        Allows access to the grid rows using indexing.
        -------------------------------------------------------------------------
        Arguments:
            index (int): The index of the row to retrieve.
        -------------------------------------------------------------------------
        Returns:
            list: The row at the specified index.
        """
        return self.grid[index]

def start_grid():
    """
    Initialize the grid.
    Creates a new Grid instance and initializes it with paths and occupied cells.
    -------------------------------------------------------------------------
    Returns:
        Grid: An initialized Grid object.
    """
    grid= Grid()
    grid.initialize_grid()
    return grid

def draw_grid(grid):
    """
    Draw the grid to the console.
    Prints the grid to the console, using 'X' for path cells,
    'N' for occupied cells, and 'O' for empty cells.
    -------------------------------------------------------------------------
    Arguments:
        grid (Grid): The Grid object to draw.
    -------------------------------------------------------------------------
    Returns:
        None
    """
    for row in grid.grid:
        for value in row:
            if value == 1:
                print('X', end=' ')
            elif value == 2:
                    print('N', end=' ')
            else:
                    print('O', end=' ')
        print()
