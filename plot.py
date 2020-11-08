import matplotlib.pyplot as plt
import numpy as np
import random
from scipy import linalg


#win関数
def win(input_list):
    if (input_list[0] == input_list[1] == input_list[2] == 1 or  
        input_list[3] == input_list[4] == input_list[5] == 1 or
        input_list[6] == input_list[7] == input_list[8] == 1 or
        input_list[0] == input_list[3] == input_list[6] == 1 or
        input_list[1] == input_list[4] == input_list[7] == 1 or
        input_list[2] == input_list[5] == input_list[8] == 1 or
        input_list[0] == input_list[4] == input_list[8] == 1 or
        input_list[2] == input_list[4] == input_list[6] == 1):
        return 1       #丸の勝ち
    elif (input_list[0] == input_list[1] == input_list[2] == 2 or  
        input_list[3] == input_list[4] == input_list[5] == 2 or
        input_list[6] == input_list[7] == input_list[8] == 2 or
        input_list[0] == input_list[3] == input_list[6] == 2 or
        input_list[1] == input_list[4] == input_list[7] == 2 or
        input_list[2] == input_list[5] == input_list[8] == 2 or
        input_list[0] == input_list[4] == input_list[8] == 2 or
        input_list[2] == input_list[4] == input_list[6] == 2):
        return -1      #バツの勝ち
    else:
        return 0       #引き分け


#要素0のインデックス抽出
def func(input_list):
    return [i for i, x in enumerate(input_list) if x == 0]


#盤面を表示
def draw_grid(g2):
    g = [" "]*9
    for i in range(9):
        if g2[i] == 1:
            g[i] = "o"
        elif g2[i] == 2:
            g[i] = "x"
    print("----")
    print(f"{g[0]}{g[1]}{g[2]}")
    print(f"{g[3]}{g[4]}{g[5]}")
    print(f"{g[6]}{g[7]}{g[8]}")


#全探索して評価値を返す
a = [[[[[[[[[0 for i9 in range(3)] for i8 in range(3)] for i7 in range(3)] for i6 in range(3)] for i5 in range(3)] for i4 in range(3)] for i3 in range(3)] for i2 in range(3)] for i1 in range(3)]   #9次元配列の作成
def all_search(input_list):
    count0 = input_list.count(0)      #要素0の数
    index0 = func(input_list)         #要素0のインデックスのリスト
    if count0 == 0:
        return win(input_list)
    if win(input_list) != 0:
        return win(input_list)
    s = 0
    for i in range(count0):                      
        l = index0[i]           #要素0のインデックス
        input_list2 = input_list.copy()  
        input_list2[l] = 2 - (count0 % 2)            #盤面の更新
        s += all_search(input_list2)
    a[input_list[0]][input_list[1]][input_list[2]][input_list[3]][input_list[4]][input_list[5]][input_list[6]][input_list[7]][input_list[8]] = s/count0
    return s / count0


#np配列をファイルに保存
def np_array(input_list):
    all_search(input_list)
    np.save('study/svd_study/three_eyes', np.array(a))        #リストをnp配列に直して保存
    return 


#np配列のロード
get_np = np.load('study/svd_study/three_eyes.npy')          #もとの評価値の配列をロード
#get_np = np.load('study/svd_study/three_eyes2.npy')       #svdした評価値の配列をロード


#与えた盤面(入力した文字列)に対する評価値を返す
def Q(input_list):
    return get_np[input_list[0]][input_list[1]][input_list[2]][input_list[3]][input_list[4]][input_list[5]][input_list[6]][input_list[7]][input_list[8]]


#softmax関数
def softmax(x):
    a = 1
    u = np.sum(np.exp(a*x))
    return np.exp(a*x) / u


#softmax関数で次の手の評価値を確率化
def prob(input_list):
    count0 = input_list.count(0)      #要素0の数
    index0 = func(input_list)         #要素0のインデックスのリスト
    s = []
    for i in range(count0):
        l = index0[i]
        input_list2 = input_list.copy()
        input_list2[l] = 2 - (count0 % 2)                 #盤面の更新
        if count0 % 2 == 0:
            s.append(Q(input_list2) * -1)         #次の手がバツのときは評価値にマイナスをつける
        else:
            s.append(Q(input_list2))
    x = np.array(s)
    y = softmax(x)
    return list(y)


#評価値に基づいて試合を進め,結果を0,1,-1で返す
def play():
    input_list = [0]*9
    for i in range(9):
        if win(input_list) != 0:
            #draw_grid(input_list)
            break
        index0 = func(input_list)
        y = random.choices(index0, k = 1, weights = prob(input_list))[0]
        input_list[y] = (i % 2) + 1 
        #draw_grid(input_list)
    return win(input_list)


#戦績を、試合を100回繰り返した平均値とした
def play100():
    s = 0
    for _ in range(100):
        s += play()
    return s / 100


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
    plt.ylabel("result")
    plt.plot(x, y)
    plt.show()


make_plot()





