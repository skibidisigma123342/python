#Создайте классы Doctor и Patient.
# Класс Doctor должен иметь атрибут `name`, а класс Patient — метод `introduce_doctor`,
# который будет выводить имя врача, переданного в качестве аргумента.
from tkinter.font import names, nametofont


class Doctor:

    def __init__(self, name):
        self.name = name


class Patient:

    def __init__(self, name):
        self.name = name


    def introduce_doctor(self, doctor):
        print(f"Hello {doctor.name}!")


doctor1 = Doctor("<Skib. Albert>")
patient1 = Patient("<Toiletor>")
patient1.introduce_doctor(doctor1)