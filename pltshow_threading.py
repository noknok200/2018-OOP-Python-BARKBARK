"""
https://matplotlib.org/examples/event_handling/keypress_demo.html
반드시 참고하기
matlib.pyplot에서 띄운 figure에 keypress를 바인드 함+ 키를 누를떄마다 그래프가 변환됨-> 함수 실행 가능
결론: 이득이득
"""

from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt


def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()

fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()