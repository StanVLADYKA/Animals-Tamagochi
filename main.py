#Симулятор жизни животного
#создать класс животные и поля: имя, возраст, вес.
#И создать методы приема пищи - при этом пользователть вводит какую пищу будет есть животное.
#При этом продумать список еды, которая будет вкусная и невкусная. Если вкусная то к весу +0,1 кг и наоборот если невкусная -0,1
#Создать метод для работы со временем. Пользователь вводит время и в зависимости от этого (игра, прогулка, кормления - по диапазону времени)
#И Продемонстрировать работу циклом, в зависиморсти от текущего времени

class Animal:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.mode = False

    def Menu(self):
        from datetime import datetime
        print("""Ввести час вручную или использовать текущее время?
        1 - ввести час вручную
        2 - использовать текущее время""")
        sel=int(input(":"))
        if sel==2:
            n = datetime.now()
            t = n.hour
        else:
            t=int(input(f"день {self.age}\nвведите час в который вы сегодня увидете {self.name} от 0 до 24\n "))


        if t==0 or t==1 or t==2 or t==3 or t==4 or t==5 or t==6 or t==7:
            self.Sleep()
        if t==8 or t==9 or t==10 or t==18 or t==19 or t==20:
            self.Food()
        if t==11 or t==12 or t==21 or t==22 or t==23:
            self.Game()
        if t==13 or t==14 or t==15 or t==16 or t==17:
            self.Walking()

    food_dic = {"мясо": 1, "сметана": 1, "консерва": 1, "сыр": 1,
                "творог": 2, "картошка": 2, "капуста": 2}
    def Game(self):
        print(f"Поиграте с {self.name}")
        self.age += 1
    def Walking(self):
        print(f"Выгуляйте {self.name}")
        self.age += 1
    def Sleep(self):
        print(f"Не тревожте {self.name}, оно сейчас спит")
        self.age += 1
    def Food(self):
        print("""Надо покормить животное, выберете еду (введите слово из списка):
         - мясо
         - сметана
         - творог
         - консерва
         - картошка
         - капуста
         - сыр""")
        f=str(input())
        try:
            if self.food_dic[f] == 1:
                self.weight += 0.1
                self.age += 1
            elif self.food_dic[f] == 2:
                self.weight += -0.1
                self.age += 1
                if self.weight <= 0.1:
                    self.mode = True
        except KeyError:
                print(f"в меню нет такой еды, сегодня {self.name} не получилось покормить")
                self.weight += -0.1
                self.age += 1
                if self.weight < 0.1:
                    self.mode = True

    def Info(self):
        print(f"У {self.name}:  возраст {self.age} дней, вес: {round((self.weight),1)} кг")


while True:
    print("Введите имя животного, к которому у вас будет доступ раз в день")
    name=input()
    age=1
    weight=0.5
    Animal1=Animal(name,age,weight)
    while True:
        Animal1.Menu()
        Animal1.Info()
        if Animal1.mode == True:
            print(f"{name} недокормлено, ,больше не увидете его.")
            break

