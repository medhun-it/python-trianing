n = int(input())
if n==0 :
  print("1")
else:
  count = 0
  
  while n > 0:
      last = n % 10
      if last == 0:
          count += 1
      n = n // 10
  
  print(count)
