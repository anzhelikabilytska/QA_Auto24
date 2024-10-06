# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент" який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, last_name, age, avg_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_grade = avg_grade
    def change_avg_grade(self, new_avg_grade):
        self.avg_grade = new_avg_grade
    def get_info(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, Avarage_grade: {self.avg_grade}"

student = Student("Jay", "Javaheri", 22, 85)

print(student.get_info())

student.change_avg_grade(95)
print(student.get_info())
