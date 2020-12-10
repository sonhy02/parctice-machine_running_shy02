import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.zeros((10,10)) 
print(arr1)
print(arr2)


import tensorflow._api.v2.compat.v1 as tf
tf.disable_v2_behavior()