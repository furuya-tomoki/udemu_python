# Numpyのアレイを利用
import numpy as np

# Pythonのリスト型から変換して作ることができる。
my_list1 = [1,2,3,4]

my_array1 = np.array(my_list1)
# Numpyのアレイを利用
import numpy as np

# Pythonのリスト型から変換して作ることができる。
my_list1 = [1,2,3,4]

my_array1 = np.array(my_list1)
# アレイを表示する
my_array1
array([1, 2, 3, 4])
# 別のアレイを作って
my_list2 = [11,22,33,44]

# リストのリストを作成
my_lists = [my_list1,my_list2]

# これを使って、多次元のアレイを作れる
my_array2 = np.array(my_lists)

my_array2
array([[ 1,  2,  3,  4],
      [11, 22, 33, 44]])
# アレイのサイズを調べる
my_array2.shape
(2, 4)
# アレイのデータ型を調べる
my_array2.dtype
dtype('int64')
# 特別なアレイを作る

#すべての要素が０
np.zeros(5)
array([ 0.,  0.,  0.,  0.,  0.])
my_zeros_array = np.zeros(5)
my_zeros_array.dtype
dtype('float64')
#すべての要素が1
np.ones((5,5))
array([[ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.],
      [ 1.,  1.,  1.,  1.,  1.]])
# 空っぽのアレイ

np.empty(5)
np.empty((3,4))
array([[  0.00000000e+000,   0.00000000e+000,   7.41098469e-323,
         0.00000000e+000],
      [  0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000],
      [  0.00000000e+000,   0.00000000e+000,   0.00000000e+000,
         0.00000000e+000]])
#単位行列I（dentity array）
np.eye(5)
array([[ 1.,  0.,  0.,  0.,  0.],
      [ 0.,  1.,  0.,  0.,  0.],
      [ 0.,  0.,  1.,  0.,  0.],
      [ 0.,  0.,  0.,  1.,  0.],
      [ 0.,  0.,  0.,  0.,  1.]])
# arange関数
np.arange(5)
array([0, 1, 2, 3, 4])
np.arange(5,50,2)
array([ 5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37,
39, 41, 43, 45, 47, 49])