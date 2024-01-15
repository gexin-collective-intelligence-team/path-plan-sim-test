from utils import dist


class PointsContainer:
    """
    An ADT to store 2D points and find a point's nearest neighbor.

    To solve the Nearest Neighbor Search problem (NNS), I chose to
      do a linear search, since it is much simpler than other
      approaches and produces a reasonably good result here.

    Time complexities:
      - insert: O(1)
      - NNS: O(N), where N is the number of points currently inside the container.
    """

    def __init__(self):
        self._points = []

    def insert(self, point):
        self._points.append(point)

    def nns(self, point):
        best = self._points[0]  # will throw IndexError if self._points is empty.
        best_dist = dist(best, point)
        for p in self._points:
            p_dist = dist(p, point)
            if p_dist < best_dist:
                best = p
                best_dist = p_dist
        return best
