class Human:

    def init(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def str(self):
        return f'{self.first_name} {self.last_name}: {self.gender}, {self.age} years old'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.init(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.str()} record book: {self.record_book} '


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        self.group.add(student)

    def delete_student(self, last_name):
        for i in self.group:
            if i.last_name == last_name:
                return self.group.remove(i)

    def find_student(self, last_name):
        for i in self.group:
            if i.last_name == last_name:
                return i
        return None

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += f'{str(i)}\n'
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!
