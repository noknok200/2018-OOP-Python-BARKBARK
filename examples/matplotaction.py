import numpy as np
from matplotlib import pyplot as plot
from matplotlib import animation as ani


fig = plot.figure()
ax = plot.axes(xlim=(0, 2), ylim=(-2, 2))
line, _ = ax.plot([], [], lw=2)
