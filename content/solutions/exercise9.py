# A. Using a boolean mask
# we start with an array of 8 x 8, filled with zeros
checkerboard = np.zeros((8, 8))
# for rows with an even index, we fill the even columns with ones
# we do the opposite for rows with an odd index
# let's create a mask to select the even rows
even_mask = np.arange(8) % 2 == 0
print(even_mask)
# we fill the appropriate cells with ones
checkerboard[even_mask, ::2] = 1
checkerboard[~even_mask, 1::2] = 1
# checking the result
print(checkerboard)

# B. Using indexing
# we start with an array of 8 x 8, filled with zeros
checkerboard = np.zeros((8, 8))
# if I assign one row out of two to one, I get lines full of 1s because of broadcasting
checkerboard[::2] = 1
print(checkerboard)
# so I need to get every other column as well
checkerboard = np.zeros((8, 8))
checkerboard[::2, ::2] = 1
print(checkerboard)
# this is better, but it's only half of the checkerboard
# I can do the same starting at (1, 1) instead of (0, 0)
checkerboard[1::2, 1::2] = 1
# et voilà!
print(checkerboard)


# C. Using concatenation
# a checkerboard is made of two types of rows: one starting with a 1, the other starting with a 0
# let's create this pattern first
row1 = np.array([1, 0] * 4)
print("row1", row1)
# the second row is the opposite of the first one
# because 0 and 1 can be interpreted as booleans, we can use the NOT operator
row2 = np.logical_not(row1).astype(int)
print("row2", row2)
# stack these two rows to creat the pattern
pattern = np.vstack([row1, row2])
print("base pattern\n", pattern)
# repeat this pattern 4 times to get the full board
checkerboard = pattern[[0, 1] * 4]
print(checkerboard)
