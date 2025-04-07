class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"ФИО: {self.full_name}")
        print(f"Возраст: {self.age}")
        print(f"Женат/Замужем: {'Да' if self.is_married else 'Нет'}")


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def introduce_myself(self):
        super().introduce_myself()
        print("Оценки:")
        for subject, mark in self.marks.items():
            print(f" - {subject}: {mark}")
        print(f"Средний балл: {self.average_mark():.2f}")


class Teacher(Person):
    base_salary = 50000  # базовая зарплата

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus_years = max(0, self.experience - 3)
        bonus = self.base_salary * 0.05 * bonus_years
        return self.base_salary + bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Стаж: {self.experience} лет")
        print(f"Зарплата: {self.calculate_salary():.2f} руб.")


# 8. Создание учителя и вывод информации
teacher = Teacher("Иван Иванов", 40, True, 7)
print("Информация об учителе:")
teacher.introduce_myself()
print()

# 9. Функция создания учеников
def create_students():
    student1 = Student("Алина Смирнова", 16, False, {"Математика": 5, "Физика": 4, "Химия": 5})
    student2 = Student("Борис Козлов", 17, False, {"Математика": 3, "Физика": 4, "Химия": 3})
    student3 = Student("Галина Орлова", 16, False, {"Математика": 5, "Физика": 5, "Химия": 5})
    return [student1, student2, student3]

# 10. Вывод информации о каждом студенте
students = create_students()
print("Информация об учениках:")
for student in students:
    student.introduce_myself()
    print()
