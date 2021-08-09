

PI = 3.14

def input_radius():
    radios_str = input("반지름을 입력하세요: ")
    return float(radios_str)

def calc_circle_area(r):
    return PI * r * r

def calc_circumference(r):
    return 2 * PI * r

radius = input_radius()
circle_area = calc_circle_area(radius)
circumferenc = calc_circumference(radius)



print("원의 면적: {0:0.2f}".format(circle_area))
print("원의 둘레: {0:0.2f}".format(circumferenc))