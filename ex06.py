for a in range(5):
    print('이 문장을 반복합니다')

#리스트에 성적 데이터가 있음
# #평균을 구하세요

#scores = [34,78,90,35,100,88]

#total = 0
#count = 0

#for score in scores:
   # total += score
    #count += 1

#average = total / count
    
#print('평균 =', round(average,2))


# 최소 성적을 구하세요
#리스트가 주어졌을떄(범위를 알고 있을때), 범위를 모를때는 첫번째 값을 비교 데이터로 둔다.
scores = [34,78,90,35,100,88] # 100 넘는수

total = 0
count = 0

min_score = 101   #현재 알고 있는 최고 성적
max_score = 0 

for score in scores:
    total += score
    count += 1
    if score < min_score: # 새로운 최저값이면 최저값 변경
        min_score = score

    if score >= max_score: 
        max_score = score

average = total / count
    
print('최소값 =', min_score)
print('최대값 =', max_score)
print('평균 =', round(average,2))

