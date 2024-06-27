from lesson13_.homework13 import Human


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def hash(self):
        return hash(str(self))

    def __str__(self):
        return f'{super().__str__()} record book: {self.record_book} '
