# 루프의 활용
# 반복문 continue
# 다시 루프로 돌아간다

score = [92, 86, 68, -1, 56]
for s in score:
    if s == -1:
        continue
    print(s)

print('성적 처리 끝')
 

# 올바른 데이터 (0 <= score <=)로
# 합계와 평균을 구하세요

scores = [92, 86, 68, -1 ,56, -30, 90, 140, 90]

total = 0
count = 0

for score in scores:
    if (score < 0) or (score >100):
        continue
    

    total += score
    count += 1

print('평균', round(total/count, 2))


#구구단 출력
#
#출력
#3x1 =3 ......3x9 = 27

dan = 3 

for dan in range(2,10):
    print(dan,'단')
    for hang in range(1,10):
        print(dan,' x', hang, ' =', dan*hang)

    print()


# 이중루프의 활용 2
# 레인지가 핵심!

for y in range(1,10):
    for x in range (y):
        print('*', end ='')
    print()

for y in range(9,0,-1):
    for x in range (y):
        print('*', end ='')
    print()

for y in range(1,10):
    print('*'*y) # 문자열*정수