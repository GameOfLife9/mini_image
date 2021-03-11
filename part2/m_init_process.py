from PyQt5.QtWidgets import QAction,QMenu,QWidget,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt
from part2 import m_blur
def init_menu(instance):
    instance.widegt_mean_blur=QWidget()
    instance.sld_mean_blur=QSlider(Qt.Horizontal, instance.widegt_mean_blur)
    instance.sld_mean_blur.setGeometry(30, 40, 100, 30)
    instance.sld_mean_blur.sliderReleased.connect(instance.signal_blur_emit)

    instance.sld_mean_blur.setMinimum(3)
    instance.sld_mean_blur.setMaximum(11)
    instance.sld_mean_blur.setSingleStep(2)
    instance.sld_mean_blur.setValue(3)

    instance.sld_mean_blur.setObjectName("mean_blur")
    instance.signal_processing_bar_blur.connect(m_blur.blur)

    blur_mean_action = QAction('&均值模糊', instance)
    blur_mean_action.triggered.connect(instance.mean_blur_widegt_show)

    change_menu = QMenu('模糊', instance)
    change_menu.addAction(blur_mean_action)

    menubar = instance.menuBar()
    editMenu = menubar.addMenu('&图像')
    editMenu.addMenu(change_menu)
