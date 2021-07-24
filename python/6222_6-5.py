"""
날짜 : 2021.07.12
학습 : SW Expert Academy
제목 : 6222. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 5
문제 : 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,
알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
출력 시 아스키코드를 함께 출력합니다.
입력 : c
출력 : c(ASCII: 99) => C(ASCII: 67)
"""

a = input()

if ord(a) > 96 and ord(a) < 123 : #소문자를 대문자로
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(a, ord(a), a.upper(), ord(a.upper())))

elif ord(a) > 64 and ord(a) < 91 : #대문자를 소문자로
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(a, ord(a), a.lower(), ord(a.lower())))

else :
    print(a)