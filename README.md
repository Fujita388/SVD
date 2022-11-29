# Using SVD(Singular Value Decomposition) for data-approximation of Tic-Tac-Toe AI


## task1.py
	・もとの配列を(81, 243)の行列とみなしてSVD
	・関数同士を対戦させる(main.pyから読み込んだbattle()を使う)
	・戦績、フロべニウスノルムと圧縮率のグラフをプロット

## main.py
	・全探索した結果をnp配列に保存
	・task1.pyに読み込ませて、関数battle()を使う

## svd.py
	・SVDを実行するテストコード

## frobenius.py
	・フロベニウスノルムの相対誤差を算出するテストコード
