n,m = map(int, input().split())
balls = list(map(int, input().split()))
array = [0] * 11
result = 0

for x in balls:
  array[x] += 1
for i in range(1, m+1):
  n -= array[i]
  result += array[i] * n

print(result)
