import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import plot_graph


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        # Задаём размер окна
        # self.setMaximumSize(1131, 724)
        # Устанавливаем поле главного шаблона
        self.h_box_main = QtWidgets.QHBoxLayout()
        self.h_box_main.setSpacing(5)
        self.v_box_all_properties = QtWidgets.QVBoxLayout()

        # Создаём верт.слой для GroupBox
        self.v_box_prop_graph = QtWidgets.QVBoxLayout()

        # Создаём надпись и выподающий список и гор.слой
        self.label_main_dev = QtWidgets.QLabel('Main division, sec :')
        self.combo_box_dev = QtWidgets.QComboBox()
        self.combo_box_dev.addItems(['300', '600', '1200',
                                     '2400', '1800', '3600',
                                     '7200', '14400'])
        self.h_line_dev = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_dev.addWidget(self.label_main_dev)
        self.h_line_dev.addWidget(self.combo_box_dev)

        # Создаём надпись, SpinBox и гор.слой
        self.label_add_div_x = QtWidgets.QLabel('Additional division X :')
        self.spin_add_div_x = QtWidgets.QSpinBox()
        self.spin_add_div_x.setRange(0, 10)
        self.spin_add_div_x.setValue(5)
        self.h_line_div_x = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_div_x.addWidget(self.label_add_div_x)
        self.h_line_div_x.addWidget(self.spin_add_div_x)

        # Создаём надпись, SpinBox и гор.слой
        self.label_add_div_y = QtWidgets.QLabel('Additional division Y :')
        self.spin_add_div_y = QtWidgets.QSpinBox()
        self.spin_add_div_y.setRange(0, 10)
        self.spin_add_div_y.setValue(5)
        self.h_line_div_y = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_div_y.addWidget(self.label_add_div_y)
        self.h_line_div_y.addWidget(self.spin_add_div_y)

        # Создаём надпись, редактор текста и гор.слой
        self.label_name_graph = QtWidgets.QLabel('Name graph :')
        self.text_edit_name = QtWidgets.QLineEdit()
        self.text_edit_name.setMaximumSize(150, 30)
        self.text_edit_name.setMaxLength(20)
        self.h_line_name_graph = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_name_graph.addWidget(self.label_name_graph)
        self.h_line_name_graph.addWidget(self.text_edit_name)

        # Создаём надпись, SpinBox и гор.слой
        self.label_rotation_x = QtWidgets.QLabel('Angle rotation X :')
        self.spin_rotation_x = QtWidgets.QSpinBox()
        self.spin_rotation_x.setRange(0, 90)
        self.h_line_rotation_x = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_rotation_x.addWidget(self.label_rotation_x)
        self.h_line_rotation_x.addWidget(self.spin_rotation_x)

        # Добавляем строки на верт.слой настроек
        self.v_box_prop_graph.addLayout(self.h_line_dev)
        self.v_box_prop_graph.addLayout(self.h_line_div_x)
        self.v_box_prop_graph.addLayout(self.h_line_div_y)
        self.v_box_prop_graph.addLayout(self.h_line_name_graph)
        self.v_box_prop_graph.addLayout(self.h_line_rotation_x)

        # Создаём GroupBox для настройки графика
        self.group_box_prop_graph = QtWidgets.QGroupBox('Properties Graph')
        # Добавляем верт.слой для настроек
        self.group_box_prop_graph.setLayout(self.v_box_prop_graph)

        # Следующий GroupBox
        # Создаём верт.слой для GroupBox
        self.v_box_prop_image = QtWidgets.QVBoxLayout()

        # Создаём надпись, SpinBox и гор.слой
        self.label_wight_pix = QtWidgets.QLabel('Wight, pix :')
        self.spin_wight_pix = QtWidgets.QSpinBox()
        self.spin_wight_pix.setRange(400, 1200)
        self.spin_wight_pix.setValue(1000)
        self.h_line_wight = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_wight.addWidget(self.label_wight_pix)
        self.h_line_wight.addWidget(self.spin_wight_pix)

        # Создаём надпись, SpinBox и гор.слой
        self.label_height_pix = QtWidgets.QLabel('Height, pix :')
        self.spin_height_pix = QtWidgets.QSpinBox()
        self.spin_height_pix.setRange(300, 800)
        self.spin_height_pix.setValue(750)
        self.h_line_height = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_height.addWidget(self.label_height_pix, alignment=QtCore.Qt.AlignTop)
        self.h_line_height.addWidget(self.spin_height_pix, alignment=QtCore.Qt.AlignTop)

        # Добавляем строки на верт.слой настроек
        self.v_box_prop_image.addLayout(self.h_line_wight)
        self.v_box_prop_image.addLayout(self.h_line_height)

        # Создаём GroupBox для настройки графики
        self.group_box_prop_image = QtWidgets.QGroupBox('Properties Image')
        self.group_box_prop_image.setLayout(self.v_box_prop_image)

        # Следующий GroupBox
        # Создаём верт.слой для GroupBox
        self.v_box_prop_file = QtWidgets.QVBoxLayout()

        # Создаём надпись, TimeEdit и гор.слой
        self.label_time_start = QtWidgets.QLabel('Time started :')
        self.time_edit_time_start = QtWidgets.QTimeEdit()
        self.time_edit_time_start.setDisplayFormat('h:mm:ss')
        self.h_line_time_start = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_time_start.addWidget(self.label_time_start)
        self.h_line_time_start.addWidget(self.time_edit_time_start)

        # Создаём надпись и выподающий список и гор.слой
        self.label_time_long = QtWidgets.QLabel('Time long, sec :')
        self.combo_box_time_long = QtWidgets.QComboBox()
        self.combo_box_time_long.addItems(['300', '600', '1200',
                                           '2400', '1800', '3600',
                                           '7200', '14400', '28800',
                                           '43200', '86400'])
        self.combo_box_time_long.setCurrentText('3600')
        self.h_line_time_long = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_time_long.addWidget(self.label_time_long)
        self.h_line_time_long.addWidget(self.combo_box_time_long)

        # Создаём надпись, SpinBox и гор.слой
        self.label_score_colomn = QtWidgets.QLabel('Score colomn :')
        self.spin_score_colomn = QtWidgets.QSpinBox()
        self.spin_score_colomn.setRange(0, 30)
        self.h_line_score_colomn = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_score_colomn.addWidget(self.label_score_colomn)
        self.h_line_score_colomn.addWidget(self.spin_score_colomn)

        # Создаём надпись и выподающий список и гор.слой
        self.label_delimit_csv = QtWidgets.QLabel('Delimiter CSV :')
        self.combo_box_delimit_csv = QtWidgets.QComboBox()
        self.combo_box_delimit_csv.addItems(['Comma', 'Dot and comma'])
        self.h_line_delimit_csv = QtWidgets.QHBoxLayout()
        # Добавляем виджеты на горизонтальный шаблон
        self.h_line_delimit_csv.addWidget(self.label_delimit_csv)
        self.h_line_delimit_csv.addWidget(self.combo_box_delimit_csv)

        # Добавляем строки на верт.слой настроек файла
        self.v_box_prop_file.addLayout(self.h_line_time_start)
        self.v_box_prop_file.addLayout(self.h_line_time_long)
        self.v_box_prop_file.addLayout(self.h_line_score_colomn)
        self.v_box_prop_file.addLayout(self.h_line_delimit_csv)

        # Создаём GroupBox для настройки файла
        self.group_box_prop_file = QtWidgets.QGroupBox('Properties File')
        self.group_box_prop_file.setLayout(self.v_box_prop_file)

        # Создаём кнопки открытия файла и создания графика
        self.btn_open_file = QtWidgets.QPushButton('Open file')
        self.btn_open_file.clicked.connect(self.get_file_dir_image)
        self.btn_open_file.setMinimumSize(200, 30)
        self.btn_create_graph = QtWidgets.QPushButton('Create graph')
        self.btn_create_graph.clicked.connect(self.create_image)
        self.btn_create_graph.setMinimumSize(200, 30)

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
        # Устанавливаем политику изменения размеров окна поля
        # (фиксированное по оси X и Y)
        self.view_scene.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        # Показываем наше поле просмотра
        self.view_scene.show()
        # Добаляем поле просмотра и кнопку на главное окно
        self.h_box_main.addWidget(self.view_scene)
        self.h_box_main.addLayout(self.v_box_all_properties)
        self.setLayout(self.h_box_main)

        # Создаём переменную для хранения пути csv-файла
        self.dir_csv_file = 'None'

    def create_image(self):
        if not (self.dir_csv_file == 'None'):
            plot_graph.create_image_file(file_path=self.dir_csv_file,
                                         time_str=self.time_edit_time_start.time().toString('HH:mm:ss'),
                                         time_long=int(self.combo_box_time_long.currentText()),
                                         angle_rotation=self.spin_rotation_x.value(),
                                         dev_major_x=int(self.combo_box_dev.currentText()),
                                         dev_minor_x=self.spin_add_div_x.value(),
                                         dev_minor_y=self.spin_add_div_y.value(),
                                         width_px=self.spin_wight_pix.value(),
                                         heigth_px=self.spin_height_pix.value(),
                                         name_line1=self.text_edit_name.text(),
                                         score_colomn=self.spin_score_colomn.value(),
                                         delimiter_csv=self.combo_box_delimit_csv.currentText())
            
            self.sienna.clear()
            QtGui.QPixmapCache.clear()
            # print(self.image_graph.cacheKey()) <- для отладки
            self.image_graph.load('temp_image.png')
            self.sienna.addPixmap(self.image_graph)
        else:
            error_window = QtWidgets.QMessageBox.information(self,
                                                             'Error!',
                                                             "File CSV don't open!")
        pass

    def get_file_dir_image(self):
        dir_name_csv = QtWidgets.QFileDialog.getOpenFileName(self, caption='Set file CSV',
                                                             filter='Exes (*.csv)')
        self.dir_csv_file = dir_name_csv[0]
        print(self.dir_csv_file)
        pass

    def resizeEvent(self, e):
        """
        Перегрузка метода для отладки
        :param e: событие метода resizeEvent
        :return: возвращает размер окна в консоль
        """
        #print(e.size())
        #print(self.dir_csv_file)
        pass

    pass


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
