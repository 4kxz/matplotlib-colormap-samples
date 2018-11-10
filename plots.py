
def barchart(colormap, filename):
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.ticker import MaxNLocator
    N = 7
    y = 10 * np.random.rand(N)
    x = range(N)
    fig = plt.figure(figsize=(4, 3))
    c = [colormap(i / N) for i in range(N)]
    plt.bar(x, y, color=c)
    fig.tight_layout()
    # fig = plt.gcf()
    plt.savefig(filename)


def contour(colormap, filename):
    """
    Shows how to combine Normalization and Colormap instances to draw
    "levels" in pcolor, pcolormesh and imshow type plots in a similar
    way to the levels keyword argument to contour/contourf.

    """
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    import numpy as np
    # make these smaller to increase the resolution
    dx, dy = 0.05, 0.05
    # generate 2 2d grids for the x & y bounds
    y, x = np.mgrid[slice(1, 5 + dy, dy),
                    slice(1, 5 + dx, dx)]
    z = np.sin(x)**10 + np.cos(10 + y * x) * np.cos(x)
    # x and y are bounds, so z should be the value *inside* those bounds.
    # Therefore, remove the last value from the z array.
    z = z[:-1, :-1]
    levels = MaxNLocator(nbins=16).tick_values(z.min(), z.max())
    fig = plt.figure(figsize=(5, 3))
    # contours are *point* based plots, so convert our bound into point centers
    cf = plt.contourf(x[:-1, :-1] + dx / 2.,
                      y[:-1, :-1] + dy / 2.,
                      -z,
                      levels=levels,
                      cmap=colormap)
    fig.colorbar(cf)
    # adjust spacing between subplots so `ax1` title and `ax0` tick labels
    # don't overlap
    fig.tight_layout()
    plt.savefig(filename)


def polar_scatter(colormap, filename):
    """
    Demo of scatter plot on a polar axis.

    Size increases radially in this example and color increases with angle
    (just to verify the symbols are being scattered correctly).
    """
    import numpy as np
    import matplotlib.pyplot as plt
    N = 120
    r = 4 * np.random.rand(N)
    theta = 2 * np.pi * np.random.rand(N)
    area = 32 * r**2 * np.random.rand(N)
    fig = plt.figure(figsize=(3.5, 3))
    plt.subplot(111, projection='polar')
    plt.scatter(theta, r, c=theta, s=area, cmap=colormap, lw=0.5)
    plt.savefig(filename)
    fig.tight_layout()
