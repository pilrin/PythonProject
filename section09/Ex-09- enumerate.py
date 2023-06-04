'''
enumerate() 함수
     list, Tuple, Strin 등 자료형을 입력 받으면
     인덱스 값을 포함한믄 enumerate 객체를 돌려준다
'''
months = [31, 28 ,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month, day in enumerate(months):
    print('{}월 = {}일'.format(month+1, day))