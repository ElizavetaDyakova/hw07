# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt


class triangle:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2

    def S(self):
        return abs((((self.x1 - self.z1) * (self.y2 - self.z2) - (self.y1 - self.z1) * (self.x2 - self.z2))) * 0.5)

    def H(self):
        return round(abs((self.y2 - self.z2) * self.x1 + (self.z1 - self.y1) * self.x2 + (
                    self.y1 * self.z2 - self.z1 * self.y2)) / sqrt((self.y2 - self.z2) ** 2 + (self.z1 - self.y1) ** 2),
                     2)

    def P(self):
        return round((sqrt(abs((self.y1 - self.x1) ** 2 - (self.y2 - self.x2) ** 2)) + sqrt(
            abs((self.z1 - self.y1) ** 2 - (self.z2 - self.y2) ** 2)) + sqrt(
            abs((self.z1 - self.x1) ** 2 - (self.z2 - self.x2) ** 2))), 2)


def createPoint(n):  #создание списка координат
    listNew = []
    for f in range(n):
        print("Введите ", f + 1, "ю координату ")
        s = int(input())
        listNew.append(s)
    return (listNew)

n=6 #для треугольника
mass = createPoint(n)

tr = triangle(mass[0], mass[1], mass[2], mass[3], mass[4], mass[5])

print("Площадь треугольника равна ", tr.S())
print("Высота треугольника равна ", tr.H())
print("Периметр треугольника равен ", tr.P())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class trapeze:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.baseA = round(sqrt(abs((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)), 2)
        self.baseC = round(sqrt(abs((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)), 2)
        self.baseB = round(sqrt(abs((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)), 2)
        self.baseD = round(sqrt(abs((self.x1 - self.x4) ** 2 + (self.y1 - self.y4) ** 2)), 2)

#проверка, равнобокая или нет
    def checktrp(self):
        if (self.baseA == self.baseC) or (self.baseB == self.baseD):
            return 1
        else:
            return 0

    #длина сторон
    def lentrp(self):
        print(
            f"Длина стороны А= {self.baseA} Длина стороны B= {self.baseB} Длина стороны C= {self.baseC} Длина стороны D= {self.baseD}")

    #периметр
    def Ptrp(self):
        return print("Периметр равен", (self.baseA + self.baseB + self.baseD + self.baseC))

n = 8
mass = createPoint(n)

trp = trapeze(mass[0], mass[1], mass[2], mass[3], mass[4], mass[5], mass[6], mass[7])
if trp.checktrp == 0:
    print("Трапеция не равнобокая")
    trp.lentrp()
    trp.Ptrp()
elif trp.checktrp == 1:
    print("Трапеция равнобокая")
    trp.lentrp()
    trp.Ptrp()
else:
    print('idk((')
    trp.lentrp()
    trp.Ptrp()