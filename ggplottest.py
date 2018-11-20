import ggplot as gp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

ex = 0
var = 1

d = {'x': np.random.normal(ex, var, 1000),
     'y': np.random.normal(ex, var, 1000)}

df = pd.DataFrame(d)
df.boxplot(column=['x', 'y'])
plot.show()
