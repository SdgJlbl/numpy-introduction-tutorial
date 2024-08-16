# create the mask of negative values
mask = a < 0
# assign 0 to all negative values
a[mask] = 0
assert np.all(a >= 0)
