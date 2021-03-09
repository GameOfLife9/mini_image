import numpy as np
import sys
import cv2 as cv
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QImage

import part1.m_edit as m_edit

class main_widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.root_path="D:/miniImage"
        print("m_ui.py:改成你自己的root_path %s" % self.root_path)
        self.m_init()

    def m_init(self):
        self.m_image=cv.imread(self.root_path+"/core/redrock.png")
        self.m_image=cv.cvtColor(self.m_image,cv.COLOR_BGR2RGB)

        self.init_imgae()
        self.file_menubar()
        self.edit_menubar()

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
    def edit_menubar(self):
        #调整
        hsv_change_action=QAction('&色相/饱和度/明度', self)
        hsv_change_action.triggered.connect(self.hsv_change)

        self.hsv_widget=m_edit.hsv_widegt()

        change_menu = QMenu('调整', self)
        change_menu.addAction(hsv_change_action)

        menubar = self.menuBar()
        editMenu = menubar.addMenu('&编辑')
        editMenu.addMenu(change_menu)

    def hsv_change(self):
        self.hsv_widget.show()

    def open_file(self):
        open_file_path = QFileDialog.getOpenFileNames(self, '选择文件',self.root_path,"photo(*.jpg *.png)")

        if open_file_path[0] is not None:
            new_image=cv.imread(open_file_path[0][0])
            new_image=cv.cvtColor(new_image, cv.COLOR_BGR2RGB)
            self.m_image = new_image

            self.updata_image()



