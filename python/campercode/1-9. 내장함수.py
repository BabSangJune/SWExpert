'''
45.
다음의 결과와 같이 이름과 나이를 입력 받아
올해를 기준으로 100세가 되는 해를 표시하는 코드를 작성하십시오.
input> 홍길동
20
output>
홍길동(은)는 2099년에 100세가 될 것입니다.
'''
# from datetime import datetime, date

# # name = input("이름을 입력하세요.")
# name = input()
# # age = int(input("나이를 입력하세요."))
# age = int(input())
# hundyear = date(2018, 1, 1).year

# print("{}(은)는 {}년에 100세가 될 것입니다.".format(name, hundyear-age+101))

'''
46.
"ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"와
같은 문자열이 주어지고, A는 4점, B는 3점, C는 2점, D는 1점이라고 할 때 문자열에 사용된
알파벳 점수의 총합을 map 함수와 람다식을 이용해 구하십시오.
'''

# data = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
# print(sum(map(lambda x : ord('E') - ord(x), data)))

'''
47.
가변형 인자로 정수들을 입력받아 곱을 반환하는 함수를 정의하고,
단, 1, 2, '4', 3와 같이 제대로 입력되지 않은 경우 예외를 처리하는 프로그램을 작성하십시오.
output>"에러발생"
'''
# def multi(*a):
#     bnum = 1
#     for i in a:
#         if type(i) != int:
#             return "에러발생"
#         else:
#             bnum *= i
#     return bnum

# print(multi(1, 2, '4', 3))

'''
48.
ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.
input> 65
output> ASCII 65 => A
'''
# acode = int(input())
# print("ASCII {} => {}".format(acode, chr(int(acode))))

'''
49.
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
짝수만을 선택해 리스트를 반환하는 프로그램을 작성하십시오.
output> [2, 4, 6, 8, 10]
'''
# nlst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(filter(lambda x: x%2==0, nlst)))

'''
50.
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 map 함수와 람다식을 이용해
항목의 제곱 값을 갖는 리스트를 반환하는 프로그램을 작성하십시오.
output> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# nlst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x: x**2, nlst)))

'''
51.
1~10까지의 정수를 항목으로 갖는 리스트 객체에서 filter 함수와 람다식을 이용해
짝수만을 선택한 후, map 함수와 람다식을 이용해 항목의 제곱 값을 갖는 리스트를 반환하는
프로그램을 작성하십시오.
'''
# nlst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evennum = list(filter(lambda x: x%2==0, nlst))
# squarenum = list(map(lambda x: x**2, evennum))
# print(squarenum)

'''
52.
가변형 인자를 전달 받아 가장 큰 값을 반환하는 함수를 정의하고,
다음과 같은 결과를 출력하는 프로그램을 작성하십시오.
output> max(3, 5, 4, 1, 8, 10, 2) => 10
'''
# def largenum(*args):
#     return "max(3, 5, 4, 1, 8, 10, 2) => 10".format(args ,max(args))
# print(largenum(3, 5, 4, 1, 8, 10, 2))

'''
53.
다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를
값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는
프로그램을 작성하십시오.
output> 
a: 0
b: 1
c: 2
d: 3
e: 4
f: 5
'''
# word = 'abcdef'
# wdic={}
# for i, w in enumerate(word):
#     wdic[w] = i
#     print("{}: {}".format(w, i))