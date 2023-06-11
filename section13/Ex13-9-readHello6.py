import sys

with open('Hello.txt', 'rt', encoding='UTF-8') as file:
    line_list = file.readlines()
    sys.stdout.writelines(line_list)