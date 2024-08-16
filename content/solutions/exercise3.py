# we want to substract each distance to all other distances to get the pairwise distances
# for one city, we could do the operation like that
print(distances - distances[0])

# if we want to perform the same operation for all the cities at the same time, we need to switch the vector to have a column
print(distances - distances[:, np.newaxis])

# we take the absolute value of the resulting array

print(np.abs(distances - distances[:, np.newaxis]))
