"""
날짜 : 2021.08.13
학습 : SWEA D3
제목 : 1221. [S/W 문제해결 기본] 5일차 - GNS
문제 :
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

[입력]
입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.
10
#1 7041
SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE
[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다.
#1
ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO ZRO

"""

# T = int(input())
# for tc in range(1, T+1):
#     # 0~9까지 인덱스 숫자에 맞춰서 단어 입력
#     number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     empty_list = [] # 값 넣을 빈 리스트
#     no_tc, len_num = input().split() #입력값 받기
#     num_list = input().split() #단어 입력
#
#     for i in range(len(number)): #단어 순서에 맞춰서 인덱스 값 가지고 오기
#         for num in num_list: #단어 입력한것 차례로 가지고 와서
#             if number[i] == num: #number[i] 값과 num 값이 같으면
#                 empty_list += [num] #빈 리스트에 집어 넣기
#
#     print('{} {}'.format(no_tc, ' '.join(empty_list)))


T = int(input())
for tc in range(1, T+1):
    number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    empty_list = [0] * len(number)
    no_tc, len_num = input().split()
    num_list = input().split()
    result = []

    for i in range(len(number)):
        for num in num_list:
            if number[i] == num:
                empty_list[i] += 1


    for i in range(len(number)):
        if empty_list[i] != 0:
            result.append(number[i] * empty_list[i])

    print(result)

