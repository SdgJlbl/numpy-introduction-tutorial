# extract the first column of a
first_column = a[:, 0]
print(first_column)
# note that the first_column is a 1D array (the first dimension has been squeezed by NumPy)
# extract the last column of a
last_column = a[:, -1]
print(last_column)
# reverse the order of the last column, using a slice with a step of -1
last_column_reversed = last_column[::-1]
print(last_column_reversed)
# stack the two columns side by side
result = np.column_stack([first_column, last_column_reversed])
print(result)
# as a one-liner
# It's cool but hard to read
print(np.column_stack([a[:, 0], a[:, -1][::-1]]))
