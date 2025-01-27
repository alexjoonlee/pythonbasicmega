# 두 수를 입력받아서 사칙연산하는 계산기 프로그램 객체를 이용하여 작성

# 클래스 선언
class Calculator():     # 클래스 선언
    # 속성, 변수
    def __init__(self, x, y):
        self.num1 = x
        self.num2 = y

    # 기능
    def add(self):      # 입력받을 것이 있다면 self 뒤에 z, w 처럼 입력
        print('\n===add===')
        print('num1 + num2 = ', self.num1 + self.num2)
    
    def subtract(self):      # 입력받을 것이 있다면 self 뒤에 z, w 처럼 입력
        print('\n===subtract===')
        print('num1 - num2 = ', self.num1 - self.num2)
    def divide(self):      # 입력받을 것이 있다면 self 뒤에 z, w 처럼 입력
        print('\n===divide===')
        print('num1 / num2 = ', self.num1 / self.num2)
    def multiply(self):      # 입력받을 것이 있다면 self 뒤에 z, w 처럼 입력
        print('\n===multiply===')
        print('num1 * num2 = ', self.num1 * self.num2)

# 클래스 실행(사용)
# 객체 생성 : 클래스 이름(속성값 ...)
calc1 = Calculator(10,20)       # calc1 이 self 가 됨
print('\ncalc1.num1', calc1.num1)
print('calc1.num2', calc1.num2)

calc1.add()
calc1.subtract()
calc1.divide()
calc1.multiply()

calc2 = Calculator(20,60)
print('\ncalc2.num1', calc2.num1)
print('calc2.num2', calc2.num2)

calc2.add()
calc2.subtract()
calc2.divide()
calc2.multiply()



