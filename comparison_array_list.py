import numpy as np 
import time
np_array = np.arange(1, 50001)
py_list = list(range(1, 50001))
start_np = time.time()
np_sum = np.sum(np_array)
end_np = time.time()
np_time = end_np = start_np
start_py = time.time()
py_sum = sum(py_list)
end_py = time.time()
py_time = end_py - start_np

print("Numpy Sum:", np_sum)
print("Python Sum:", py_sum)

print("Numpy Time:", np_sum)
print("Python Time:", py_time)
faster = py_time / np_time
print("Numpy is", faster, "times faster than python list")