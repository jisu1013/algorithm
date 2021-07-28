N = int(input())
people = []
result = 0
dasom = int(input())
for i in range(N-1):
  people.append(int(input())) 
people = sorted(people, reverse=True)
while people[0] >= dasom:
  dasom += 1
  people[0] -= 1
  result += 1
  people = sorted(people, reverse=True)
print(result)
