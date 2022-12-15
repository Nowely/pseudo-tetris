from Box import Box
from Field import Field
from Visualization import show

box = Box(1, 2)
field = Field(10, 10)

if __name__ == '__main__':
    field.add_box(box)
    field.add_box(Box(2, 3))
    field.add_box(Box(2, 3))

    show(field.get_snapshot())
