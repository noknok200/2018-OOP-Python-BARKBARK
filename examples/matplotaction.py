# 참고: http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as ani


fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.tan(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,


anim = ani.FuncAnimation(
    fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.show()
