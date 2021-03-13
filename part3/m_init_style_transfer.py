from PyQt5.QtWidgets import QAction,QMenu,QWidget,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt
from part3 import neural_style_transfer_core
def init_style_transfer_menubar(instance):
    instance.signal_neural_style_transfer.connect(neural_style_transfer_core.neual_style_transfer)

    instance.widget_neural_style_transfer=QWidget()

    instance.button_neural_style_stop=QPushButton("开始",instance.widget_neural_style_transfer)
    instance.button_neural_style_stop.setGeometry(30, 30, 50, 50)
    instance.button_neural_style_stop.clicked.connect(instance.signal_neural_style_emit)

    instance.widget_neural_style_transfer.setGeometry(300, 300, 280, 170)
    instance.widget_neural_style_transfer.setWindowTitle('基于神经网络的风格迁移')

    action_neural_style_widget_show = QAction('&基于神经网络的风格迁移', instance)
    action_neural_style_widget_show.triggered.connect(instance.show_neural_style_transfer_widget)

    menubar = instance.menuBar()
    tempMenu = menubar.addMenu('&艺术风格迁移')
    tempMenu.addAction(action_neural_style_widget_show)