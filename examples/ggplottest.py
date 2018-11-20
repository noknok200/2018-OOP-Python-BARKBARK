import ggplot as gp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

ex = 0
var = 1

ex1 = 1
var1 = 3

d = np.random.normal(ex, var, 1000)

df = pd.DataFrame({'pig': [1, 2, 3, 4]}, index=[
                  1000, 2000, 3000, 4000])
df.plot.line()
plot.show()

# 참고한 페이지: http://uncoded.tistory.com/11
