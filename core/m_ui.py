import numpy as np
import sys
import cv2 as cv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtCore import Qt,pyqtSignal

import part1.m_edit as m_edit
class main_widget(QMainWindow):
    signal_edit_bar_1_hsv = pyqtSignal('PyQt_PyObject',int)
    def __init__(self):
        super().__init__()
        self.root_path="F:/mini_image"
        print("m_ui.py:改成你自己的root_path %s" % self.root_path)
        self.m_init()

    def m_init(self):
        self.m_image=cv.imread(self.root_path+"/core/redrock.png")
        self.m_image=cv.cvtColor(self.m_image,cv.COLOR_BGR2RGB)

        self.init_imgae()
        self.file_menubar()
        self.edit_menubar()
        self.process_menubar()

        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('mini image')
        self.show()

    def init_imgae(self):
        self.m_QImage = QImage(self.m_image[:], self.m_image.shape[1], self.m_image.shape[0], self.m_image.shape[1] * 3,
                               QImage.Format_RGB888)

        self.m_image_width = 600
        self.m_image_height = self.m_image.shape[0] / self.m_image.shape[1] * self.m_image_width

        self.pixmap = QPixmap(self.m_QImage)

        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl.resize(self.m_image_width, self.m_image_height)
        self.lbl.setScaledContents(True)
        self.lbl.setGeometry(0, 0, self.m_image_width, self.m_image_height)

    def updata_image(self):
        self.m_QImage = QImage(self.m_image[:], self.m_image.shape[1], self.m_image.shape[0], self.m_image.shape[1] * 3,
                               QImage.Format_RGB888)

        self.m_image_width = 600
        self.m_image_height = self.m_image.shape[0] / self.m_image.shape[1] * self.m_image_width

        self.pixmap = QPixmap(self.m_QImage)

        self.lbl.setPixmap(self.pixmap)
        self.lbl.resize(self.m_image_width, self.m_image_height)
        self.lbl.setScaledContents(True)
        self.lbl.setGeometry(0, 0, self.m_image_width, self.m_image_height)

    def file_menubar(self):
        #程序退出
        exitAction = QAction('&退出', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        #文件打开
        open_file_Action = QAction('&打开', self)
        open_file_Action.triggered.connect(self.open_file)

        self.statusBar()
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&文件')

        fileMenu.addAction(exitAction)
        fileMenu.addAction(open_file_Action)

    def open_file(self):
        open_file_path = QFileDialog.getOpenFileNames(self, '选择文件',self.root_path,"photo(*.jpg *.png)")

        if open_file_path[0] is not None:
            new_image=cv.imread(open_file_path[0][0])
            new_image=cv.cvtColor(new_image, cv.COLOR_BGR2RGB)
            self.m_image = new_image

            self.updata_image()

    def edit_menubar(self):
        #调整
        self.signal_edit_bar_1_hsv.connect(m_edit.hsv_change)
        self.widegt_hsv = QWidget()
        #色调/饱和度/明度-------------------------------------------

        #-----slider_h--------------------------------------------
        self.sld_hsv_h = QSlider(Qt.Horizontal, self.widegt_hsv)
        self.sld_hsv_h.setGeometry(30, 40, 100, 30)
        self.sld_hsv_h.sliderReleased.connect(self.hsv_signal_emit)

        self.sld_hsv_h.setMinimum(-100)
        self.sld_hsv_h.setMaximum(100)
        self.sld_hsv_h.setSingleStep(1)
        self.sld_hsv_h.setValue(0)
        self.sld_hsv_h.setObjectName("sld_hsv_h")

        self.widegt_hsv.label_hsv_h = QLabel(self.widegt_hsv)
        self.widegt_hsv.label_hsv_h.setText("色调")
        self.widegt_hsv.label_hsv_h.setGeometry(0, 40, 30, 30)

        #-----slider_s--------------------------------------------
        self.sld_hsv_s = QSlider(Qt.Horizontal, self.widegt_hsv)
        self.sld_hsv_s.setGeometry(30, 70, 100, 30)
        self.sld_hsv_s.sliderReleased.connect(self.hsv_signal_emit)

        self.sld_hsv_s.setMinimum(-100)
        self.sld_hsv_s.setMaximum(100)
        self.sld_hsv_s.setSingleStep(1)
        self.sld_hsv_s.setValue(0)
        self.sld_hsv_s.setObjectName("sld_hsv_s")

        self.widegt_hsv.label_hsv_s = QLabel(self.widegt_hsv)
        self.widegt_hsv.label_hsv_s.setText("饱和")
        self.widegt_hsv.label_hsv_s.setGeometry(0, 70, 30, 30)

        #-----slider_v--------------------------------------------
        self.sld_hsv_v = QSlider(Qt.Horizontal, self.widegt_hsv)
        self.sld_hsv_v.setGeometry(30, 100, 100, 30)
        self.sld_hsv_v.sliderReleased.connect(self.hsv_signal_emit)

        self.sld_hsv_v.setMinimum(-100)
        self.sld_hsv_v.setMaximum(100)
        self.sld_hsv_v.setSingleStep(1)
        self.sld_hsv_v.setValue(0)
        self.sld_hsv_v.setObjectName("sld_hsv_v")

        self.widegt_hsv.label_hsv_v = QLabel(self.widegt_hsv)
        self.widegt_hsv.label_hsv_v.setText("明度")
        self.widegt_hsv.label_hsv_v.setGeometry(0, 100, 30, 30)

        #--------------------------------------------------------------
        self.widegt_hsv.setGeometry(300, 300, 280, 170)
        self.widegt_hsv.setWindowTitle('色调/饱和度/明度调整')

        hsv_change_action=QAction('&色相/饱和度/明度', self)
        hsv_change_action.triggered.connect(self.hsv_show)
        #------------------------------------------------------

        change_menu = QMenu('调整', self)
        change_menu.addAction(hsv_change_action)

        menubar = self.menuBar()
        editMenu = menubar.addMenu('&编辑')
        editMenu.addMenu(change_menu)

    def hsv_show(self):
        self.widegt_hsv.show()
    def hsv_signal_emit(self):
        type=0
        if self.sender().objectName()=="sld_hsv_h":
            type=0
        if self.sender().objectName()=="sld_hsv_s":
            type=1
        if self.sender().objectName()=="sld_hsv_v":
            type=2
        print(type)
        self.signal_edit_bar_1_hsv.emit(self,type)

    def process_menubar(self):
        blur_mean_action=QAction('&均值模糊', self)
        blur_mean_action.triggered.connect(self.action_blur_mean)

        change_menu = QMenu('模糊', self)
        change_menu.addAction(blur_mean_action)

        menubar = self.menuBar()
        editMenu = menubar.addMenu('&图像')
        editMenu.addMenu(change_menu)

    def action_blur_mean(self):
        self.m_image=cv.blur(self.m_image,(5,5))
        self.updata_image()




