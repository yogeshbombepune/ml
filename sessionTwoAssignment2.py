# matrix multiplication

x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

# result is 3x4
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
            
# result is 3x4
result = [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*y)] for X_row in x]

for r in result:
    print(r)
