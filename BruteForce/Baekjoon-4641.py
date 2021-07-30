while True:
  result = 0
  num_list = list(map(int, input().split()))
  if num_list[0] == -1:
    break
  else:
    num_list = sorted(num_list[:len(num_list)-1])
    for i in range(len(num_list)):
      for j in range(i, len(num_list)):
        if num_list[j] == (num_list[i]*2):
          result += 1
          break
    print(result)  
