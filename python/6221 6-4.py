"""
날짜 : 2021.07.11
학습 : SW Expert Academy
제목 : 6221. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 6. 흐름과 제어 - If 4
문제 : 다음의 결과와 같이 가상의 두 사람이 가위 바위 보 중 하나를 내서 승패를 가르는 가위 바위 보 게임을 작성하십시오.
이 때 ["가위", "바위", "보"] 리스트를 활용합니다.
입력 : 두 줄에 ["가위", "바위", "보"] 중 하나가 차례로 주어진다.
출력 : 첫 번째 사람은 Man1, 두 번째 사람은 Man2라고 하고, 이긴 사람의 결과를 출력한다.
예를 들어, Man1이 이겼을 경우 Result : Man1 Win! 이라고 출력한다.
단, 비긴 경우는 Result : Draw 라고 출력한다.
"""

man1 = input()
man2 = input()
case = ["가위", "바위", "보"]

if case.index(man1) < case.index(man2):
    if case.index(man1) == 0 and case.index(man2) == 2:
        print("Result : Man1 Win!")
    else:
        print("Result : Man2 Win!")
if case.index(man1) > case.index(man2):
    if case.index(man1) == 2 and case.index(man2) == 0:
        print("Result : Man2 Win!")
    else:
        print("Result : Man1 Win!")
if case.index(man1) == case.index(man2):
    print("Result : Draw")