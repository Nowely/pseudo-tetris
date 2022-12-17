import numpy as np
from matplotlib import pyplot as plt
import matplotlib; matplotlib.use("TkAgg")
import matplotlib.animation as animation
from Field import Field
from Figure import Figure
from Visualization import show

slices = []

if __name__ == '__main__':
    field = Field(5, 6, 6)
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
    #show(field.map)


def update_lines(num):
    ax.clear()
    ax.set(xlabel='x')
    ax.set(ylabel='y')
    ax.set(zlabel='h')
    edge_colors = np.where(slices[num], '#BFAB6E', '#0000')
    a = ax.voxels(slices[num], edgecolors=edge_colors)
    return a


# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")


ani = animation.FuncAnimation(
    fig, update_lines, interval=300, frames=range(1, len(slices)))
#ani.save('тетрис.gif', writer='imagemagick', fps=2)

plt.show()
