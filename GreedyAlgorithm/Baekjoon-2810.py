N = int(input())
seats = input()
cnt = 0
i = 0
while i < len(seats):
    if seats[i] == 'S':
        cnt += 1
        i += 1
    else:
        cnt += 1
        i += 2
if N < (cnt+1):
    print(N)
else:
    print(cnt+1)
