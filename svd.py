import numpy as np
from scipy import linalg


#評価値をsvd
original_np = np.load('study/svd/three_eyes.npy')
print(original_np.shape)                           #もとの行列のshape
original_np2 = original_np.reshape(81, 243)        #もとの行列をreshape
u, s, v = linalg.svd(original_np2)                 #svd
print(f"u: {u.shape}")
print(f"s: {s.shape}")
print(f"v: {v.shape}")

r = 30               #残す特異値の数   
ur = u[:, :r]
sr = np.diag(np.sqrt(s[:r]))       #sの平方根
vr = v[:r, :]
A = ur @ sr
B = sr @ vr
print(f"A: {A.shape}")           
print(f"B: {B.shape}")
print(f"AB: {(A @ B).shape}")
print(np.linalg.matrix_rank(A @ B)) 
print((A.size + B.size)/original_np2.size)      #圧縮率


#データの復元
svd_np = np.array(A @ B)
svd_np2 = svd_np.reshape((3,3,3,3,3,3,3,3,3))     #もとの配列に復元



