import copy
from collections import OrderedDict

info = OrderedDict();
num = 0;
number = 0;
grade = ' ';
info2 = OrderedDict();

def make():
    number = input("학번을 입력하세요 :")
    name = input("이름을 입력하세요 :")
    grade = input("학점을 입력하세요 :")
    language = input("국어 점수를 입력하세요:")
    english = input("영어 점수를 입력하세요:")
    math = input("수학 점수를 입력하세요:")
    info2["학번"] = number;
    info2["이름"] = name;
    info2["학점"] = grade;
    info2["국어"] = language;
    info2["영어"] = english;
    info2["수학"] = math;
    info[number] = copy.deepcopy(info2)
    info2.clear()
    print("등록완료")
    return 0;

def search():
    number = input("검색을 원하는 학생의 학번을 입력하세요 :")
    if info.get(number) == None:
        print("해당하는 학생이 없습니다")
    else:
        for i, k in info[number].items():
            print(i, ":", k)

def delete():
    number = input("삭제를 원하는 학생의 학번을 입력하세요 :")
    if info.get(number) == None:
        print("해당하는 학생이 없습니다")
    else:
        print(info.pop(number), "삭제 완료되었습니다")

def sort():
    for i, k in info.items():
        print(i, "학번")
        print(k)


while True:
    print("1.데이터추가\n2.데이터검색\n3.데이터삭제\n4.데이터정렬")
    print("0.종료")
    num = int(input("원하는 번호를 입력하세요 :"))
    if num == 1:
        make()

    elif num == 2:
       search()

    elif num == 3:
        delete()

    elif num == 4:
        sort()

    elif num == 0:
        print("프로그램을 종료합니다")
        break;

