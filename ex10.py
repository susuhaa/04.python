# 반복 묻기
#exit 단어 입력되면 종료


names = ['홍길동', '고길동', '둘리', '두치']
while True:
    search_name = input('이름을 입력하세요')
    if search_name == 'exit':
       break

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

    