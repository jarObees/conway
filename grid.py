import pygame
import numpy as np


class Grid:
    def __init__(self, width, height, cell_size):
        self.columns = width // cell_size
        self.rows = height // cell_size
        self.cell_size = cell_size
        self.cells = np.zeros((self.columns, self.rows), dtype=np.int8)

    def draw(self, window, colors, running):
        for column in range(self.rows):
            for row in range(self.columns):
                if running:
                    color = colors["green"] if self.cells[column][row] else colors["dark_gray"]
                else:
                    color = colors["dark_green"] if self.cells[column][row] else colors["darker_gray"]
                pygame.draw.rect(window, color, (column * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

    def clear(self):
        self.cells = np.zeros_like(self.cells)

    def toggle_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = not self.cells[row][column]