# computing `y` element by element
y = np.zeros(3, dtype=int)
for i in range(3):
    y[i] = np.sum(a * X[i]) + b[i]
print(y)
# vectorized version
y = np.sum(a * X, axis=1) + b
