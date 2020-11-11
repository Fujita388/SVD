import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
import random
import all_search
import original_play
import svd_play


# 1. get_npの非グローバル変数化
# play(get_np)
# 2. 二つの評価関数を受け取って戦わせる関数
# play(get_np1, get_np2)
# 3. get_np1を先手 get_np2を後手として戦わせて、結果{-1,0,1}を返す関数




#二つの評価関数を受け取って戦わせる      
def match1():                  #original先行
    input_list = [0]*9
    for i in range(9):
        if all_search.win(input_list) != 0:
            break
        if (i % 2) == 0:
            original_play.play(input_list)
        if (i % 2) == 1:
            svd_play.play(input_list)  
    return all_search.win(input_list)
    

def match2():                 #svd先行
    input_list = [0]*9
    for i in range(9):
        if all_search.win(input_list) != 0:
            break
        if (i % 2) == 0:
            svd_play.play(input_list)
        if (i % 2) == 1:
            original_play.play(input_list)  
    return all_search.win(input_list)
    


#print(match2())

# h = [0, 0, 0] 
# for _ in range(500):
#     if match2() == 0:
#         h[0] += 1
#     if match2() == 1:    #先行の勝ち
#         h[1] += 1
#     if match2() == -1:   #後攻の勝ち
#         h[2] += 1
# print(h)



#先行後攻の有利不利を加味した結果を返す関数
def battle():
    w1 = 0           #originalの勝ち
    w2 = 0           #svdの勝ち
    trial = 100
    for _ in range(trial):
        w = match1()
        if w == 1:    #originalの勝ち
            w1 += 1
        if w == -1:   #svdの勝ち
            w2 += 1  
        w = match2()
        if w == 1:    #svdの勝ち
            w2 += 1
        if w == -1:   #originalの勝ち
            w1 += 1
    # print(w1, w2)
    # print(f"original-win = {w1 / (trial*2)}")
    # print(f"svd-win = {w2 / (trial*2)}")
    # print(f"draw = {(trial*2-w1-w2) / (trial*2)}")
    w1_ratio = w1 / (trial*2)
    w2_ratio = w2 / (trial*2)
    return [w1_ratio, w2_ratio, 1 - w1_ratio - w2_ratio]


#print(battle())


#戦績とランクのグラフをプロット
def make_plot():
    #svd#
    original_np = np.load('study/svd_study/three_eyes.npy')  #もとの評価値をロード
    original_np2 = original_np.reshape(81, 243)        #もとの行列をreshape
    u, s, v = linalg.svd(original_np2)                 #svd
    x = []
    y1 = []                                  #originalが勝つ割合
    y2 = []                                  #svdが勝つ割合
    y3 = []                                  #引き分けの割合
    for i in range(0, 82):
        r = i                                    #残す特異値の数
        ur = u[:, :r]
        sr = np.diag(np.sqrt(s[:r]))                #sの平方根
        vr = v[:r, :]
        A = ur @ sr
        B = sr @ vr
        #データの復元#
        svd_np = np.array(A @ B)
        svd_np2 = svd_np.reshape((3,3,3,3,3,3,3,3,3))     #もとの配列に復元
        #svdした評価値のnp配列をファイルに保存#
        np.save('study/svd_study/three_eyes2', svd_np2)                    
        x.append(i / 81)                         #残した特異値の割合
        y1.append(battle()[0])
        y2.append(battle()[1])
        y3.append(battle()[2])
    plt.xlabel("left singular value ratio")
    #plt.ylabel("ratio")
    plt.plot(x, y1, color = 'red')
    plt.plot(x, y2, color = 'blue')
    plt.plot(x, y3, color = 'green')
    plt.show()


make_plot()