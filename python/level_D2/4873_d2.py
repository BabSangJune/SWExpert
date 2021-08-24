"""
날짜 : 2021.08.19
학습 : SWEA D2
제목 : 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
문제 :
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.

CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
CAA 연속 문자 AA를 지운다.
C 1글자가 남았으므로 1을 리턴한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
#1 1
#2 4
#3 11
"""

T = int(input()) #tc 갯수

for tc in range(1, T+1):
    arr = list(input())

    while len(arr) > 1:
        for i in range(len(arr)-1, 0, -1): #뒤에서부터 #(, -1, -1) 에러 i가 0일때 맨앞 맨뒤 같으면 삭제함

            if arr[i] == arr[i-1]: #맨뒤와 그 앞이 같으면
                arr.pop(i) #빼기
                arr.pop(i-1)
                break

        else:
            break

    print('#{} {}'.format(tc, len(arr)))
