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
        expanded_map = np.zeros(shape, bool)
        expanded_map[
        position[0]:position[0] + self.width,
        position[1]:position[1] + self.depth,
        position[2]:position[2] + self.height
        ] = True
        return expanded_map
