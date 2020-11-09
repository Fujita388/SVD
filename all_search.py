import numpy as np
import random


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


#全探索して評価値を返す(再帰)
a = [[[[[[[[[0 for i9 in range(3)] for i8 in range(3)] for i7 in range(3)] for i6 in range(3)] for i5 in range(3)] for i4 in range(3)] for i3 in range(3)] for i2 in range(3)] for i1 in range(3)]   #9次元配列の作成
def all_search(input_list):
    count0 = input_list.count(0)      #要素0の数
    index0 = func(input_list)         #要素0のインデックスのリスト
    if count0 == 0:                   #終端条件
        return win(input_list)
    if win(input_list) != 0:          #終端条件
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


#実行
s = "000000000"
list_0 = list(map(int, list(s)))   

#np_array(list_0)   #np配列をファイルに保存

#draw_grid(list_0)
#print(all_search(list_0))    #全探索した評価値


