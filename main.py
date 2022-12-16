import numpy as np

from Box import Box
from Field import Field
from Visualization import show

if __name__ == '__main__':
    field = Field(4, 6, 6)
    field.add_box(Box(2, 2, 1))
    field.add_box(Box(2, 5, 2))
    field.add_box(Box(1, 1, 1))
    field.add_box(Box(2, 2, 2))
    show(field.map)
