"""
날짜 : 2021.08.10
학습 : SWEA D2
제목 : 1966. 숫자정열
문제 :
[제약 사항]
N 은 5 이상 50 이하이다.


[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어지고, 다음 줄에 N 개의 숫자가 주어진다.
10
5
1 4 7 8 0
...

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
#1 0 1 4 7 8
...
"""

#bubble
test_case = int(input())

for i in range(1, test_case+1):
    num_count = int(input())
    nums_list = list(map(int, input().split()))
    result = ''
    n = len(nums_list)

    for j in range(n-1, 0 , -1):
        for k in range(0, j):
            if nums_list[k] > nums_list[k+1]:
                nums_list[k], nums_list[k+1] = nums_list[k+1], nums_list[k]

    print('#{}'.format(i), end=' ')
    print(*nums_list, sep=' ')

#count