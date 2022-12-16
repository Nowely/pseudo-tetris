import Figure
import numpy as np


class Field:
    def __init__(self, x: int, y: int, height: int):
        self.map = np.zeros((x, y, height), bool)
        self.height = height

    def add_figure(self, figure: Figure, position: tuple[int, int] = (0, 0)):
        box_map = self.__get_box_map(figure, position)
        self.map = self.map | box_map
        return self.map

    def __get_box_map(self, figure: Figure, position: tuple[int, int]):
        x, y = position
        current_height = self.height - 1
        box_map = self.__get_shift((x, y, current_height), figure)
        while not self.__is_intersect(box_map, current_height - 1):
            current_height = current_height - 1
            box_map = self.__get_shift((x, y, current_height), figure)
        return box_map

    def __is_intersect(self, box: np.ndarray, h: int):
        if h == -1:
            return True

        h_map_slice = self.map[:, :, h]
        h_box_slice = box[:, :, h+1]
        return np.any(h_map_slice & h_box_slice)

    def __get_shift(self, shift: tuple[int, int, int], box: Figure):
        x1, y1, h1 = shift
        x, y, h = np.indices(self.map.shape)
        xs = (x1 <= x) & (x < box.x + x1)
        ys = (y1 <= y) & (y < box.y + y1)
        hs = (h1 <= h) & (h < box.h + h1)
        return np.ndarray(self.map.shape, buffer=xs & ys & hs, dtype=bool)