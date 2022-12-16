import Box
import numpy as np


class Field:
    def __init__(self, x: int, y: int, height: int):
        self.map = np.zeros((x, y, height), bool)
        self.height = height

    def add_box(self, box: Box):
        box_map = self.get_box_map(box)
        self.map = self.map | box_map
        return self.map

    def get_box_map(self, box: Box):
        current_height = self.height - 1
        box_map = self.get_shift((0, 0, current_height), box)
        while not self.is_intersect(box_map, current_height-1):
            current_height = current_height - 1
            box_map = self.get_shift((0, 0, current_height), box)
        return box_map

    def is_intersect(self, box: np.ndarray, h: int):
        if h == -1:
            return True

        h_map_slice = self.map[:, :, h]
        h_box_slice = box[:, :, h+1]
        return np.any(h_map_slice & h_box_slice)

    def get_shift(self, shift: tuple[int, int, int], box: Box):
        x1, y1, h1 = shift
        x, y, h = np.indices(self.map.shape)
        xs = (x1 <= x) & (x < box.x + x1)
        ys = (y1 <= y) & (y < box.y + y1)
        hs = (h1 <= h) & (h < box.h + h1)
        return np.ndarray(self.map.shape, buffer=xs & ys & hs, dtype=bool)