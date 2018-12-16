"""
주식을 보여주는 그래프에 keyboard listener가 추가됨.
"""
import sys
import plot_core


def press(self):
    if plot_core.first_click == 0:
        plot_core.first_click = 1
    else:
        plot_core.first_click = 0
        plot_core.data_storage.append(
            [plot_core.click_time, plot_core.t_time+100])
    click_time = plot_core.t_time + 100
    plot_core.click_time = click_time
    sys.stdout.flush()


def startstock():
    plot_core.fig.canvas.mpl_connect('button_press_event', press)
    plot_core.show()
