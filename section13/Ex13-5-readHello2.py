'''
file 객체 read()함수
    read() -> 전체 읽어오기
    read(인자값) -> 인자값 크기 만큼 읽어오기
'''
file = open('Hello.txt', 'rt', encoding='UTF-8')
while True:
    str = file.read(5)
    if not str:
        break
    print(str)
file.close()