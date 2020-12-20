###もとの配列を(81, 243)の行列とみなしてsvd###




import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
import main


get_np = np.load('three_eyes.npy')   


#もとの評価値の配列をsvdする            r:残す特異値の数   
def approx(original_np, r):
    #svd#
    u, s, v = linalg.svd(original_np.reshape(81, 243))                 
    ur = u[:, :r]
    sr = np.diag(np.sqrt(s[:r]))                 #sの平方根
    vr = v[:r, :]
    A = ur @ sr
    B = sr @ vr
    #データの復元#
    svd_np1 = np.array(A @ B)
    svd_np = svd_np1.reshape((3,3,3,3,3,3,3,3,3))     #もとの配列に復元
    return svd_np


#戦績とフロベニウスノルムをプロット
def make_plot():              
    #battle#
    x = []
    y1 = []                                  #originalが勝つ割合
    y2 = []                                  #svdが勝つ割合
    y3 = []                                  #引き分けの割合
    #frobenius#
    y4 = []
    X = get_np.reshape(81,243)     #もとの行列をreshape         
    u, s, v = linalg.svd(X)                              #svd
    norm = np.sqrt(np.sum(X * X))                        #sのフロベニウスノルム
    for r in range(0, 82):                      
        #battle#
        y1.append(main.battle(get_np, approx(get_np, r))[0])
        y2.append(main.battle(get_np, approx(get_np, r))[1])
        y3.append(main.battle(get_np, approx(get_np, r))[2])
        #frobenius#  
        ur = u[:, :r]
        sr = np.diag(np.sqrt(s[:r]))                #sの平方根
        vr = v[:r, :]
        A = ur @ sr
        B = sr @ vr
        Y = A @ B                                   #近似した行列
        norm1 = np.sqrt(np.sum((X-Y) * (X-Y)))     #フロベニウスノルム
        rate = (A.size+B.size) / X.size
        y4.append(norm1 / norm)
        x.append(rate)                         #残した特異値の割合 
    plt.xlabel("compression ratio")
    ######plt.ylabel("ratio")
    #battle#
    plt.plot(x, y1, color = 'red')
    plt.plot(x, y2, color = 'blue')
    plt.plot(x, y3, color = 'green')
    #frobenius#
    plt.plot(x, y4, color = 'black')

    plt.show()

#make_plot()

#datファイル作成
def save_file():
    with open("task1.dat", "w") as f:
        X = get_np.reshape(81,243)     #もとの行列をreshape         
        u, s, v = linalg.svd(X)                              #svd
        norm = np.sqrt(np.sum(X * X))                        #sのフロベニウスノルム
        for r in range(0, 82):                      
            #battle#
            y1 = main.battle(get_np, approx(get_np, r))[0]    #originalが勝つ割合
            y2 = main.battle(get_np, approx(get_np, r))[1]    #svdが勝つ割合
            y3 = main.battle(get_np, approx(get_np, r))[2]    #引き分けの割合
            #frobenius#  
            ur = u[:, :r]
            sr = np.diag(np.sqrt(s[:r]))                #sの平方根
            vr = v[:r, :]
            A = ur @ sr
            B = sr @ vr
            Y = A @ B                                   #近似した行列
            norm1 = np.sqrt(np.sum((X-Y) * (X-Y)))     #フロベニウスノルム
            x = (A.size+B.size) / X.size            #圧縮率
            y4 = norm1 / norm                #フロべニウスノルムの相対誤差
            f.write("{} {} {} {} {}\n".format(x, y1, y2, y3, y4))

#save_file()


#5回分の標準偏差を算出しdatファイルを作成
def std_calc():
	with open("task1_std.dat", "w") as f:
		for r in range(0, 82):                      
			y1 = []
			y2 = []
			y3 = []
			for _ in range(5):     #5回分のループ
				y1.append(main.battle(get_np, approx(get_np, r))[0])    #originalが勝つ割合
				y2.append(main.battle(get_np, approx(get_np, r))[1])    #svdが勝つ割合
				y3.append(main.battle(get_np, approx(get_np, r))[2])    #引き分けの割合
			ans1 = np.std(y1)
			ans2 = np.std(y2)
			ans3 = np.std(y3)
			f.write("{} {} {}\n".format(ans1, ans2, ans3))	


std_calc()





