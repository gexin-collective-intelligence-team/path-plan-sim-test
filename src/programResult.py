import pygame
import sys


class programResult:

    def __init__(self, rows, cols, cell_size, start_point, end_point, obstacle_map):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.padding = 20
        self.background_color = (255, 255, 255)

        self.grid_width = cols * cell_size
        self.grid_height = rows * cell_size
        self.width = self.grid_width + (2 * self.padding)
        self.height = self.grid_height + (2 * self.padding)

        self.start_point = start_point
        self.end_point = end_point
        self.obstacle_map = obstacle_map

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.background_color)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.draw_grid()
            self.draw_points()
            pygame.display.flip()

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 ((col * self.cell_size) + self.padding, (row * self.cell_size) + self.padding,
                                  self.cell_size, self.cell_size), 1)

    def draw_points(self):
        start_rect = pygame.Rect(self.start_point[1] * self.cell_size + self.padding,
                                 self.start_point[0] * self.cell_size + self.padding, self.cell_size, self.cell_size)
        end_rect = pygame.Rect(self.end_point[1] * self.cell_size + self.padding,
                               self.end_point[0] * self.cell_size + self.padding, self.cell_size, self.cell_size)

        pygame.draw.rect(self.screen, (255, 0, 0), start_rect)
        pygame.draw.rect(self.screen, (0, 255, 0), end_rect)

    def draw_obstacles(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.obstacle_map[row][col] == 0:
                    obstacle_rect = pygame.Rect(col * self.cell_size + self.padding,
                                                row * self.cell_size + self.padding, self.cell_size, self.cell_size)
                    pygame.draw.rect(self.screen, (255, 255, 0), obstacle_rect)
