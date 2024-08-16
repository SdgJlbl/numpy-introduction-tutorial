import numpy as np

# option 1
result = np.zeros((3, 4))
result[:, :] = 2
result[0, -1] = 3
print(result)

# option 2
result = np.full((3, 4), 2)
result[0, -1] = 3
print(result)

# option 3 (spoiler: we'll cover `array * value` in the next chapter)
result = np.ones((3, 4)) * 2
result[0, -1] = 3
print(result)

# bad option 4: do not do that (mixing Python for-loop and NumPy -> bad performance)
result = np.zeros((3, 4))
for i in range(3):
    for j in range(4):
        if i == 0 and j == 3:
            result[i, j] = 3
        else:
            result[i, j] = 2
print(result)

# pure python option 5: this is better (create a list of list in Python, then
# move everything to NumPy in one go)
result_list = []
for i in range(3):
    result_list.append([])
    for j in range(4):
        if i == 0 and j == 3:
            result_list[i].append(3)
        else:
            result_list[i].append(2)
print(np.array(result_list))
