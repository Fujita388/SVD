import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
import battle_record2 as b2


get_np = np.load('study/svd_study/three_eyes.npy')         #もとの評価値の配列をロード


#戦績とランクのグラフをプロット
def make_plot():              
    #battle#
    x = []
    y1 = []                                  #originalが勝つ割合
    y2 = []                                  #svdが勝つ割合
    y3 = []                                  #引き分けの割合
    #frobenius#
    y4 = []
    original_np = get_np.reshape(81,243)     #もとの行列をreshape
    ######original_np = get_np.reshape(27,729)     
    X = original_np.copy()        
    u, s, v = linalg.svd(X)                              #svd
    norm = np.sqrt(np.sum(X * X))                        #sのフロベニウスノルム
    for r in range(0, 82):
    #####for r in range(0, 28):
        x.append(r / 81)                         #残した特異値の割合
        #####x.append(r / 27)                         
        #battle#
        y1.append(b2.battle(get_np, b2.approx(get_np, r))[0])
        y2.append(b2.battle(get_np, b2.approx(get_np, r))[1])
        y3.append(b2.battle(get_np, b2.approx(get_np, r))[2])
        #frobenius#  
        ur = u[:, :r]
        sr = np.diag(np.sqrt(s[:r]))                #sの平方根
        vr = v[:r, :]
        A = ur @ sr
        B = sr @ vr
        Y = A @ B                                   #近似した行列
        norm1 = np.sqrt(np.sum((X-Y) * (X-Y)))     #フロベニウスノルム
        y4.append(norm1 / norm)
    plt.xlabel("left singular value ratio")
    ######plt.ylabel("ratio")
    #battle#
    plt.plot(x, y1, color = 'red')
    plt.plot(x, y2, color = 'blue')
    plt.plot(x, y3, color = 'green')
    #frobenius#
    plt.plot(x, y4, color = 'black')

    plt.show()


make_plot()