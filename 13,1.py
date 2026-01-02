from typing import List, Optional


class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self) -> str:
        return f"Person: {self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_info()


class Student(Person):
    def __init__(self, first_name: str, last_name: str, student_ticket: str):
        super().__init__(first_name, last_name)
        self.student_ticket = student_ticket

    def get_info(self) -> str:
        return f"Student: {self.first_name} {self.last_name}, Ticket: {self.student_ticket}"


class Group:
    def __init__(self, title: str):
        self.title = title
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        if isinstance(student, Student):
            self.students.append(student)
        else:
            raise TypeError("Object must be an instance of Student")

    def search_student(self, last_name: str) -> Optional[Student]:
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str) -> bool:
        student_to_remove = self.search_student(last_name)

        if student_to_remove:
            self.students.remove(student_to_remove)
            return True
        else:
            return False

    def __str__(self) -> str:
        if not self.students:
            return f"Група {self.title} порожня."

        student_list = "\n".join([f"- {student.get_info()}" for student in self.students])
        return f"Група: {self.title}\nСтуденти:\n{student_list}"


if __name__ == "__main__":
    st1 = Student("Іван", "Петренко", "KB-123")
    st2 = Student("Марія", "Коваленко", "KB-124")
    st3 = Student("Олег", "Сидоренко", "KB-125")

    group = Group("Python-Pro")
    group.add_student(st1)
    group.add_student(st2)
    group.add_student(st3)

    print(group)

    search_result = group.search_student("Коваленко")
    print(search_result.get_info() if search_result else None)

    group.delete_student("Петренко")

    print(group)