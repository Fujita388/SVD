import numpy as np
import random
import all_search
from numba import jit

#与えた盤面(入力した文字列)に対する評価値を返す(svd)
def Q(input_list):
    get_np = np.load('study/svd_study/three_eyes2.npy')       #svdした評価値の配列をロード
    return get_np[input_list[0]][input_list[1]][input_list[2]][input_list[3]][input_list[4]][input_list[5]][input_list[6]][input_list[7]][input_list[8]]


#softmax関数
def softmax(x):
    a = 10
    u = np.sum(np.exp(a*x))
    return np.exp(a*x) / u


#softmax関数で次の手の評価値を確率化(svd)
def prob(input_list):
    count0 = input_list.count(0)      #要素0の数
    index0 = all_search.func(input_list)         #要素0のインデックスのリスト
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


#次の一手を返す
@jit
def play(input_list):
    index0 = all_search.func(input_list)    #要素0のインデックスのリスト
    count0 = input_list.count(0)            #要素0の数
    #print(prob(input_list))
    y = random.choices(index0, k = 1, weights = prob(input_list))[0]
    input_list[y] = 2 - (count0 % 2)            #盤面の更新
    #all_search.draw_grid(input_list)
    return input_list  #結果を返す

#実行
s = "000000010"
list_0 = list(map(int, list(s)))   

play(list_0)
