from Field import Field
from Figure import Figure
from Visualization import show, show_gif


if __name__ == '__main__':
    field = Field(6, 6, 6)
    field.add_figure(Figure(2, 2, 1), (2, 1))
    field.add_figure(Figure(2, 5, 2))
    field.add_figure(Figure(1, 1, 1))
    field.add_figure(Figure(2, 2, 2))
    field.add_figure(Figure(2, 2, 2), (3, 2))

    show(field.map)
    show_gif(field.slices)  # .save('pseudo-tetris.gif', writer='imagemagick', fps=5)
