'''
Создайте класс «Страна». Необходимо хранить в
полях класса: название страны, название континента,
количество жителей в стране, телефонный код страны,
название столицы, название городов страны. Реализуйте
методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса.
'''

#Инкапсуляция - возможность программы скрыть атрибуты
#класса
class Person:
    def __init__(self,FIO:str, age:int, salary:float):
        self.FIO = FIO
        self.age = age
        self.__salary = salary
    def display(self)->None:
        print(f"{self.FIO=} {self.age=} {self.__salary=}")
    def getSalary(self)->float:
        return self.__salary

objPerson1 = Person("Ivanov I.I", 25, 100000)
objPerson1.display()
#вывод данных об объекте
print(objPerson1.FIO) #атрибут открыт и мы можем его вывести
#print(objPerson1.salary) - ошибка т.к поле скрыто
#Обращение к закр.атрибуту - объект._имяКласса__имяАтрибута
print(objPerson1._Person__salary)#атрибут закрыт
print(objPerson1.getSalary())
#изменение ФИО
objPerson1.FIO = "Petrov P.P"
objPerson1.display()















#Разбор класс Дробь
class Fraction:#класс Fraction - дробь
    #numenator - числитель, denominator - знаменатель
    def __init__(self,numenator:int, denominator:int):
        self.numenator = numenator
        while denominator==0:
            print("Знаменатель не может быть равен 0.")
            denominator = int(input("Введите знаменатель:"))
        self.denominator = denominator
        print(f"Вызван метод __init__() класса Fraction")
    #метод для сложения 2ух объектов(дробей)
    def summa(self,objFr2):
        #если равны знаменатели обеих дробей
        if self.denominator==objFr2.denominator:
            print(f"{self.numenator+objFr2.numenator} "
                  f"\n --- \n "
                  f"{self.denominator}")
        else:#если неравны знаменатели обеих дробей
            # self.denominator * objFr2.numerator}"
            print(f"{self.numenator*objFr2.denominator + self.denominator * objFr2.numerator}"
                  f"\n --- \n "
                  f"{self.denominator*objFr2.denominator }")


objFr1 = Fraction(3,4)
objFr2 = Fraction(int(input("Числитель: ")),
                  int(input("Знаменатель: ")))
objFr1.summa(objFr2) #сложение дробей
