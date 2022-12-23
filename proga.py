#Рассчёт григорианской даты:
def gr_date(filter_star_size):
    total = []
    for i in filter_star_size:
        a = float(i[0]) + + 32082
        b = (4 * a + 3) // 146097
        c = a - (146097 * b) // 4
        d = (4 * c + 3) // 1461
        e = c - (1461 * d) / 4
        m = (5 * e + 2) // 153
        day = e - (153 * m + 2) / 5 + 1
        month = m + 3 - 12 * (m / 10)
        year = 100 * b + d - 4800 + m / 10
        hour = (float(i[0])) % 1 * 60
        minute = (hour % 1 * 60)
        second = (minute % 1 * 60)
        Date = int(day), int(month), int(year), int(hour), int(minute), int(second)
        total.append(Date)
    return total #Оператор содержит наше вычисленное выражение

'''     def - это функция. Она нужна, чтобы для каждого фильтра не дублировать код. Делает дату григорианской.
        Мы передаём в неё список, она его обрабатывает и возвращает. Кортежи являются неизменяемыми списками.
        Это значит, что после создания кортежа хранимые в нем значения нельзя удалять или менять. Добавлять новые также нельзя.
        По сути функцию мы можем вызывать сколько угодно раз для данных.
        Оператор return используется, чтобы прервать выполнение функции и вернуться в ту часть кода, откуда была вызвана функция.
                                                                             '''

path ='C:/Users/aga00/OneDrive/Рабочий стол/task2_data.txt'
with open(path, encoding="utf-8") as file:
    object=[]
    for i in file:
        objects=i.split()
        object.append(objects[0])
    object=set(object)
    object.remove('rz_lyr')
    object.remove('Object')
    print('Доступные объекты',object)
with open(path, encoding="utf-8") as file:
    for head in file:
        header = head
        break
    result = {}
    for star in file:
        obj, HJD, filter_c, magnitude = star.split()  # элементы списка, которые заносим в словарь result
        obj = obj.lower()
        HJD = "24" + HJD
        result.setdefault(obj, {}).setdefault(filter_c, []).append((HJD, magnitude))

'''

        result.setdefault(obj, {}).setdefault(filter_c, []).append((HJD, magnitude))
        словарь.setdefault(ключ, []).append(значение)
        setdefault смотрит, если ключа нет, то создаёт его, если есть, и там пустой список, то добавляет в него значение
        Идея кода сверху создать пустой словарь, создать элементы списка и заполнить наш словарь этими элементами.
        Дальше мы и будем с ним работать. Мы получим что нашим значениям соответствует фильтр и объект. ^_^

                                                                             '''
obj = input().lower()
if obj == 'su_hor':
    print('Объект', obj, 'В фильтрах: V, B, Ic')
else:
    print('Объект', obj, 'В фильтрах: V, B')
filter_obj = result[obj]
filters_user_input = input().split()
#Создание файла
fileee = open(f'{obj}.txt', 'w+')
for filter_input in filters_user_input:
    data = filter_obj[filter_input]
    d = gr_date(data)
    print(d)
    fileee.write(f'Filter {filter_input} \n')
    fileee.write(f'\t  Gregorian_date \t \t \t \t \t \t \t \t HJD \t \t \t \t \t Magnitude \n')
    for num, obj_gr_star in enumerate(data): #Делаем счётчик количества элементов в последовательности.
        fileee.write(f'{d[num]} \t \t \t \t \t \t {obj_gr_star[0]} \t \t \t \t    {obj_gr_star[1]} \n ')
