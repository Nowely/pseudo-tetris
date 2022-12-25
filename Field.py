from Figure import Figure
import numpy as np


class Field:
    map: np.ndarray
    "3d boolean array of a final field state."

    slices: list[np.ndarray] = []
    "List of 3d boolean array. Represent each slice of a map state. Used for animation."

    def __init__(self, width: int, depth: int, height: int):
        self.map = np.zeros((width, depth, height), bool)
        self._height = height

    def add_random_figure(self):
        width, depth, height = self.map.shape
        r_width, r_depth, r_height = np.random.randint(1, [
            round(width / 2) + 1, round(depth / 2) + 1, round(height / 2) + 1
        ])
        return self.add_figure(
            Figure(r_width, r_depth, r_height),
            (np.random.randint(width), np.random.randint(height))
        )

    def add_figure(self, figure: Figure, position: tuple[int, int] = (0, 0)):
        """Return height of added figure position. If -1 then figure is not added."""

        [final_figure_map, height] = self._get_final_figure_map(figure, position)
        self.map |= final_figure_map
        self.slices.append(self.map)
        return height

    def _get_final_figure_map(self, figure: Figure, position: tuple[int, int]):
        width, depth = position

        figure_map = np.zeros(self.map.shape, bool)
        for height in range(self._height):
            if not self._is_intersect(height, figure, position):
                return [figure.get_expanded_map(self.map.shape, position=(width, depth, height)), height]
        return [figure_map, -1]

    def _is_intersect(self, height: int, figure, position: tuple[int, int]):
        if height == -1:
            return True

        if position[0] + figure.width > self.map.shape[0]:
            return True
        if position[1] + figure.depth > self.map.shape[1]:
            return True
        if height + figure.height > self.map.shape[2]:
            return True

        field_slice = self.map[
                      position[0]:position[0] + figure.width,
                      position[1]:position[1] + figure.depth,
                      height: height + figure.height
                      ]

        if np.any(field_slice & figure.map):
            return True

        return False
