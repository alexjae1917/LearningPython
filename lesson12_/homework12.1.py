class GroupQuantityError(Exception):
    msg = 'There are already 10 students in the group'


class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.gender}, {self.age} years old'


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()} record book: {self.record_book} '


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()


    def add(self, student: Student):
        if len(self.group) == 2:
            raise GroupQuantityError
        else:
            self.group.add(student)


    def add_student(self, student: Student):
        try:
            self.add(student)
        except GroupQuantityError as error:
            print(error.msg)

    def delete_student(self, last_name: str):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += f'{str(i)}\n'
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Maria', 'Ivanova', 'AN144')
gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!
