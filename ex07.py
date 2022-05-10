#반복문을 벗어나게 하는 break

score = [92, 86 ,68 ,120, 56]
for s in score:
    if(s < 0) or (s > 100):
        break
    print(s)

print('성적 처리 끝')


# 문제
# 사용자로 부터 이름을 입력 받아
# 리스트에 이름이 있는지 여부를 판단하세요


names = ['홍길동', '고길동', '둘리', '두치']

search_name = input('이름을 입력하세요')
search_result = False

for name in names:
     if name == search_name: #ture 찾음
        search_result = True 
        break

print('결과:', search_result )


# 찾았으면 몇번째 있는지 출력하고,
# 없다면 xxx는 목록에 없습니다. 출력


names = ['홍길동', '고길동', '둘리', '두치']

search_name = input('이름을 입력하세요')
search_result = False
index = 0     #첫번째를 의미
for name in names:

    if name == search_name: #ture 찾음
        search_result = True 
        break
    index += 1

if search_result:
    print(search_name,'은',(index+1),'번째에 있습니다')
else:
    print(search_name, '은 목록에 없습니다')