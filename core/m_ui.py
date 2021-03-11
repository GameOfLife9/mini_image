import numpy as np
import sys
from PyQt5.QtGui import QPixmap,QImage
from part2 import m_blur

import cv2 as cv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,pyqtSignal

from part1 import m_edit

from core import image_init_update as init_update
from core import  m_init_file_menu

import part2.m_init_process as menu_process_init

class main_widget(QMainWindow):
    signal_file_bar_openfile = pyqtSignal('PyQt_PyObject')
    signal_edit_bar_1_hsv = pyqtSignal('PyQt_PyObject',int)
    signal_processing_bar_blur = pyqtSignal('PyQt_PyObject', int,int)

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
        init_update.image_init(self)

    def updata_image(self):
        init_update.image_update(self)

    def file_menubar(self):
        m_init_file_menu.init_file_menu(self)

    def signal_open_file_emit(self):
        m_init_file_menu.open_file(self)

    def edit_menubar(self):
        m_edit.init_menue(self)

    def hsv_show(self):
        self.widegt_hsv.show()
    def mean_blur_widegt_show(self):
        self.widegt_mean_blur.show()

    def hsv_signal_emit(self):
        type=0
        if self.sender().objectName()=="sld_hsv_h":
            type=0
        if self.sender().objectName()=="sld_hsv_s":
            type=1
        if self.sender().objectName()=="sld_hsv_v":
            type=2
        self.signal_edit_bar_1_hsv.emit(self,type)
    def signal_blur_emit(self):
        type=0
        value=self.sender().value()
        if self.sender().objectName()=="mean_blur":
            type=0
        self.signal_processing_bar_blur.emit(self,type,value)
    def process_menubar(self):
        menu_process_init.init_menu(self)





