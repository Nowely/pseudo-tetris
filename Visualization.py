import matplotlib.pyplot as plt
import numpy as np


def show(data: np.ndarray):
    ax = plt.figure().add_subplot(projection='3d')
    edge_colors = np.where(data, '#BFAB6E', '#0000')
    ax.voxels(data, edgecolors=edge_colors)
    ax.set_aspect('equal')

    ax.set(xlabel='width')
    ax.set(ylabel='depth')
    ax.set(zlabel='height')

    plt.show()
