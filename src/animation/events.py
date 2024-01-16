from .config import *
from .utils import dist
from . import drawing
import pygame as pg

mustQuit = False  # flag to indicate that the user closed the program's window.


def rrt_handler():
    """Handle user events during RRT execution."""
    global mustQuit
    event = pg.event.poll()
    if event.type == pg.QUIT:
        mustQuit = True
        return False
    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_h:
            drawing.toggle_info()
        else:
            drawing.clear_tree()
            drawing.showInfo = False
            return False
    return True


def main_handler(event, state, mouse_pos):
    """State transitions when executing the main function."""
    over_start = dist(drawing.startPos, mouse_pos) < RADIUS
    over_goal = dist(drawing.goalPos, mouse_pos) < RADIUS

    if event.type == pg.QUIT:
        return 'quit'
    elif state == 'waiting':
        if mustQuit:
            return 'quit'
        elif event.type == pg.MOUSEBUTTONDOWN:
            if over_start:
                return 'start-positioning'
            elif over_goal:
                return 'goal-positioning'
            elif event.button == 1:
                return 'drawing'
            elif event.button == 3:
                return 'erasing'
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                return 'rrt'
            elif event.key == pg.K_s:
                return 'save'
            elif event.key == pg.K_l:
                return 'load'
            elif event.key == pg.K_c:
                return 'clear'

    elif state in ['drawing', 'erasing', 'start-positioning', 'goal-positioning']:
        if event.type == pg.MOUSEBUTTONUP:
            return 'waiting'

    elif state in ['save', 'load', 'clear']:
        return 'waiting'

    elif state == 'path-found':
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_h:
                drawing.toggle_info()
            else:
                drawing.clear_tree()
                drawing.showInfo = False
                return 'waiting'

    return state
