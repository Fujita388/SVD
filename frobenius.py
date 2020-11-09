import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg


#フロベニウスノルムの相対誤差
def frob():
    original_np = np.load('study/svd_study/three_eyes.npy').reshape(81,243)     #もとの行列をreshape
    X = original_np.copy()        
    u, s, v = linalg.svd(X)                 #svd
    #norm = np.sqrt(np.sum(X * X))                      #sのフロベニウスノルム
    norm = np.sum(X * X)                    #sのフロベニウスノルムの二乗
    x = []
    y = []
    for i in range(0, 82):
        r = i               #残す特異値の数   
        ur = u[:, :r]
        sr = np.diag(np.sqrt(s[:r]))       #sの平方根
        vr = v[:r, :]
        A = ur @ sr
        B = sr @ vr
        Y = A @ B              #近似した行列
        #norm1 = np.sqrt(np.sum((X-Y) * (X-Y)))     #フロベニウスノルム
        norm1 = np.sum((X-Y) * (X-Y))             #フロベニウスノルムの二乗
        x.append(i)
        y.append(norm1/ norm)
    plt.xlabel("rank")
    plt.ylabel("difference")
    print(y)
    # plt.yscale('log')
    # plt.plot(x, y)
    # plt.show() 


#実行
frob()