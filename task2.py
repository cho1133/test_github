from task1 import Student

## 문제 2: 상속을 이용한 고등학생 클래스 만들기
class HighSchoolStudent(Student):  # task1의 Student class를 상속받음.
    def __init__(self, name, age, grade, school_name):
        # super()를 사용하여 부모 클래스의 __init__ 메서드를 호출하세요.
        # YOUR CODE HERE
        super().__init__(name, age, grade) #Student의 속성을 받아옴
        self.school_name = school_name #이부분 이해 불가 -> 상속 이외(task1.py)의 속성을 초기화

    # study 메서드를 오버라이딩하여 고등학생에 맞는 메시지를 출력하세요.
    # YOUR CODE HERE
    def study(self, hours):
        print(f"{self.name}이(가) {hours}시간 동안 {self.school_name}에서 공부했습니다.")

# HighSchoolStudent 클래스의 객체를 생성하고 study 메서드를 호출해보세요.
# 이름 나이 학년 학교 = 철수 , 17 , 3 , 새싹고
# YOUR CODE HERE

cho = HighSchoolStudent("철수",17,3,"새싹고")
cho.study(5)



# task1의 문자열 출력과 현재 출력이 동시에 발생

# from task1 import Student 실행시 task1.py 가 전체 실행됨.
# 따라서 그 안에 있는 기존출력코드가 함께 출력됨

# 이 문제를 해결하려면 task1.py 파일에서 클래스 정의만 남기고 
# 객체 생성과 메서드 호출 부분을 제거하거나 
# 조건문을 사용해 직접 실행할 때만 해당 코드가 실행되도록 하면 된다.