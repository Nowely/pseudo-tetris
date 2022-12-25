from dataclasses import dataclass

import numpy as np


@dataclass
class Figure:
    width: int
    depth: int
    height: int

    def __post_init__(self):
        self.map = np.ones((self.width, self.depth, self.height), bool)

    def get_expanded_map(self, shape, position: tuple[int, int, int]):
        width, depth, height = np.indices(shape)
        shift_width, shift_depth, height_shift = position

        width_map = (shift_width <= width) & (width < self.width + shift_width)
        depth_map = (shift_depth <= depth) & (depth < self.depth + shift_depth)
        height_map = (height_shift <= height) & (height < self.height + height_shift)

        shift_map = width_map & depth_map & height_map
        return np.ndarray(shape, bool, shift_map)
