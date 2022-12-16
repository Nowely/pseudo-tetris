import Figure
import numpy as np


class Field:
    def __init__(self, x: int, y: int, height: int):
        self.map = np.zeros((x, y, height), bool)
        self._height = height

    def add_figure(self, figure: Figure, position: tuple[int, int] = (0, 0)):
        figure_map = self._get_box_map(figure, position)
        self.map = self.map | figure_map
        return self.map

    def _get_box_map(self, figure: Figure, position: tuple[int, int]):
        x, y = position
        current_height = self._height - 1
        figure_map = self._get_shift((x, y, current_height), figure)
        while not self._is_intersect(figure_map, current_height - 1):
            current_height = current_height - 1
            figure_map = self._get_shift((x, y, current_height), figure)
        return figure_map

    def _is_intersect(self, box: np.ndarray, h: int):
        if h == -1:
            return True

        h_map_slice = self.map[:, :, h]
        h_box_slice = box[:, :, h+1]
        return np.any(h_map_slice & h_box_slice)

    def _get_shift(self, shift: tuple[int, int, int], figure: Figure):
        x, y, h = np.indices(self.map.shape)
        x1, y1, h1 = shift
        xs = (x1 <= x) & (x < figure.x + x1)
        ys = (y1 <= y) & (y < figure.y + y1)
        hs = (h1 <= h) & (h < figure.h + h1)
        return np.ndarray(self.map.shape, buffer=xs & ys & hs, dtype=bool)
