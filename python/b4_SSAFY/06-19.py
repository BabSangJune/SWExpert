"""
날짜 : 2021.07.11
학습 : SW Expert Academy
제목 : 12차시 6. 흐름과 제어 - If
문제 : 간단한 계산기 만들기
"""

#변수 선언

operand1, operator, poerand2 = 0, "", 0

operand1 = int(input("첫 번째 숫자를 입력하세요: "))
operator = input("dustkswkfmf dlqfurgktpdy (+, -, *, /): ")
operand2 = int(input("두 번째 숫자를 입력하세요: "))

if operator == "+":
    print("%d + %d = %d " % (operand1, operand2, operand1 + operand2))
elif operator == "-":
    print("%d - %d = %d " % (operand1, operand2, operand1 - operand2))
elif operator == "*":
    print("%d * %d = %d " % (operand1, operand2, operand1 * operand2))
elif operator == "/":
    print("%d / %d = %d " % (operand1, operand2, operand1 / operand2))
else:
    print("'%s'는 본 프로그램에서 지원하지 않는 연산자 입니다." % operator)
