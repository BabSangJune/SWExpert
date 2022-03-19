import sys

sys.stdin = open("test.txt", "r")

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for j in range(len(arr[0])):
        empty_lst = []
        for i in range(len(arr)):
            if arr[i][j] == 1 or arr[i][j] == 2:
                empty_lst += [arr[i][j]]

        for i in range(len(empty_lst)-1):
            if empty_lst[i] == 1 and empty_lst[i+1] == 2:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
