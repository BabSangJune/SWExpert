"""
날짜 : 2021.08.16
학습 : SWEA D2
제목 : 1979 .어디에 단어가 들어갈 수 있을까
문제 :
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

[예제]
N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때
길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.

[제약 사항]
1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)

[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.
10
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
…
[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
#1 2
#2 6
...
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    N, word_len = map(int, input().split()) #가로, 세로 길이 / 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cp_list = [] # 퍼즐 가로 세로 전체 저장 할 리스트

    for i in range(N): #가로 전부 cp_list에 저장
        empty_list = []
        for j in range(N):
            empty_list += [puzzle[i][j]]
        cp_list += [empty_list]

    for j in range(N): #세로 전부 cp_list에 저장
        empty_list = []
        for i in range(N):
            empty_list += [puzzle[i][j]]
        cp_list += [empty_list]

    result = 0
    for i in range(N+N): #cp_list 인덱스 접근 ex)N =5 면 10개
        cnt_one = 0

        for j in range(N):

            if cp_list[i][j] == 0: #0 이면 cnt_one 0으로 초기화
                cnt_one = 0

            elif cp_list[i][j] == 1: #1이면 cnt_one += 1
                cnt_one += 1

                if cnt_one == word_len:
                    result += 1

                elif cnt_one > word_len: #cnt_one word_len 이상일때
                    result -= 1 #result -1 cnt_one이 4이상일때의 3에도 result에 +1했으므로
                    cnt_one = 0 #cnt_one 초기화
                    continue #포문 돌아가기

    print('#{} {}'.format(tc, result))

