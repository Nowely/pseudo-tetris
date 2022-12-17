import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.animation as animation


def configure_plot(ax):
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.set(xlabel='width')
    ax.set(ylabel='depth')
    ax.set(zlabel='height')


def show(data: np.ndarray):
    ax = plt.figure().add_subplot(projection='3d')
    configure_plot(ax)

    ax.voxels(data, edgecolors='#BFAB6E')
    plt.show()


def show_gif(slices: list[np.ndarray], interval: int = 200):
    def update_plot(num):
        ax.clear()
        configure_plot(ax)
        ax.voxels(slices[num], edgecolors='#BFAB6E')

    # Open gif in a modal window. Actual for PyCharm.
    matplotlib.use("TkAgg")

    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    ani = animation.FuncAnimation(fig, update_plot, interval=interval, frames=len(slices))
    plt.show()

    return ani
