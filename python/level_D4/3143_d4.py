"""
날짜 : 2021.08.17
학습 : SWEA D4
제목 : 3143. 가장빠른문자열타이밍
문제 :
어떤 문자열 A를 타이핑하려고 한다.
그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.
여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.
이미 타이핑 한 문자를 지우는 것은 불가능하다.
예를 들어 A=”asakusa”, B=”sa”일 때, 다음 그림과 같이 B를 두 번 사용하면 5번 만에 A를 타이핑 할 수 있다.
A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하여라.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스마다 첫 번째 줄에 두 문자열 A, B가 주어진다. A의 길이는 1이상 10,000이하, B의 길이는 1이상 100이하이다.
2
banana bana
asakusa sa
[출력]
각 테스트 케이스마다 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 출력한다.
#1 3
#2 5
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    fst_str, snd_str = input().split()
    fst_len = len(fst_str)
    snd_len = len(snd_str)
    cnt = 0

    # jump_idx = 0
    # for i in range(fst_len - snd_len + 1):
    #     # jump_idx = 0
    #     if i < (i+jump_idx):
    #         if fst_str[i+jump_idx:i+snd_len+jump_idx] == snd_str:
    #             cnt += 1
    #             jump_idx += (snd_len - 1)
    #         else:
    #             cnt += 1

    jump_idx = 0
    for i in range(fst_len - snd_len + 1): #
        # jump_idx = 0
        if fst_len <= (i + jump_idx): #글자 크기 넘어가면 break
            break
        # 같으면 카운트, index jump
        if fst_str[i + jump_idx:i + snd_len + jump_idx] == snd_str:
            cnt += 1
            jump_idx += (snd_len - 1) #snd_len 만큼
        #틀리면 카운트만
        else:
            cnt += 1


    # while jump_idx < fst_len:
    #     if fst_str[]


    print('#{} {}'.format(tc, cnt))





