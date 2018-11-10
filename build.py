from inspect import getmembers, isfunction
from matplotlib import cm, colors
import jinja2 as jj
import matplotlib.pyplot as plt
import numpy as np

import plots


def brightness(rgb):
    return rgb[0] + rgb[1] * 3 + rgb[2] * 2


def iscolormap(x):
    return issubclass(type(x), colors.Colormap)


def get_colormaps():
    for name, value in getmembers(cm):
        if iscolormap(value) and not name.endswith('_r'):
            a, b = value(0), value(1)
            print(name, a, b)
            if brightness(a) > brightness(b):
                try:
                    value = getattr(value, name + '_r')
                except AttributeError:
                    print("{} doesn't have a reversed version".format(name))
            yield {'colormap_name': name, 'colormap': value}


def get_functions(module):
    for x, y in getmembers(module):
        if isfunction(y) and not x.startswith('_'):
            yield {'function_name': x, 'function': y}


def render_plot(function_name, function, colormap_name, colormap):
    np.random.seed(0)
    plt.clf()
    file_name = "dist/{}-{}.png".format(function_name, colormap_name)
    function(colormap, file_name)


if __name__ == '__main__':
    colormaps = list(get_colormaps())
    functions = list(get_functions(plots))
    loader = jj.FileSystemLoader("templates")
    environment = jj.Environment(loader=loader)
    template = environment.get_template("index.html")
    with open("dist/index.html", 'w') as f:
        f.write(template.render(functions=functions, colormaps=colormaps))
    for x in functions:
        for y in colormaps:
            render_plot(**x, **y)
