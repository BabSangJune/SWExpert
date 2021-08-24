"""
날짜 : 2021.08.24
학습 : SWEA D4
제목 : 1224 .[S/W 문제해결 기본] 6일차 - 계산기3
문제 :
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
예를 들어
“3+(4+5)*6+7”
라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"345+6*+7+"
변환된 식을 계산하면 64를 얻을 수 있다.
문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.
이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.
피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

[입력]
각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.
총 10개의 테스트 케이스가 주어진다.

[출력]
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다.

"""

for tc in range(1, 11):
    N = int(input())
    formula = list(input())

    stack = []
    back_formula = ''

    for i in formula:

        if i == '(':  # ( 이면 죽으나 사나 stack에 쌓기
            stack.append(i)

        elif i == '+' or i == '-':  # + or - 면
            while stack and stack[-1] != '(':  # stack에 값이 있고, 우선 순위가 0인 '('가 아니라면 실행, 아니면 while stop
                back_formula += stack.pop()  # pop 하고 result에 넣기
            stack.append(i)  # while 다 돌았으면 stack에 넣기

        elif i == '*' or i == '/':  # * or / 면
            while stack and (stack[-1] == '*' or stack[-1] == '/'):  # stack 값이 있고, * or / 이라면 실행 # /,* 외 나머지 전부 저것보다 우선 순위 높음
                back_formula += stack.pop()  # pop하고  result 넣기
            stack.append(i)  # 끝나면 stack에 넣기

        elif i == ')':
            while stack and stack[-1] != '(': # 닫는 괄호가 나오면 여는 괄호가 나올때까지
                back_formula += stack.pop() #result에 쌓고
            stack.pop() #여는 괄호 버림
        else:
            back_formula += i #나머지는 숫자로 순서대로 쌓는다

    while stack: #혹시나 연산자가 남아있으면 전부 result에 쌓는다
        back_formula += stack.pop()

    result = []
    arithmetic = ['+', '-', '*', '/']
    for i in back_formula:
        if i in arithmetic:
            num2 = result.pop() #연산 순서 지켜야함 처음 뺴오는 숫자가 연산시 뒤에 있도록
            num1 = result.pop()

            if i == '*':
                result.append(num1 * num2)
            elif i == '/':
                result.append(num1 / num2)
            elif i == '+':
                result.append(num1 + num2)
            elif i == '-':
                result.append(num1 - num2)

        else:
            result.append(int(i))

    print('#{} {}'.format(tc, result[0]))



