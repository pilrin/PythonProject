'''
open 함수 모드
    a(append mode) : 추가 모드
'''
file = open('Hello.txt', 'at', encoding='UTF-8')
file.write('Hello\n')
file.write('Nice to meet you\n')
print('Hello.txt 파일에 새로운 애용이 추가되었습니다')
file.close()