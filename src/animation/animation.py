import pygame
from pygame import font

font.init()


class Animation(pygame.Surface):
    WIDTH = 900
    HEIGHT = 400
    START_INIT_POS = (30, 30)
    GOAL_INIT_POS = (WIDTH - 30, HEIGHT - 30)
    START_COLOR = (0, 255, 0)
    GOAL_COLOR = (255, 0, 0)
    RADIUS = 20
    OBSTACLES_COLOR = (77, 135, 181)
    OBSTACLES_RADIUS = 10

    # Font used to display information about the algorithm:
    FONT = font.SysFont('Tahoma', 25, bold=True)

    # During RRT, update the screen every MAX_EDGES_POOL new edges created.
    MAX_EDGES_POOL = 10

    # Filename to save and load obstacles map:
    MAP_FILENAME = 'map.png'

    def __init__(self, width=WIDTH, height=HEIGHT, start_pos=START_INIT_POS, goal_pos=GOAL_INIT_POS,
                 start_color=START_COLOR, goal_color=GOAL_COLOR, radius=RADIUS, obstacles_color=OBSTACLES_COLOR,
                 obstacles_radius=OBSTACLES_RADIUS):
        super().__init__((width, height))

        self.width = width
        self.height = height
        self.start_color = start_color
        self.goal_color = goal_color
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.radius = radius
        self.obstacles_color = obstacles_color
        self.obstacles_radius = obstacles_radius

        # Surfaces drawn to the animation surface:
        self.obstacles_surface = pygame.Surface((width, height))
        self.tree_surface = pygame.Surface((width, height))
        self.info_surface = pygame.Surface((width, height))

        self.tree_surface.set_colorkey((0, 0, 0))
        self.info_surface.set_colorkey((0, 0, 0))

        self.edges_pool = []
        self.show_info = False

    def draw_obstacle(self, position):
        pygame.draw.circle(self.obstacles_surface, self.obstacles_color, position, self.obstacles_radius)

    def erase_obstacle(self, position):
        pygame.draw.circle(self.obstacles_surface, (0, 0, 0), position, self.obstacles_radius)

    def clear_obstacles(self):
        self.obstacles_surface.fill(0)

    def clear_tree(self):
        self.tree_surface.fill(0)

    def save_obstacles(self):
        pygame.image.save(self.obstacles_surface, Animation.MAP_FILENAME)

    def load_obstacles(self):
        # global obstaclesSurface
        self.obstacles_surface = pygame.image.load(Animation.MAP_FILENAME)

    def add_edge(self, edge):
        # global edgesPool
        self.edges_pool.append(edge)
        if len(self.edges_pool) >= Animation.MAX_EDGES_POOL:
            for e in self.edges_pool:
                pygame.draw.circle(self.tree_surface, (255, 128, 0), e[1], 2)
                pygame.draw.line(self.tree_surface, (255, 255, 255), e[0], e[1])
            self.edges_pool = []
            self.update()

    def clear_edges_pool(self):
        # global edgesPool
        self.edges_pool = []

    def toggle_info(self):
        # global showInfo
        self.show_info = not self.show_info

    def update_info(self, elapsed, nodes, height, length=None):
        self.info_surface.fill(0)
        elapsed = format(elapsed, '.4f')
        lines = [
            f'Time: {elapsed}s',
            f'Nodes: {nodes}',
            f'Height: {height}'
        ]
        if length:
            lines.append(f'Path length: {length}')
        for i in range(len(lines)):
            temp = Animation.FONT.render(lines[i], 0, (255, 255, 0), (0, 0, 1))
            self.info_surface.blit(temp, (self.width - temp.get_width(), i * Animation.FONT.get_height()))

    def draw_path(self, parent):
        # global showInfo
        self.show_info = True
        current = self.goal_pos
        while parent[current]:
            pygame.draw.line(self.tree_surface, (0, 0, 255), current, parent[current], 4)
            pygame.draw.circle(self.tree_surface, (0, 191, 255), current, 4)
            current = parent[current]
        pygame.draw.circle(self.tree_surface, (0, 191, 255), current, 4)

    def update(self):
        """Update the surface."""
        self.fill(0)
        self.blit(self.obstacles_surface, (0, 0))
        pygame.draw.circle(self, self.goal_color, self.goal_pos, self.radius)
        pygame.draw.circle(self, self.start_color, self.start_pos, self.radius)
        self.blit(self.tree_surface, (0, 0))
        if self.show_info:
            self.blit(self.info_surface, (0, 0))
        # pygame.display.flip()
