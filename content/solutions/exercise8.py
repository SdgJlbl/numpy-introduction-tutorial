notes = np.array([8, 7, 6, 9, 5, 4, 10])
# extracting the sorting index
sorted_indices = np.argsort(notes)
# removing the lowest and highest notes
middle_indices = sorted_indices[1:-1]
print(notes[middle_indices])
