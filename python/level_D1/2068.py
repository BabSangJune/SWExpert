"""
날짜 : 2021.08.06
학습 : SWEA D1
제목 : 2068. 최대수 구하기
문제 :
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.

[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
#1 99
#2 123
#3 76
"""


n = int(input())


for i in range(1, n+1):
    max_num = 0
    numbers = list(map(int, input().split()))
    for j in numbers:
        while max_num < j:
            max_num = j

    print(f'#{i} {max_num}')