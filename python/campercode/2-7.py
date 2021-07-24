# 44

class Student:
    def sum(self, scores):
        return "국어, 영어, 수학의 총점: {0}".format(sum(scores))


nums = [int(i) for i in input().split(',')]
print(Student().sum(nums))

# 45

class Korean:
    def printNationality(self):
        return "대한민국"


print(Korean.printNationality(1))
print(Korean.printNationality(1))


# 46
# 객체지향 3

class Student:

    def __init__(self, student_name):
        self.student_name = student_name

    def Print(self):
        print(f"이름: {self.student_name}")

class GraduateStudent(Student):

    def __init__(self, student_name, student_major):
        super(GraduateStudent, self).__init__(student_name)
        self.student_major = student_major

    def Print(self):
        print(f"이름: {self.student_name}, 전공: {self.student_major}")


student = Student("홍길동")
graduatestudent = GraduateStudent("이순신", "컴퓨터")

student.Print()
graduatestudent.Print()


# 47


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        print("원의 면적: {0:0.2f}".format(3.14 * (self.r) ** 2))


circle = Circle(2)

circle.area()


# 48

class Rectangle:
    def __init__(self, w, h):
        self.area = w * h

    def PrintArea(self):
        print(f"사각형의 면적: {self.area}")


rectangle = Rectangle(4, 5)

rectangle.PrintArea()


# 49

class Shape:

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


square = Square(3)

print(f"정사각형의 면적: {square.area()}")


# 50


class Person:

    def getGender(self):
        return "Unknown"


class Male(Person):

    def getGender(self):
        return "Male"


class Female(Person):

    def getGender(self):
        return "Female"


p1 = Male()
p2 = Female()

print(p1.getGender())
print(p2.getGender())
