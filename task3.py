# 2. 중급 문제

## 문제 3: 성적 계산 기능 추가

import random  # 랜덤함수추가
from task1 import Student  # task1에서(from) 부모클래스 import


class GradedStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.scores = []  #

    def add_score(self, score):
        self.scores.append(score)

    def calculate_average(self):
        # scores 리스트의 평균을 계산하여 반환하는 메서드를 작성하세요.
        # YOUR CODE HERE
        # 0일 경우와 아닐 경우의 분기를 정하라
        return sum(self.scores) / len(self.scores)

    def study(self, hours):
        super().study(hours)
        # 공부한 시간에 비례하여 임의의 점수를 생성하고 add_score 메서드를 호출하세요.
        # YOUR CODE HERE
        score = random.randint(1, 100)  # random.random()은 float을 배출
        self.add_score(score)


# GradedStudent 클래스의 객체를 생성하고, 여러 번 study 메서드를 호출한 후 평균 점수를 계산해보세요.
# YOUR CODE HERE

student = GradedStudent("성진", 15, 3)
student.study(2)  # 예: 2시간 공부
student.study(3)  # 예: 3시간 공부
student.study(5)  # 예: 5시간 공부


avg = student.calculate_average()
print(avg)

# 각각의 점수를 출력해 주는 것 까지 구현하면 좋을듯
