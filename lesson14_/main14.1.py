from lesson14_.homework14_1 import Student, Group

if __name__ == '__main__':
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')
    gr.add_student(st1)
    gr.add_student(st2)
    print(gr)
    assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
    assert gr.find_student('Jobs2') is None, 'Test2'
    assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
    assert st1 > st2, 'Test3'
    assert st2 < st1, 'Test4'
    assert not st1 == st2, 'Test5'
    assert st1 != st2, 'Test6'

    gr.delete_student('Taylor')
    print(gr)  # Only one student
    gr.delete_student('Taylor')  # No error!
