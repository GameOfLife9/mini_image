import cv2 as cv
from PyQt5.QtWidgets import QWidget,QSlider,QLabel,QAction,QMenu
from PyQt5.QtCore import Qt
def init_menue(instance):
    # 调整
    instance.signal_edit_bar_1_hsv.connect(hsv_change)
    instance.widegt_hsv = QWidget()
    # 色调/饱和度/明度-------------------------------------------

    # -----slider_h--------------------------------------------
    instance.sld_hsv_h = QSlider(Qt.Horizontal, instance.widegt_hsv)
    instance.sld_hsv_h.setGeometry(30, 40, 100, 30)
    instance.sld_hsv_h.sliderReleased.connect(instance.hsv_signal_emit)

    instance.sld_hsv_h.setMinimum(-100)
    instance.sld_hsv_h.setMaximum(100)
    instance.sld_hsv_h.setSingleStep(1)
    instance.sld_hsv_h.setValue(0)
    instance.sld_hsv_h.setObjectName("sld_hsv_h")

    instance.widegt_hsv.label_hsv_h = QLabel(instance.widegt_hsv)
    instance.widegt_hsv.label_hsv_h.setText("色调")
    instance.widegt_hsv.label_hsv_h.setGeometry(0, 40, 30, 30)

    # -----slider_s--------------------------------------------
    instance.sld_hsv_s = QSlider(Qt.Horizontal, instance.widegt_hsv)
    instance.sld_hsv_s.setGeometry(30, 70, 100, 30)
    instance.sld_hsv_s.sliderReleased.connect(instance.hsv_signal_emit)

    instance.sld_hsv_s.setMinimum(-100)
    instance.sld_hsv_s.setMaximum(100)
    instance.sld_hsv_s.setSingleStep(1)
    instance.sld_hsv_s.setValue(0)
    instance.sld_hsv_s.setObjectName("sld_hsv_s")

    instance.widegt_hsv.label_hsv_s = QLabel(instance.widegt_hsv)
    instance.widegt_hsv.label_hsv_s.setText("饱和")
    instance.widegt_hsv.label_hsv_s.setGeometry(0, 70, 30, 30)

    # -----slider_v--------------------------------------------
    instance.sld_hsv_v = QSlider(Qt.Horizontal, instance.widegt_hsv)
    instance.sld_hsv_v.setGeometry(30, 100, 100, 30)
    instance.sld_hsv_v.sliderReleased.connect(instance.hsv_signal_emit)

    instance.sld_hsv_v.setMinimum(-100)
    instance.sld_hsv_v.setMaximum(100)
    instance.sld_hsv_v.setSingleStep(1)
    instance.sld_hsv_v.setValue(0)
    instance.sld_hsv_v.setObjectName("sld_hsv_v")

    instance.widegt_hsv.label_hsv_v = QLabel(instance.widegt_hsv)
    instance.widegt_hsv.label_hsv_v.setText("明度")
    instance.widegt_hsv.label_hsv_v.setGeometry(0, 100, 30, 30)

    # --------------------------------------------------------------
    instance.widegt_hsv.setGeometry(300, 300, 280, 170)
    instance.widegt_hsv.setWindowTitle('色调/饱和度/明度调整')

    hsv_change_action = QAction('&色相/饱和度/明度', instance)
    hsv_change_action.triggered.connect(instance.hsv_show)
    # ------------------------------------------------------

    change_menu = QMenu('调整', instance)
    change_menu.addAction(hsv_change_action)

    menubar = instance.menuBar()
    editMenu = menubar.addMenu('&编辑')
    editMenu.addMenu(change_menu)


def hsv_change(instance,type,h):
    image=cv.cvtColor(instance.m_image, cv.COLOR_RGB2HSV)
    row = image.shape[0]
    col = image.shape[1]

    for i in range(0,row-1):
        for j in range(0,col-1):
            image[i][j][type]=image[i][j][type]+h

            if type==0:
                if image[i][j][type]>179:
                    image[i][j][type]=179
            else:
                if image[i][j][type]>255:
                    image[i][j][type]=255

            if image[i][j][type] < 0:
                image[i][j][type] = 0
    instance.m_image=cv.cvtColor(image, cv.COLOR_HSV2RGB)
    instance.updata_image()

