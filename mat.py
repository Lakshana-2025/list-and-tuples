A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [[0 for col in range(len(B[0]))] for row in range(len(A))]

for i in range(len(A)):

    for j in range(len(B[0])):

        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)
