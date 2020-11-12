import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
import random
import play


#softmax関数
def softmax(x):
    a = 10
    u = np.sum(np.exp(a*x))
    return np.exp(a*x) / u


get_np = np.load('study/svd_study/three_eyes.npy')         #もとの評価値の配列をロード


#与えた盤面(入力した文字列)に対する評価値を返す
def Q(input_list, np1):
    return np1[input_list[0]][input_list[1]][input_list[2]][input_list[3]][input_list[4]][input_list[5]][input_list[6]][input_list[7]][input_list[8]]


#softmax関数で次の手の評価値を確率化         
def prob(input_list, np1):
    count0 = input_list.count(0)      #要素0の数
    index0 = play.func(input_list)         #要素0のインデックスのリスト
    s = []
    for i in range(count0):
        l = index0[i]
        input_list2 = input_list.copy()
        input_list2[l] = 2 - (count0 % 2)                 #盤面の更新
        if count0 % 2 == 0:
            s.append(Q(input_list2, np1) * -1)         #次の手がバツのときは評価値にマイナスをつける      
        else:
            s.append(Q(input_list2, np1))
    x = np.array(s)
    y = softmax(x)
    return list(y)


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


#次の一手を返す   
def next(np1, np2):                       #np1先攻、np2後攻
    input_list = [0]*9
    for i in range(9):
        index0 = play.func(input_list)    #要素0のインデックスのリスト
        if play.win(input_list) != 0:
            break
        if (i % 2) == 0:        #先攻
            #print(prob(input_list, np1))
            y = random.choices(index0, k = 1, weights = prob(input_list, np1))[0]
        if (i % 2) == 1:        #後攻
            #print(prob(input_list, np2))
            y = random.choices(index0, k = 1, weights = prob(input_list, np2))[0]
        input_list[y] = (i % 2) + 1            #盤面の更新
    return play.win(input_list)


#先行後攻の有利不利を加味した結果を返す関数
def battle(np1, np2):
    w1 = 0           #np1の勝ち
    w2 = 0           #np2の勝ち
    trial = 500
    for _ in range(trial):
        w = next(np1, np2)
        if w == 1:    #np1の勝ち
            w1 += 1
        if w == -1:   #np2の勝ち
            w2 += 1  
        w = next(np2, np1)
        if w == 1:    #np2の勝ち
            w2 += 1
        if w == -1:   #np1の勝ち
            w1 += 1
    # print(w1, w2)
    # print(f"original-win = {w1 / (trial*2)}")
    # print(f"svd-win = {w2 / (trial*2)}")
    # print(f"draw = {(trial*2-w1-w2) / (trial*2)}")
    w1_ratio = w1 / (trial*2)
    w2_ratio = w2 / (trial*2)
    return [w1_ratio, w2_ratio, 1 - w1_ratio - w2_ratio]


#戦績とランクのグラフをプロット
def make_plot():              
    x = []
    y1 = []                                  #originalが勝つ割合
    y2 = []                                  #svdが勝つ割合
    y3 = []                                  #引き分けの割合
    for i in range(0, 82):
        x.append(i / 81)                         #残した特異値の割合
        y1.append(battle(get_np, approx(get_np, i))[0])
        y2.append(battle(get_np, approx(get_np, i))[1])
        y3.append(battle(get_np, approx(get_np, i))[2])
    plt.xlabel("left singular value ratio")
    #plt.ylabel("ratio")
    plt.plot(x, y1, color = 'red')
    plt.plot(x, y2, color = 'blue')
    plt.plot(x, y3, color = 'green')
    plt.show()


make_plot()

#実行
s = "000010000"
list_0 = list(map(int, list(s)))   
#print(Q(list_0, get_np))

#print(prob(list_0, get_np))

#print(next(get_np, approx(get_np, 10)))

#print(battle(get_np, approx(get_np, 10)))

