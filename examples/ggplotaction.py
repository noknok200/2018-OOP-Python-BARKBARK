from ggplot import *
import numpy as np
from matplotlib import pyplot as plot
from matplotlib import animation


str(ggplot(meat, aes('date', 'beef')) +
    geom_line(color='black') +
    scale_x_date(breaks=date_breaks('7 years'), labels='%b %Y') +
    scale_y_continuous(labels='comma'))

print()
