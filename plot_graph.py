import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import numpy as np
import os
from datetime import timedelta
from path import Path


def time_str_to_timedelta(string_time):
    """
    Функция преобразует время из формата str в timedelta
    :param string_time: время str (hh:mm:ss)
    :return: время timedelta
    """
    list_time = string_time.split(':')
    hours_int = 0
    minutes_int = 0
    seconds_int = 0
    count_int = 0
    for t in list_time:
        t = int(t)
        if count_int == 0:
            hours_int = t
        elif count_int == 1:
            minutes_int = t
        elif count_int == 2:
            seconds_int = t
        count_int += 1

    t_from_str = timedelta(hours=hours_int, minutes=minutes_int, seconds=seconds_int)
    return t_from_str


def create_image_file( **kwargs):
    """
    Функция создаёт картинку с графиком
    :param kwargs: словарь с параметрами
    :return: создаёт файл temp_image.png в директории со скриптом
    """
    # Создаём нужные переменные
    path_default = Path("20191025.csv") # Путь до файла по умолчанию
    dict_time_main = {'5 мин': 300,
                      '10 мин': 600,
                      '20 мин': 1200,
                      '30 мин': 1800,
                      '1 час': 3600,
                      '2 часа': 7200,
                      '4 часа': 14400}
    dict_delimiter_csv = {'Запятая': ',',
                          'Точка с запятой': ';'}
    list_push1 = []
    list_x_ticks = []
    title_gr = ''
    count = 0
    flag_cycle = False

    # Входные переменные (для создания графика)
    file_path = kwargs.get("file_path", str(path_default))
    time_start_str = kwargs.get("time_start", '00:00:00')
    time_finish_str = kwargs.get("time_finish", '01:00:00')
    angle_rotation = kwargs.get("angle_rotation", 45)
    dev_major_x_key = kwargs.get("dev_major_x", '1 час')
    dev_major_x = dict_time_main.get(dev_major_x_key)
    dev_minor_x = kwargs.get("dev_minor_x", 4)
    dev_minor_y = kwargs.get("dev_minor_y", 5)
    width_px = kwargs.get("width_px", 1000)
    heigth_px = kwargs.get("heigth_px", 750)
    name_line1 = kwargs.get("name_line1", 'P 1')
    score_colomn = kwargs.get("score_colomn", 3)
    score_time = kwargs.get("score_time", -1)
    delimiter_csv_key = kwargs.get("delimiter_csv", 'Запятая')
    delimiter_csv = dict_delimiter_csv.get(delimiter_csv_key)
    bool_name_x = kwargs.get("bool_name_x", False)

    time_start = time_str_to_timedelta(time_start_str)
    time_finish = time_str_to_timedelta(time_finish_str)
    time_long = time_finish - time_start
    time_count = timedelta(seconds=time_start.total_seconds())
    time_second = timedelta(seconds=1)

    # Открываем и читаем файл
    with open(file_path, 'r') as text_csv:
        text = csv.reader(text_csv, delimiter=delimiter_csv)
        # Обходим текст файла построчно
        for line in text:
            # пробуем прочитать строку
            try:
                time_csv = time_str_to_timedelta(line[score_time])
            # если не time
            except ValueError:
                continue
            # если дошли до нужноо времени или уже начали цикл
            if time_csv == time_start or flag_cycle:
                flag_cycle = True
                # меням разделитель т.к. нужно float через точку
                value_p = line[score_colomn - 1].replace(',', '.')
                push1 = float(value_p)
                list_push1.append(push1)
                if (count % dev_major_x) == 0 and count != 0:  # при целочисленном делении нуля True
                    # если нужны все значения из файла цифра в цифру
                    if bool_name_x:
                        list_x_ticks.append(line[score_time])
                    # если нет, то считаем сами
                    else:
                        list_x_ticks.append(str(time_count))
                if count == 0:
                    title_gr += line[score_time] + ' - '
                    if bool_name_x:
                        list_x_ticks.append(line[score_time])
                    else:
                        list_x_ticks.append(str(time_count))
                if count == (time_long.total_seconds()):
                    title_gr += str(time_count)
                    flag_cycle = False
                    break
                time_count += time_second
                count += 1
            pass
    # Создаём экземпляры для линий сетки графика
    minor_locator_x = AutoMinorLocator(dev_minor_x)
    minor_locator_y = AutoMinorLocator(dev_minor_y)

    # Устанавливаем разрешение
    px = 1 / plt.rcParams['figure.dpi']
    fig, ax = plt.subplots(figsize=(width_px * px, heigth_px * px))

    # Задаём диапазон значений оси X
    ax.set(xlim=(0, time_long.total_seconds()))
    # Задаём названия осей и заголовка
    plt.xlabel('Время', fontsize=16)
    plt.ylabel('Значение давления, кгс/см2', fontsize=16)
    plt.title(title_gr, fontsize=18)
    # Задаём оси
    x_axe = ax.xaxis
    y_axe = ax.yaxis

    # Устанавливаем угол наклона меток графика
    # Ось X
    for label in x_axe.get_ticklabels(which='major'):
        label.set_rotation(angle_rotation)
        label.set_fontsize(14)
    # Ось Y
    for label in y_axe.get_ticklabels(which='major'):
        label.set_rotation(0)
        label.set_fontsize(14)
    # Задаём деления сетки графика
    x_axe.set_minor_locator(minor_locator_x)
    y_axe.set_minor_locator(minor_locator_y)

    # Устанавливаем сетку
    ax.grid(True, which='major', linestyle='solid')
    ax.grid(True, which='minor', linestyle='dashed')

    # Рисуем графики на одной оси
    line1 = ax.plot(list_push1, 'b')

    # Добавляем легенду
    list_name = [name_line1]
    plt.legend([line1], list_name, fontsize=14)

    # Создаём массив для основных меток
    arr_need_ticks = np.arange(0, time_long.total_seconds() + 1, dev_major_x)
    # Устанавливаем на оси х основные метки
    ax.set_xticks(arr_need_ticks)
    # Устанавливаем метки в соответствии со временем
    ax.set_xticklabels(list_x_ticks)
    # Удаляем предыдущий файл с графиком и создаём новый

    try:
        os.remove('temp_image.png')
    except OSError:
        fig.savefig('temp_image.png')
    fig.savefig('temp_image.png')
    plt.close()


pass

#create_image_file()
