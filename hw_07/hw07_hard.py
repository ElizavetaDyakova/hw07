# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import re

infoperson = []
infohours = []
info =[]
workers = open('data/workers.txt', 'r', encoding='utf-8')
for line in workers:
    infoperson.append(re.findall(r'[А-я]+[_]?[А-я]+|[0-9]+', line))
workers.close()
hours = open('data/hours_of.txt', 'r', encoding='utf-8')
for line in hours:
    infohours.append(re.findall(r'[А-я]+\s?[А-я]+|[0-9]+', line))
hours.close()
fl = open('data/price.txt', 'w', encoding='utf-8')
fl.write('Имя ----- Фамилия ----- Заработанная плата\n')
# убираем строку с названием колонок
infoperson = infoperson[1:]
infohours = infohours[1:]
for i in infoperson:
    name_one_table = i[0]
    surname_one_table= i[1]
    for n in infohours:
        name_two_table = n[0]
        surname_two_table = n[1]
        if name_one_table == name_two_table and \
            surname_one_table == surname_two_table:
            okl = int(i[2])      # оклад
            hnorm = int(i[4])  # норма отработанных часов
            hwork = int(n[2])  # отработано часов
            work = hwork - hnorm
            # Если отработано больше нормы, сверхурочную почасовую оплату считаем по двойному тарифу.
            # Если отработано меньше нормы, недоработанную почасовую оплату считаем по текущему тарифу
            if work > 0:
                price = okl + \
                        (2 * (okl / hnorm) * (hwork - hnorm))
            else:
                price = okl + \
                        (okl / hnorm) * (hwork - hnorm)
            # записываем в файл
            person_data = '{0} {1} {2:.2f}\n'.format(name_one_table,
                                                  surname_one_table,
                                                  price)
            fl.write(person_data)
            print(person_data.strip())
fl.close()
print('Зарплатная ведомость сформирована в data/price.txt')