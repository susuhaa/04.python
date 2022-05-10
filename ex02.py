

# 이 소스 구조를 활용해서
#홀수의 합과 짝수의 합을 구해 출력하세요

num = 1
even_total = 0
odd_tatal = 0

while num <= 100:
  if num % 2 == 0: 
    even_total += num
  
  else
    odd_tatal += num 
  
  num += 1   

print('짝수의 합', even_total)