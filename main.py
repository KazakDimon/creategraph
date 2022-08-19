import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import timedelta
import plot_graph


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        size_policy_widgets = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        alignment_widgets = QtCore.Qt.AlignLeft
        # Задаём размер окна
        # self.setMaximumSize(1131, 724)
        # Устанавливаем поле главного шаблона
        self.h_box_main = QtWidgets.QHBoxLayout()
        self.h_box_main.setSpacing(5)
        self.v_box_all_properties = QtWidgets.QVBoxLayout()

        # Создаём верт.слой для GroupBox
        self.v_box_prop_graph = QtWidgets.QVBoxLayout()

        # Создаём надпись и выподающий список и гор.слой
        self.label_main_dev = QtWidgets.QLabel('Основные деления:')
        self.label_main_dev.setToolTip('Число основных делений графика на оси Х')
        self.combo_box_dev = QtWidgets.QComboBox()
        self.combo_box_dev.setToolTip('Период основных делений графика')
        self.combo_box_dev.addItems(['5 мин', '10 мин', '20 мин', '30 мин',
                                     '1 час', '2 часа', '4 часа'])
        self.h_line_dev = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_main_dev.setSizePolicy(size_policy_widgets)
        self.combo_box_dev.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_dev.addWidget(self.label_main_dev, alignment=alignment_widgets)
        self.h_line_dev.addWidget(self.combo_box_dev, alignment=alignment_widgets)

        # Создаём надпись, SpinBox и гор.слой
        self.label_add_div_x = QtWidgets.QLabel('Дополнительные деления Х:')
        self.label_add_div_x.setToolTip('Промежуточные деления между основными')
        self.spin_add_div_x = QtWidgets.QSpinBox()
        self.spin_add_div_x.setToolTip('от 1 до 10')
        self.spin_add_div_x.setRange(1, 10)
        self.spin_add_div_x.setValue(5)
        self.h_line_div_x = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_add_div_x.setSizePolicy(size_policy_widgets)
        self.spin_add_div_x.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_div_x.addWidget(self.label_add_div_x, alignment=alignment_widgets)
        self.h_line_div_x.addWidget(self.spin_add_div_x, alignment=alignment_widgets)

        # Создаём надпись, SpinBox и гор.слой
        self.label_add_div_y = QtWidgets.QLabel('Дополнительные деления Y:')
        self.label_add_div_y.setToolTip('Промежуточные деления между основными')
        self.spin_add_div_y = QtWidgets.QSpinBox()
        self.spin_add_div_y.setToolTip('от 1 до 10')
        self.spin_add_div_y.setRange(1, 10)
        self.spin_add_div_y.setValue(5)
        self.h_line_div_y = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_add_div_y.setSizePolicy(size_policy_widgets)
        self.spin_add_div_y.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_div_y.addWidget(self.label_add_div_y, alignment=alignment_widgets)
        self.h_line_div_y.addWidget(self.spin_add_div_y, alignment=alignment_widgets)

        # Создаём надпись, редактор текста и гор.слой
        self.label_name_graph = QtWidgets.QLabel('Название:')
        self.label_name_graph.setToolTip('Имя графика на рисунке')
        self.text_edit_name = QtWidgets.QLineEdit()
        self.text_edit_name.setMaximumSize(150, 20)
        self.text_edit_name.setMaxLength(15)
        self.h_line_name_graph = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_name_graph.setSizePolicy(size_policy_widgets)
        self.text_edit_name.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_name_graph.addWidget(self.label_name_graph, alignment=alignment_widgets)
        self.h_line_name_graph.addWidget(self.text_edit_name, alignment=alignment_widgets)

        # Создаём надпись, SpinBox и гор.слой
        self.label_rotation_x = QtWidgets.QLabel('Угол поворота Х:')
        self.label_rotation_x.setToolTip('Угол поворота значений на оси Х')
        self.spin_rotation_x = QtWidgets.QSpinBox()
        self.spin_rotation_x.setToolTip('От 0 до 30 градусов')
        self.spin_rotation_x.setRange(0, 30)
        self.h_line_rotation_x = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_rotation_x.setSizePolicy(size_policy_widgets)
        self.spin_rotation_x.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_rotation_x.addWidget(self.label_rotation_x, alignment=alignment_widgets)
        self.h_line_rotation_x.addWidget(self.spin_rotation_x, alignment=alignment_widgets)

        self.check_box_real_name_x = QtWidgets.QCheckBox('Реальные значения на оси Х?')
        self.check_box_real_name_x.setToolTip('Те значения которые указаны в файле\n' + \
                                              '(приборы могут пропускать секунды)')
        # Устанвливаем политику изменения размеров виджетов
        self.check_box_real_name_x.setSizePolicy(size_policy_widgets)

        # Добавляем строки на верт.слой настроек
        self.v_box_prop_graph.addLayout(self.h_line_dev)
        self.v_box_prop_graph.addLayout(self.h_line_div_x)
        self.v_box_prop_graph.addLayout(self.h_line_div_y)
        self.v_box_prop_graph.addLayout(self.h_line_name_graph)
        self.v_box_prop_graph.addLayout(self.h_line_rotation_x)
        self.v_box_prop_graph.addWidget(self.check_box_real_name_x, alignment=alignment_widgets)

        # Создаём GroupBox для настройки графика
        self.group_box_prop_graph = QtWidgets.QGroupBox('Настройки графика')
        # Добавляем верт.слой для настроек
        self.group_box_prop_graph.setLayout(self.v_box_prop_graph)

        # Следующий GroupBox
        # Создаём верт.слой для GroupBox
        self.v_box_prop_image = QtWidgets.QVBoxLayout()

        # Создаём надпись, SpinBox и гор.слой
        self.label_wight_pix = QtWidgets.QLabel('Ширина в пикс:')
        self.spin_wight_pix = QtWidgets.QSpinBox()
        self.spin_wight_pix.setToolTip('От 400 до 1200')
        self.spin_wight_pix.setRange(400, 1200)
        self.spin_wight_pix.setValue(800)
        self.h_line_wight = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_wight_pix.setSizePolicy(size_policy_widgets)
        self.spin_wight_pix.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_wight.addWidget(self.label_wight_pix, alignment=alignment_widgets | QtCore.Qt.AlignTop)
        self.h_line_wight.addWidget(self.spin_wight_pix, alignment=alignment_widgets | QtCore.Qt.AlignTop)

        # Создаём надпись, SpinBox и гор.слой
        self.label_height_pix = QtWidgets.QLabel('Высота в пикс:')
        self.spin_height_pix = QtWidgets.QSpinBox()
        self.spin_height_pix.setToolTip('От 300 до 800')
        self.spin_height_pix.setRange(300, 800)
        self.spin_height_pix.setValue(600)
        self.h_line_height = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_height_pix.setSizePolicy(size_policy_widgets)
        self.spin_height_pix.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_height.addWidget(self.label_height_pix, alignment=alignment_widgets | QtCore.Qt.AlignTop)
        self.h_line_height.addWidget(self.spin_height_pix, alignment=alignment_widgets | QtCore.Qt.AlignTop)

        # Добавляем строки на верт.слой настроек
        self.v_box_prop_image.addLayout(self.h_line_wight)
        self.v_box_prop_image.addLayout(self.h_line_height)

        # Создаём GroupBox для настройки графики
        self.group_box_prop_image = QtWidgets.QGroupBox('Настройки изображения')
        self.group_box_prop_image.setLayout(self.v_box_prop_image)

        # Следующий GroupBox
        # Создаём верт.слой для GroupBox
        self.v_box_prop_file = QtWidgets.QVBoxLayout()

        # Создаём надпись, TimeEdit и гор.слой
        self.label_time_start = QtWidgets.QLabel('Время начала:')
        self.time_edit_time_start = QtWidgets.QTimeEdit()
        self.time_edit_time_start.setDisplayFormat('hh:mm:ss')
        self.h_line_time_start = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_time_start.setSizePolicy(size_policy_widgets)
        self.time_edit_time_start.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_time_start.addWidget(self.label_time_start, alignment=alignment_widgets)
        self.h_line_time_start.addWidget(self.time_edit_time_start, alignment=alignment_widgets)

        # Создаём надпись и TimeEdit и гор.слой
        self.label_time_finish = QtWidgets.QLabel('Время окончания')
        self.time_edit_time_finish = QtWidgets.QTimeEdit()
        self.time_edit_time_finish.setDisplayFormat('hh:mm:ss')
        self.h_line_time_finish = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_time_finish.setSizePolicy(size_policy_widgets)
        self.time_edit_time_finish.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_time_finish.addWidget(self.label_time_finish, alignment=alignment_widgets)
        self.h_line_time_finish.addWidget(self.time_edit_time_finish, alignment=alignment_widgets)

        # Создаём надпись, SpinBox и гор.слой
        self.label_score_colomn = QtWidgets.QLabel('Колонка значений:')
        self.label_score_colomn.setToolTip('Вертикальая колонка, где находится целевое значение')
        self.spin_score_colomn = QtWidgets.QSpinBox()
        self.spin_score_colomn.setToolTip('От 0 до 30')
        self.spin_score_colomn.setRange(1, 30)
        self.h_line_score_colomn = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_score_colomn.setSizePolicy(size_policy_widgets)
        self.spin_score_colomn.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_score_colomn.addWidget(self.label_score_colomn, alignment=alignment_widgets)
        self.h_line_score_colomn.addWidget(self.spin_score_colomn, alignment=alignment_widgets)

        # Создаём надпись, SpinBox и гор.слой
        self.label_score_time = QtWidgets.QLabel('Колонка времени:')
        self.label_score_time.setToolTip('Вертикальая колонка, где находится значение времени\n' + \
                                         '(нужно указывать значение минус 1 т.е. если колонка 2, то значение 1)')
        self.spin_score_time = QtWidgets.QSpinBox()
        self.spin_score_time.setToolTip('От -1 до 30\n' + '(-1 соответствует последней колонке в файле)')
        self.spin_score_time.setRange(-1, 30)
        self.spin_score_time.setValue(-1)
        self.h_line_score_time = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_score_time.setSizePolicy(size_policy_widgets)
        self.spin_score_time.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_score_time.addWidget(self.label_score_time, alignment=alignment_widgets)
        self.h_line_score_time.addWidget(self.spin_score_time, alignment=alignment_widgets)

        # Создаём надпись и выподающий список и гор.слой
        self.label_delimit_csv = QtWidgets.QLabel('Разделитель:')
        self.label_delimit_csv.setToolTip('Разделитель можно посмотреть, открыв файл в текстовом редакторе')
        self.combo_box_delimit_csv = QtWidgets.QComboBox()
        self.combo_box_delimit_csv.addItems(['Запятая', 'Точка с запятой'])
        self.h_line_delimit_csv = QtWidgets.QHBoxLayout()
        # Устанвливаем политику изменения размеров виджетов
        self.label_delimit_csv.setSizePolicy(size_policy_widgets)
        self.combo_box_delimit_csv.setSizePolicy(size_policy_widgets)
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_delimit_csv.addWidget(self.label_delimit_csv, alignment=alignment_widgets)
        self.h_line_delimit_csv.addWidget(self.combo_box_delimit_csv, alignment=alignment_widgets)

        # Добавляем строки на верт.слой настроек файла
        self.v_box_prop_file.addLayout(self.h_line_time_start)
        self.v_box_prop_file.addLayout(self.h_line_time_finish)
        self.v_box_prop_file.addLayout(self.h_line_score_colomn)
        self.v_box_prop_file.addLayout(self.h_line_score_time)
        self.v_box_prop_file.addLayout(self.h_line_delimit_csv)

        # Создаём GroupBox для настройки файла
        self.group_box_prop_file = QtWidgets.QGroupBox('Настройки файла')
        self.group_box_prop_file.setLayout(self.v_box_prop_file)

        # Создаём кнопки открытия файла и создания графика
        self.btn_open_file = QtWidgets.QPushButton('Открыть файл')
        self.btn_open_file.clicked.connect(self.get_file_dir_image)
        self.btn_open_file.setMinimumSize(220, 30)
        self.btn_create_graph = QtWidgets.QPushButton('Построить график')
        self.btn_create_graph.setToolTip('Если график не отобразился попробуйте сменить разделить\nГрафик лежит в папке с программой')
        self.btn_create_graph.clicked.connect(self.create_image)
        self.btn_create_graph.setMinimumSize(220, 30)

        # Добавляем виджеты групп настроек и кнопки на главный вер.слой
        self.v_box_all_properties.addWidget(self.group_box_prop_graph)
        self.v_box_all_properties.addWidget(self.group_box_prop_image)
        self.v_box_all_properties.addWidget(self.group_box_prop_file)
        self.v_box_all_properties.addWidget(self.btn_open_file, alignment=QtCore.Qt.AlignRight)
        self.v_box_all_properties.addWidget(self.btn_create_graph, alignment=QtCore.Qt.AlignRight)

        # Устанавливаем график
        # Загружаем картинку
        self.image_graph = QtGui.QPixmap()
        self.image_graph.load('temp_image.png')
        # Ставим сцену
        self.sienna = QtWidgets.QGraphicsScene()
        # Добавляем картинку на сцену
        self.sienna.addPixmap(self.image_graph)
        # Добавляем поле просмотра сцены
        self.view_scene = QtWidgets.QGraphicsView()
        # Добаляем сцену на поле
        self.view_scene.setScene(self.sienna)
        # Показываем наше поле просмотра
        self.view_scene.show()
        # Добаляем поле просмотра и кнопку на главное окно
        self.h_box_main.addWidget(self.view_scene)
        self.h_box_main.addLayout(self.v_box_all_properties)
        self.setLayout(self.h_box_main)

        # Создаём переменную для хранения пути csv-файла
        self.dir_csv_file = ''

    def create_image(self):
        """
        Функция создаёт график и задаёт условия для вывода
        окон предуреждения, использет модуль plot_graph
        :return: temp_image.png
        """
        # Создаём переменные и находим их разницу для проверки указанного user периода времени
        # (время в начале периода не должно быть больше чем время в конце)
        time_st_for_compare = self.time_str_to_timedelta(self.time_edit_time_start.time().toString('HH:mm:ss'))
        time_fh_for_compare = self.time_str_to_timedelta(self.time_edit_time_finish.time().toString('HH:mm:ss'))
        delta_time_start_finish = time_fh_for_compare - time_st_for_compare
        # Если указана дирректория и правельный период времени, то строим график
        if not (self.dir_csv_file == '') and delta_time_start_finish.total_seconds() > 0:
            plot_graph.create_image_file(file_path=self.dir_csv_file,
                                         time_start=self.time_edit_time_start.time().toString('HH:mm:ss'),
                                         time_finish=self.time_edit_time_finish.time().toString('HH:mm:ss'),
                                         angle_rotation=self.spin_rotation_x.value(),
                                         bool_name_x=self.check_box_real_name_x.isChecked(),
                                         dev_major_x=self.combo_box_dev.currentText(),
                                         dev_minor_x=self.spin_add_div_x.value(),
                                         dev_minor_y=self.spin_add_div_y.value(),
                                         width_px=self.spin_wight_pix.value(),
                                         heigth_px=self.spin_height_pix.value(),
                                         name_line1=self.text_edit_name.text(),
                                         score_colomn=self.spin_score_colomn.value(),
                                         score_time=self.spin_score_time.value(),
                                         delimiter_csv=self.combo_box_delimit_csv.currentText())
            # Очищаем графическую сцену и кэш
            self.sienna.clear()
            QtGui.QPixmapCache.clear()
            # Загружаем график, добавляем на сцену, обновляем поле просмотра
            self.image_graph.load('temp_image.png')
            self.sienna.addPixmap(self.image_graph)
            self.view_scene.update()
        # Если директория не указана, то выводится предупреждение
        elif self.dir_csv_file == '':
            QtWidgets.QMessageBox.information(self, 'Ошибка!', "Файл .CSV не открыт!")
        # Если период времени указан user неверно, то выводится предупреждение
        elif delta_time_start_finish.total_seconds() <= 0:
            QtWidgets.QMessageBox.information(self, 'Ошибка!',
                                              "Время начала не может быть больше или равно времени окончания!")
        pass

    def get_file_dir_image(self):
        """
        Функция вызывает окно для указания директории csv-файла
        пользователем
        :return: path в формате str
        """
        # Создаём окно для выбора директории
        dir_name_csv = QtWidgets.QFileDialog.getOpenFileName(self, caption='Set file CSV', filter='Exes (*.csv)')
        self.dir_csv_file = dir_name_csv[0]
        print(self.dir_csv_file)
        pass

    def resizeEvent(self, e):
        """
        Перегрузка метода для отладки
        :param e: событие метода resizeEvent
        :return:
        """
        # print(e.size())
        # print(self.check_box_real_name_x.isChecked())
        pass

    @staticmethod
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



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my_window = Window()
    my_window.move(my_window.width() * -2, 0)
    my_window.show()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - my_window.frameSize().width()) // 2
    y = (desktop.height() - my_window.frameSize().height()) // 2
    my_window.move(x, y)
    sys.exit(app.exec_())
