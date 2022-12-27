import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.animation as animation
import plotly.graph_objects as go
from Figure import Figure


def configure_plot(ax):
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.set(xlabel='width')
    ax.set(ylabel='depth')
    ax.set(zlabel='height')


def show(data: np.ndarray):
    ax = plt.figure().add_subplot(projection='3d')
    configure_plot(ax)

    ax.voxels(data)
    plt.show()


def show1(data: np.ndarray):
    # print(np.random.rand(6500, 3))
    print(data[:, 0, 0].ravel())
    # print(np.array(data[:, 0, 0]))
    # print(data[0, :, 0])
    # print(data[0, 0, :])
    # print(data)
    # fig = go.Figure(data=go.Isosurface(
    #     x=data[:, 0, 0].astype(int),
    #     y=data[0, :, 0].astype(int),
    #     z=data[0, 0, :].astype(int),
    #     value=[1, 2, 3, 4, 5, 6, 7, 8],
    #     isomin=2,
    #     isomax=6,
    # ))

    # print(data[:, 0, 0].ravel().astype(int))
    # print(np.where(data[:, 0, 0]))
    # print(np.where(data))
    # print(np.argwhere(data))
    a = np.argwhere(data)
    # print(np.concatenate([0, 1, 0, 1, 0, 1, 0, 1],  map(lambda x: x+1, [0, 1, 0, 1, 0, 1, 0, 1])))
    X, Y, Z = np.mgrid[0:15, 0:15, 0:15]
    # print(X)
    values = (1 <= X) * (X < 3) * (1 <= Y) * (Y < 3) * Z
    print(values)
    # fig = go.Figure(data=go.Isosurface(
    #     x=X.flatten(),
    #     y=Y.flatten(),
    #     z=Z.flatten(),
    #     value=(X * Y * Z).flatten(),
    #     isomin=10,
    #     isomax=40,
    #     caps=dict(x_show=False, y_show=False)
    # ))
    x=[0, 0, 1, 1, 0, 0, 1, 1]
    y=[0, 1, 1, 0, 0, 1, 1, 0]
    z=[0, 0, 0, 0, 1, 1, 1, 1]
    my3dmesh = go.Mesh3d(x=x, y=y, z=z, alphahull=0, intensity=np.linspace(1, 1, 8, endpoint=True), name='y')
    fig = go.Figure(data=my3dmesh)

    x=[1, 1, 2, 2, 1, 1, 2, 2]
    y=[1, 2, 2, 1, 1, 2, 2, 1]
    z=[1, 1, 1, 1, 2, 2, 2, 2]
    my3dmesh1 = go.Mesh3d(x=x, y=y, z=z, alphahull=0, intensity=np.linspace(1, 1, 8, endpoint=True), name='y')
    fig.add_trace(my3dmesh1)
    #fig.show()

    def _get_shift_map(self, shift: tuple[int, int, int], figure: Figure):
        X, Y, Z = np.indices(self.map.shape)
        shift_width, shift_depth, height_shift = shift

        width_map = (shift_width <= X) & (X < figure.width + shift_width)
        depth_map = (shift_depth <= Y) & (Y < figure.depth + shift_depth)
        height_map = (height_shift <= Z) & (Z < figure.height + height_shift)

        shift_map = width_map & depth_map & height_map
        return np.ndarray(self.map.shape, bool, shift_map)

    # fig = go.Figure(data=go.Isosurface(
    #     x=[0, 1, 0, 1, 0, 1, 0, 1],
    #     y=[0, 0, 1, 1, 0, 0, 1, 1],
    #     z=[0, 0, 0, 0, 1, 1, 1, 1],
    #     value=[2.5, 2, 2, 2, 2, 2, 2, 2],
    #     surface=dict(count=3, fill=0.7, pattern='odd'),
    #     caps=dict(x_show=True, y_show=True),
    # ))

    # marker_data = go.Scatter3d(
    #     x=a[:, 0],
    #     y=a[:, 1],
    #     z=a[:, 2],
    #     marker=go.scatter3d.Marker(size=30),
    #     mode='markers'
    # )
    # fig = go.Figure(data=marker_data)
    fig.show()


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
