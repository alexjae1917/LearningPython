from lesson14_.homework14_1.Human import Human


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __hash__(self):
        return hash(str(self))

    def __eq__(self,other):
        if self.age == other.age:
            return True
        return False

    def __lt__(self,other):
        if self.age < other.age:
            return True
        return False

    def __ne__(self,other):
        if self.age != other.age:
            return True
        return False

    def __gt__(self,other):
        if self.age > other.age:
            return True
        return False


    def __str__(self):
        return f'{super().__str__()} record book: {self.record_book} '
