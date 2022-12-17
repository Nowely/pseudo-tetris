import matplotlib.pyplot as plt
import numpy as np


def show(data: np.ndarray):
    ax = plt.figure().add_subplot(projection='3d')
    edge_colors = np.where(data, '#BFAB6E', '#0000')
    ax.voxels(data, edgecolors=edge_colors)
    ax.set_aspect('equal')

    ax.set(xlabel='x')
    ax.set(ylabel='y')
    ax.set(zlabel='h')

    plt.show()
