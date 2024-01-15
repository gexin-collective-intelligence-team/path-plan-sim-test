from config import *
from rrt import rrt
import drawing
import events
import pygame as pg

pg.init()


def main():
    drawing.screen = pg.display.set_mode((WIDTH, HEIGHT))

    game_state = 'waiting'

    while True:
        event = pg.event.poll()
        mouse_pos = pg.mouse.get_pos()

        game_state = events.main_handler(event, game_state, mouse_pos)

        if game_state == 'quit':
            return
        elif game_state == 'start-positioning':
            drawing.startPos = mouse_pos
        elif game_state == 'goal-positioning':
            drawing.goalPos = mouse_pos
        elif game_state == 'drawing':
            drawing.draw_obstacle(mouse_pos)
        elif game_state == 'erasing':
            drawing.erase_obstacle(mouse_pos)
        elif game_state == 'clear':
            drawing.clear_obstacles()
        elif game_state == 'save':
            drawing.save_obstacles()
        elif game_state == 'load':
            drawing.load_obstacles()
        elif game_state == 'rrt':
            drawing.clear_edges_pool()
            tree = rrt(drawing.startPos, drawing.goalPos, drawing.obstaclesSurface)
            if tree:  # A path was found:
                drawing.draw_path(tree)
                game_state = 'path-found'
            else:  # User terminated the algorithm's execution:
                game_state = 'waiting'

        drawing.update()


if __name__ == '__main__':
    main()
