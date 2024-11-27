n, m = (int(tmp) for tmp in input().split(" "))
matriz = [[0 for col in range(n)] for row in range(n)]
for k in range(m):
  i, j = (int(tmp) for tmp in input().split(" "))
  matriz[i][j] = 1
#print (matriz)
for i in range (n):
  texto = "%d: " % i
  for j in range (n):
    if (matriz[i][j] ==  1):
      texto += "%d " % j
  print (texto)