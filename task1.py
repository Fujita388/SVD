###もとの配列を(81, 243)の行列とみなしてsvd###
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
import main


get_np = np.load('three_eyes.npy')   


#もとの評価値の配列をsvdする。同時に圧縮率とノルム誤差を返す。            r:残す特異値の数   
def approx(X, r):
	#svd#
	X = X.reshape(81, 243)
	u, s, v = linalg.svd(X)                 
	ur = u[:, :r]
	sr = np.diag(np.sqrt(s[:r]))                 #sの平方根
	vr = v[:r, :]
	A = ur @ sr
	B = sr @ vr
	#データの復元#
	Y = A @ B
	#圧縮率
	rate = (A.size + B.size) / X.size  
	#フロべニウスノルムの相対誤差
	norm = np.sqrt(np.sum(X * X))
	norm1 = np.sqrt(np.sum((X-Y) * (X-Y)))
	frob = norm1 / norm
	return [Y.reshape((3,3,3,3,3,3,3,3,3)), rate, frob]


#5回分の平均と標準偏差を算出しdatファイルを作成
def save_file():
	with open("task1.dat", "w") as f:
		for r in range(0, 82):            
			print(r)  # 進捗確認用
			#圧縮率
			x = approx(get_np, r)[1]
			#battle          
			y1 = []
			y2 = []
			y3 = []
			for _ in range(5):     #5回分のループ
				y1.append(main.battle(get_np, approx(get_np, r)[0])[0])    #originalが勝つ割合
				y2.append(main.battle(get_np, approx(get_np, r)[0])[1])    #svdが勝つ割合
				y3.append(main.battle(get_np, approx(get_np, r)[0])[2])    #引き分けの割合
			y1_m = np.mean(y1)
			y2_m = np.mean(y2)
			y3_m = np.mean(y3)
			y1_std = np.std(y1)
			y2_std = np.std(y2)
			y3_std = np.std(y3)
			#frobenius#  
			y4 = approx(get_np, r)[2]               
			f.write("{} {} {} {} {} {} {} {}\n".format(x, y1_m, y2_m, y3_m, y4, y1_std, y2_std, y3_std))


save_file()
