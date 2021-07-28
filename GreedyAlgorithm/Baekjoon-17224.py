N, L, K = map(int, input().split())
tasks = []
for i in range(N):
  tasks.append(list(map(int, input().split())))
tasks = sorted(tasks, key=lambda x:x[1])
result = 0
cnt = 0
index = 0
while True:
  if index == N:
    break
  if cnt == K:
    break
  if tasks[index][0] < L or tasks[index][0] == L:
    if tasks[index][1] < L or tasks[index][1] == L:
      result += 140
      cnt += 1
    else:
      result += 100
      cnt += 1
  index += 1
print(result)
