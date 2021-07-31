A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
time_ = 0
temperature = A
while temperature < B:
  if temperature < 0:
    time_ += C
    temperature += 1
  elif temperature > 0:
    time_ += E
    temperature += 1
  else:
    time_ += D
    time_ += E
    temperature += 1
  #temperature += 1
print(time_)
