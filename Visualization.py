import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import plotly.graph_objects as go
import matplotlib.style as mplstyle


def configure_plot(ax):
    ax.set_box_aspect(aspect=(1, 1, 1))
    ax.set(xlabel='width')
    ax.set(ylabel='depth')
    ax.set(zlabel='height')


def show(data: np.ndarray):
    matplotlib.use("TkAgg")
    mplstyle.use('fast')
    matplotlib.rcParams['path.simplify'] = True
    matplotlib.rcParams['agg.path.chunksize'] = 10000
    matplotlib.rcParams['path.simplify_threshold'] = 1.0
    ax = plt.figure().add_subplot(projection='3d')
    configure_plot(ax)

    ax.voxels(data)
    plt.show()


x = [0, 0, 1, 1, 0, 0, 1, 1]
y = [0, 1, 1, 0, 0, 1, 1, 0]
z = [0, 0, 0, 0, 1, 1, 1, 1]


def show_by_3d_mesh(data: np.ndarray):
    def create_mesh_cube_by_dot(dot):
        x1, y1, z1 = dot
        my3dmesh = go.Mesh3d(
            x=list(np.asarray(x) + x1),
            y=list(np.asarray(y) + y1),
            z=list(np.asarray(z) + z1),
            alphahull=0, intensity=np.linspace(1, 1, 8, endpoint=True), name='y')
        return my3dmesh

    XYZ = np.argwhere(data)
    fig = go.Figure()
    for xyz in XYZ:
        fig.add_trace(create_mesh_cube_by_dot(xyz))
    fig.show()


def show_by_3d_scatter(data: np.ndarray):
    def create_point_cloud(dot):
        x1, y1, z1 = dot
        x, y, z = np.mgrid[x1:x1 + 0.9:8j, y1:y1 + 0.9:8j, z1:z1 + 0.9:8j]
        return (x.flatten(), y.flatten(), z.flatten())

    a = np.argwhere(data)
    X = []
    Y = []
    Z = []
    for l in a:
        x, y, z = create_point_cloud(l)
        X.extend(x)
        Y.extend(y)
        Z.extend(z)

    marker_data = go.Scatter3d(
        x=X,
        y=Y,
        z=Z,
        marker=go.scatter3d.Marker(size=3),
        mode='markers'
    )
    fig = go.Figure(data=marker_data)
    fig.show()
