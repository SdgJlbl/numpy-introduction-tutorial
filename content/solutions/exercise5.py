# extracting the first column of the array
print(a[:, 0])
# for the first column, we want to pick every other value, starting from the first one
print(a[::2, 0])
# for the second column, we want to pick every other value, starting from the second one
print(a[1::2, 1])
# we stack the two columns side by side to retrieve the right order
print(np.column_stack([a[::2, 0], a[1::2, 1]]))
# unraveling the array
print(np.column_stack([a[::2, 0], a[1::2, 1]]).reshape(-1))
