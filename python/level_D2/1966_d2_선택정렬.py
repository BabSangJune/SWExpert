"""
날짜 : 2021.08.12
학습 : SWEA D2
제목 : 1966. 숫자정열(선택정렬)
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

# 선택 정렬로 풀기
T = int(input())

for tc in range(1, T+1):
    num_count = int(input())
    nums_list = list(map(int, input().split()))

    for i in range(len(nums_list)-1): #인덱스 가져오기(마지막 인덱스 제외)
        min = i #num_list 값중 가장 작은 숫자 인덱스 저장 할 변수

        for j in range(i+1, len(nums_list)): #i 다음 인덱스부터 마지막 인덱스까지
            if nums_list[min] > nums_list[j]: #num_list[min] 보다 num_list[j]의 값이 작으면
                min = j #min에 j를 저장

        #자리 변경
        nums_list[i], nums_list[min] = nums_list[min], nums_list[i]


    print('#{}'.format(tc), end=' ')
    print(*nums_list, sep=' ')