from dataclasses import dataclass

import numpy as np


@dataclass
class Figure:
    width: int
    depth: int
    height: int

    def __post_init__(self):
        self.map = np.ones((self.width, self.depth, self.height), bool)