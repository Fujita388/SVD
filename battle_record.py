import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
import random
import play


# 1. get_npの非グローバル変数化
# play(get_np)
# 2. 二つの評価関数を受け取って戦わせる関数
# play(get_np1, get_np2)
# get_np1を先手 get_np2を後手として戦わせて、結果{-1,0,1}を返す関数


def match(file):
    np.load('study/svd_study/file') 
    play.Q()
    play.play()


def battle(get_np1, get_np2):
    w1 = 0
    w2 = 0
    trial = 1000
    for _ in trial:
        w = play(get_np1, get_np2)
        if w==1:
            w1 += 1
        else:
            w2 += 1
        w = play(get_np2, get_np1)
        if w==1:
            w1 += 1
        else:
            w2 += 1
    print(f"1 win = {w1/trial}")
    print(f"draw = {(trial-w1-w2)/trial}")


#戦績とランクのグラフをプロット
def make_plot():
    original_np = np.load('study/svd_study/three_eyes.npy')  #もとの評価値をロード
    original_np2 = original_np.reshape(81, 243)        #もとの行列をreshape
    u, s, v = linalg.svd(original_np2)                 #svd
    x = []
    y = []
    for i in range(1, 82):
        r = i               #残す特異値の数   
        ur = u[:, :r]
        sr = np.diag(np.sqrt(s[:r]))       #sの平方根
        vr = v[:r, :]
        A = ur @ sr
        B = sr @ vr
        #もとの配列に復元#
        svd_np = np.array(A @ B)
        svd_np2 = svd_np.reshape((3,3,3,3,3,3,3,3,3))     
        np.save('study/svd_study/three_eyes2', svd_np2)
        #グラフのx,y成分#
        x.append(i)
        y.append(play100())
    plt.xlabel("rank")
    plt.ylabel("average")
    plt.plot(x, y)
    plt.show()