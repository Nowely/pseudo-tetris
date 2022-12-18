from Field import Field
from Figure import Figure
from Visualization import show, show_gif


def show_small_field():
    field = Field(6, 6, 6)
    field.add_figure(Figure(2, 2, 1), (2, 1))
    field.add_figure(Figure(2, 5, 2))
    field.add_figure(Figure(1, 1, 1))
    field.add_figure(Figure(2, 2, 2))
    field.add_figure(Figure(2, 2, 2), (3, 2))
    field.add_figure(Figure(1, 1, 3), (4, 1))

    show(field.map)
    show_gif(field.slices)  # .save('pseudo-tetris.gif', writer='pillow', fps=5)


def show_big_field():
    field = Field(20, 20, 20)
    [field.add_random_figure() for _ in range(20)]

    show(field.map)
    show_gif(field.slices)  # .save('pseudo-tetris 20x20x20.gif', writer='pillow', fps=30)


if __name__ == '__main__':
    show_small_field()
    #show_big_field()
