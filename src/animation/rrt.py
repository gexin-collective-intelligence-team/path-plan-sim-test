from .points_container import PointsContainer
from .collision import collision
from .utils import random_point, inside
import pygame as pg
# from . import drawing
from .animation import Animation
from . import events
import time


def rrt(surface, start, goal, obstacles):
    """
    start -- point (x, y)
    goal  -- point (x, y)
    obstacles: pygame.Surface
    """
    parent = {start: None}
    depth = {start: 0}

    container = PointsContainer()
    container.insert(start)

    height = 0
    nodes = 1

    current = start

    start_time = time.perf_counter()

    while not inside(current, goal):
        if not events.rrt_handler():  # handle user events.
            return None

        if surface.show_info:  # drawing-related.
            elapsed = time.perf_counter() - start_time
            surface.update_info(elapsed, nodes, height)
            surface.update()

        sample = random_point()
        nearest = container.nns(sample)

        if sample == nearest:  # do not allow two identical points.
            continue

        if not collision(sample, nearest, obstacles):
            container.insert(sample)
            parent[sample] = nearest
            depth[sample] = depth[nearest] + 1

            height = max(height, depth[sample])
            nodes += 1

            surface.add_edge((nearest, sample))

            current = sample

    if goal not in parent:
        parent[goal] = current
        depth[goal] = depth[current] + 1
        height = max(height, depth[goal])
        nodes += 1
        surface.add_edge((current, goal))

    elapsed = time.perf_counter() - start_time
    surface.update_info(elapsed, nodes, height, depth[goal])

    return parent
