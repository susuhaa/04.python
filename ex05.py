# For 문 
# range(시작, 끝[, 증가값 +1])


total = 0
for num in range(1, 101):  # 끝 숫자는 포함되지 않기 때문에, +1을 더해서 셋업해야 한다.
    total += num

print('tatal = ', total)





# 짝수의 합

total = 0
for num in range(2, 101, 2):
    total += num

print('total =', total)

total = 0
for num in range(1,101,2):
    total += num

print('total =', total)


# 변수값 입력하기

start = int(input('시작값:'))
end = int(input('종료값:'))

num = start
total = 0

for num in range(start, end+1):  # 끝 숫자는 포함되지 않기 때문에, +1을 더해서 셋업해야 한다.
    total += num

print(start, '~', end, '까지의 합',total)