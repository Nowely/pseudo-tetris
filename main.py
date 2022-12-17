from Field import Field
from Figure import Figure
from Visualization import show, show_gif

slices = []

if __name__ == '__main__':
    field = Field(6, 6, 6)
    slices.append(field.map.copy())
    field.add_figure(Figure(2, 2, 1), (2, 1))
    slices.append(field.map.copy())
    field.add_figure(Figure(2, 5, 2))
    slices.append(field.map.copy())
    field.add_figure(Figure(1, 1, 1))
    slices.append(field.map.copy())
    field.add_figure(Figure(2, 2, 2))
    slices.append(field.map.copy())
    field.add_figure(Figure(2, 2, 2), (3, 2))
    slices.append(field.map.copy())
    # show(field.map)
    show_gif(slices)  # .save('pseudo-tetris.gif', writer='imagemagick', fps=2)
