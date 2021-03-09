from PyQt5.QtWidgets import QWidget,QSlider,QLabel
from PyQt5.QtCore import Qt
class hsv_widegt(QWidget):
    def __init__(self):
        super().__init__()
        self.m_init()
    def m_init(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        #self.show()

    def changeValue(self, value):
        s=1