import numpy as np

# create a range of values between 1 and 12
a = np.arange(1, 13)
print(a)
# we want to separate the odd and the even values, that means taking one value out of two
# we will reshape the array to have 2 columns
b = a.reshape(-1, 2)
print(b)
# it looks like almost what we want, but we want the odd and even values to be in the same row respectively, not the same column
# we need to transpose the array to get to the result we want
c = b.T
print(c)
