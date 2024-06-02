import typing
from grid import Grid
import numpy as np

COLORS = {
    "black" : (0, 0, 0),
    "dark_gray" : (20, 20, 20),
    "green" : (57, 255, 20),
    "dark_green" : (57, 200, 20),
    "darker_gray": (10, 10, 10)
}


class Simulation:
    """
    Attributes:
        grid (Grid obj): Grid object from grid.py used for drawing onto pygame.
        temp_grid (Grid obj): Changes to grid done on the temp_grid first before being copied over to the grid.
        columns (int): Total number of columns in the grids.
        rows (int): Total number of rows in the grids.
        run (bool): Determines whether paused or running for pygame and update() calculations.
    """
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.columns = width // cell_size
        self.rows = height // cell_size
        self.run = False

    def draw(self, window):
        self.grid.draw(window, COLORS, self.run)

    # Applies offset to the particular cell to look into the cells around it and check to see if they're alive.
    def count_live_neighbors(self, grid: 'Grid', row: int, column: int) -> int:
        neighbor_offsets = np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
        # Takes modulus of total rows/columns to essentially make the grid toroidal.
        neighbor_positions = (np.array([row, column]) + neighbor_offsets) % [self.rows, self.columns]
        live_neighbors: int = grid.cells[neighbor_positions[:, 0], neighbor_positions[:, 1]].sum()

        return live_neighbors

    # Updates each cell in the grid as either dead (0) or alive (1) based on Conway's rules.
    def update(self):
        if self.is_running():
            for row in range(self.rows):
                for column in range(self.columns):
                    live_neighbors = self.count_live_neighbors(self.grid, row, column)
                    cell_value = self.grid.cells[row][column]

                    if cell_value == 1:
                        if live_neighbors > 3 or live_neighbors < 2:
                            self.temp_grid.cells[row][column] = 0
                        else:
                            self.temp_grid.cells[row][column] = 1
                    else:
                        if live_neighbors == 3:
                            self.temp_grid.cells[row][column] = 1
                        else:
                            self.temp_grid.cells[row][column] = 0
            np.copyto(self.grid.cells, self.temp_grid.cells)

    def is_running(self):
        return self.run

    def toggle_sim(self):
        self.run = not self.run

    def fill_random(self):
        self.grid.cells = np.random.choice([1, 0, 0, 0, 0, 0], size=self.grid.cells.shape)

    def toggle_cell(self, row: int, column: int):
        if self.is_running() == False:
            self.grid.toggle_cell(row, column)