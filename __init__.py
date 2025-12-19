n = int(input())
matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

summa = 0
for i in range(n):
    summa += matrix[i][i]
print(summa)
