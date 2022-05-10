num = 151
total = 0

while num <= 300:
    total += num
    num += 2

print('total =', total)


start = int(input('시작값:'))
end = int(input('종료값:'))

num = start
total = 0

while num <= end:
    total += num
    num += 1


print(start,'~',end,'까지의 합:',total, sep='')



