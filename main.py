from Field import Field
from Figure import Figure
from Visualization import show, show_by_3d_scatter, show_by_3d_mesh
import time


# Show a small field 6x6x6 with determine figures
def show_small_field():
    # Init a field with width = 6, depth = 6, height = 6
    field = Field(6, 6, 6)
    # Add the figure with width = 2, depth = 2, height = 1 and the start position width = 2, depth = 1 of field
    field.add_figure(Figure(2, 2, 1), (2, 1))
    field.add_figure(Figure(2, 5, 2))
    field.add_figure(Figure(1, 1, 1))
    field.add_figure(Figure(2, 2, 2))
    field.add_figure(Figure(2, 2, 2), (3, 2))
    field.add_figure(Figure(1, 1, 3), (4, 1))
    field.add_figure(Figure(1, 1, 1), (1, 0))
    field.add_figure(Figure(1, 2, 1), (4, 2))

    # Show plot with added figures
    show(field.map)
    #show_by_3d_mesh(field.map)
    #show_by_3d_scatter(field.map)


def show_big_field():
    field = Field(120, 100, 100)
    [field.add_random_figure() for _ in range(20)]

    #print(field.map)
    show(field.map)


if __name__ == '__main__':
    tic = time.perf_counter()
    #show_small_field()
    show_big_field()
    toc = time.perf_counter()
    print(f"Computed for {toc - tic:0.4f} seconds")
