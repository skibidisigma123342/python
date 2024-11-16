
class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        __init__(self.message)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = 0

    def set_age(self, age):

        if age < 0 or age > 120:

            raise InvalidAgeError(f"Ошибка: летчиков лет у вас не софподает с моими {age} тоесть некорректен. Он должен быть от 0 до 120 лет.")
        self.age = age
        print(f"Возраст тебя {self.name} установлен на какикто {self.age} годика/ов.")
try:
    person = Person("Лама")
    person.set_age(-5)
except InvalidAgeError as e:

    print(e)

try:

    person2 = Person("Ламия")
    message = ("нельзя имеееееееть больше чем 119 лет, 12 месяцеф и 30 дней")
    person2.set_age(30)
except InvalidAgeError as e:()

("делал с туторам от идуса на трай и принт е, я пропустил урок пересмотрел и надеюсь вам зайдет то как я зделал код с гайдом от индуса с ломаным английским"
 )