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
        self.add_figure(
            Figure(r_width, r_depth, r_height),
            (np.random.randint(width), np.random.randint(height))
        )

    def add_figure(self, figure: Figure, position: tuple[int, int] = (0, 0)):
        final_figure_map = self._get_final_figure_map(figure, position)
        self.map |= final_figure_map

    def _get_final_figure_map(self, figure: Figure, position: tuple[int, int]):
        width, depth = position

        figure_map = np.zeros(self.map.shape, bool)
        for height in range(self._height - 1, -1, -1):
            current_figure_map = self._get_shift_map((width, depth, height), figure)
            if not self._is_intersect(current_figure_map, height, figure):
                figure_map = current_figure_map
        return figure_map

    def _get_shift_map(self, shift: tuple[int, int, int], figure: Figure):
        width, depth, height = np.indices(self.map.shape)
        shift_width, shift_depth, height_shift = shift

        width_map = (shift_width <= width) & (width < figure.width + shift_width)
        depth_map = (shift_depth <= depth) & (depth < figure.depth + shift_depth)
        height_map = (height_shift <= height) & (height < figure.height + height_shift)

        shift_map = width_map & depth_map & height_map
        return np.ndarray(self.map.shape, bool, shift_map)

    def _is_intersect(self, figure_map: np.ndarray, height: int, figure):
        if height == -1:
            return True

        for d in range(figure.height):
            if height + d >= figure_map.shape[2]:
                self.slices.append(figure_map | self.map)
                return True

            figure_slice = figure_map[:, :, height + d]
            field_slice = self.map[:, :, height + d]
            if np.any(field_slice & figure_slice):
                return True

        self.slices.append(figure_map | self.map)
        return False
