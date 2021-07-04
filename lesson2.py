import numpy as np
import numpy as np
5/2
2.5
from __future__ import division
# Python2を使っている場合は、5/2が2にならないように、以下の1行を実行
from __future__ import division
# アレイを作る
arr1 = np.array([[1,2,3,4],[8,9,10,11]])

arr1
array([[ 1,  2,  3,  4],
      [ 8,  9, 10, 11]])
# アレイのかけ算
arr1*arr1
array([[  1,   4,   9,  16],
      [ 64,  81, 100, 121]])
# 引き算
arr1-arr1
array([[0, 0, 0, 0],
      [0, 0, 0, 0]])
# 1をアレイの書く要素で割ってみる
1 / arr1
array([[ 1.        ,  0.5       ,  0.33333333,  0.25      ],
      [ 0.125     ,  0.11111111,  0.1       ,  0.09090909]])
# 累乗（べき乗）を計算
arr1 ** 3
array([[   1,    8,   27,   64],
      [ 512,  729, 1000, 1331]])