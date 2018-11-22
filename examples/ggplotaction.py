from ggplot import *
import numpy as np
from matplotlib import pyplot as plot
from matplotlib import animation


print(ggplot(meat, aes('date', 'beef')) +
      geom_line(color='black') +
      scale_x_date(breaks=date_breaks('7 years'), labels='%b %Y') +
      scale_y_continuous(labels='comma'))

fig = plot.figure()
G = ggplot(meat, aes('wearenumberone'))


def init():
    return G,


def animate(i):
    geom_line(list(range(i)), list(range(i)))
    return G,


anim = animation.FuncAnimation(
    fig, animate, init_func=init, frames=200, interval=1, blit=True)
