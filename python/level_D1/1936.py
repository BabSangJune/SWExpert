"""
날짜 : 2021.08.02
학습 : SWEA D1
제목 : 1936. 1대1 가위바위보
문제 :
A와 B가 가위바위보를 하였다.

가위는 1, 바위는 2, 보는 3으로 표현되며 A와 B가 무엇을 냈는지 입력으로 주어진다.

A와 B중에 누가 이겼는지 판별해보자. 단, 비기는 경우는 없다.

입력 :
입력으로 A와 B가 무엇을 냈는지 빈 칸을 사이로 주어진다.
3 2

출력 :
A가 이기면 A, B가 이기면 B를 출력한다.
A
"""

p1, p2 = map(int, input().split())

if p1 == 1 and p2 == 2:
    print('B')
elif p1 == 1 and p2 == 3:
    print('A')
elif p1 == 2 and p2 == 1:
    print('A')
elif p1 == 2 and p2 == 3:
    print('B')
elif p1 == 3 and p2 == 1:
    print('B')
elif p1 == 3 and p2 == 2:
    print('A')