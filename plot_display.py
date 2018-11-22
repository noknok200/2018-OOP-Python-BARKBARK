from marcap import marcap_utils as mu
from matplotlib import pyplot as plot
from matplotlib import animation

'''
fig = plot.figure()
ax = plot.axes(xlim=(0, 2), ylim=(-200, 200))
line, = ax.plot([], [], lw=2)
'''

code = '005930'
l = mu.marcap_date_range('2018-05-01', '2018-10-31', code)
ml = list(l['Marcap'])

print(ml)

# def init():
