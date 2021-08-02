"""
날짜 : 2021.08.03
학습 : SWEA D1
제목 : 2050. 알파벳을 숫자로 변환
문제 :
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.


[제약 사항]
문자열의 최대 길이는 200이다.

[입력]
알파벳으로 이루어진 문자열이 주어진다.
ABCIJKLMNOPWXYZ

[출력]
각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
"""

alpha = input()
list_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# list_alpha += alpha[::1] 이렇게 받아오면 입력 순서로 받아와서 안나옴

for i in alpha:
    for j in range(len(list_alpha)):
        if i == list_alpha[j]:
            print(j+1, end=' ')