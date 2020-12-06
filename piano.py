from PyQt5 import Qt, QtWidgets, QtMultimedia, QtCore
from PyQt5.QtWidgets import QMainWindow
import pyqtgraph


class Piano(QMainWindow):
    def __init__(self, parent=None):
        super(Piano, self).__init__(parent)
        self.setWindowTitle("Фортепиано")
        # создаем виджеты
        self.main_widget = QtWidgets.QWidget(self)
        self.lbl_do = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _S_')
        self.lbl_do.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_re = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _D_')
        self.lbl_re.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_mi = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _F_')
        self.lbl_mi.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_fa = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _G_')
        self.lbl_fa.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_so = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _H_')
        self.lbl_so.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_la = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _J_')
        self.lbl_la.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_si = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _K_')
        self.lbl_si.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.lbl_all = QtWidgets.QLabel(self.main_widget, text = 'Клавиша: _L_')
        self.lbl_all.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

        self.btn_do = Qt.QPushButton('До')
        self.btn_re = Qt.QPushButton('Ре')
        self.btn_mi = Qt.QPushButton('Ми')
        self.btn_fa = Qt.QPushButton('Фа')
        self.btn_so = Qt.QPushButton('Соль')
        self.btn_la = Qt.QPushButton('Ля')
        self.btn_si = Qt.QPushButton('Си')
        self.btn_all = Qt.QPushButton('Все')

        # задаем расположение
        self.gridLayout = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout.addWidget(self.lbl_do, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.lbl_re, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.lbl_mi, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.lbl_fa, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.lbl_so, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.lbl_la, 0, 5, 1, 1)
        self.gridLayout.addWidget(self.lbl_si, 0, 6, 1, 1)
        self.gridLayout.addWidget(self.lbl_all, 0, 7, 1, 1)

        self.gridLayout.addWidget(self.btn_do, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.btn_re, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.btn_mi, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.btn_fa, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.btn_so, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.btn_la, 1, 5, 1, 1)
        self.gridLayout.addWidget(self.btn_si, 1, 6, 1, 1)
        self.gridLayout.addWidget(self.btn_all, 1, 7, 1, 1)

        self.setCentralWidget(self.main_widget)

        # задаем события (сигналы)
        self.btn_do.clicked.connect(lambda: self.igraet_music('music/do.mp3'))
        self.btn_re.clicked.connect(lambda: self.igraet_music('music/re.mp3'))
        self.btn_mi.clicked.connect(lambda: self.igraet_music('music/mi.mp3'))
        self.btn_fa.clicked.connect(lambda: self.igraet_music('music/fa.mp3'))
        self.btn_so.clicked.connect(lambda: self.igraet_music('music/sol.mp3'))
        self.btn_la.clicked.connect(lambda: self.igraet_music('music/lja.mp3'))
        self.btn_si.clicked.connect(lambda: self.igraet_music('music/si.mp3'))
        self.btn_all.clicked.connect(lambda: self.igraet_music('music/do-re-mi-fa-sol-lja-si.mp3'))

    def igraet_music(self, filename):
        content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(filename))
        self.player = QtMultimedia.QMediaPlayer(media = content)
        self.player.play()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_S:
            self.igraet_music('music/do.mp3')
        elif event.key() == QtCore.Qt.Key_D:
            self.igraet_music('music/re.mp3')
        elif event.key() == QtCore.Qt.Key_F:
            self.igraet_music('music/mi.mp3')
        elif event.key() == QtCore.Qt.Key_G:
            self.igraet_music('music/fa.mp3')
        elif event.key() == QtCore.Qt.Key_H:
            self.igraet_music('music/sol.mp3')
        elif event.key() == QtCore.Qt.Key_J:
            self.igraet_music('music/lja.mp3')
        elif event.key() == QtCore.Qt.Key_K:
            self.igraet_music('music/si.mp3')
        elif event.key() == QtCore.Qt.Key_L:
            self.igraet_music('music/do-re-mi-fa-sol-lja-si.mp3')


if __name__ == "__main__":
    import sys
    app = Qt.QApplication([])
    main = Piano()
    main.show()
    sys.exit(app.exec_())