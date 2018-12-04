"""
실행 안되면 안되는 대로 놔둬
"""
from __future__ import print_function
import sys
import matplotanimate_LES
from calculate_asset import cal_asset

def press(self):
    if matplotanimate_LES.first_click == 0:
        matplotanimate_LES.first_click = 1
    else:
        # 점수 갱신
        # matplotanimate_LES.score_button = cal_asset(matplotanimate_LES.asset, matplotanimate_LES.stock_data[matplotanimate_LES.click_time],matplotanimate_LES.stock_data[matplotanimate_LES.t_time+100])
        matplotanimate_LES.plt.title(cal_asset(matplotanimate_LES.asset, matplotanimate_LES.stock_data[matplotanimate_LES.click_time],matplotanimate_LES.stock_data[matplotanimate_LES.t_time+100]))
        matplotanimate_LES.first_click = 0
        matplotanimate_LES.data_storage.append([matplotanimate_LES.click_time, matplotanimate_LES.t_time+100])
    click_time = matplotanimate_LES.t_time + 100
    matplotanimate_LES.click_time = click_time
    #점수갱신
    # matplotanimate_LES.plt.title(matplotanimate_LES.asset)
    sys.stdout.flush()

#점수 시각화
# matplotanimate_LES.plt.title(matplotanimate_LES.asset)
