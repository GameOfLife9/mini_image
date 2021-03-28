import sys

import cv2 as cv
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from core import image_init_update,m_init_file_menu

from part1 import m_edit,file_function_define
from part2 import m_init_process,m_blur
from part3 import m_init_style_transfer
from part4 import m_init_part4_menubar

class main_widget(QMainWindow):

    # 信号需要放在函数外面声明，初始化参数为信号发射时需要的参数类型
    # PyQt_PyObject：任何类型都可以
    # int 传入int型参数

    signal_file_bar_openfile = pyqtSignal('PyQt_PyObject')
    signal_edit_bar_1_hsv = pyqtSignal('PyQt_PyObject', int, int)
    signal_processing_bar_blur = pyqtSignal('PyQt_PyObject', int, int)
    signal_neural_style_transfer = pyqtSignal('PyQt_PyObject')
    signal_part4_segmentation_human = pyqtSignal('PyQt_PyObject')

    signal_part5_submenu1=pyqtSignal('PyQt_PyObject', int)
    def __init__(self):
        # 父类QMainWindow初始化
        super().__init__()

        # 设置根路径
        self.root_path = "F:/mini_image"
        print("m_ui.py:改成你自己的root_path %s" % self.root_path)

        # 当前类初始化
        self.m_init()

    def m_init(self):
        # 读入一张初始图片
        self.m_image = cv.imread(self.root_path + "/core/redrock.png")

        # OpenCv读入格式为BGR，需要转换成RGB
        self.m_image = cv.cvtColor(self.m_image, cv.COLOR_BGR2RGB)

        # 初始化图像
        self.init_imgae()

        # 文件菜单，编辑菜单，图像菜单，风格迁移菜单，part4菜单初始化
        self.file_menubar()
        self.edit_menubar()
        self.process_menubar()
        self.style_transfer_menubar()
        self.part4_menurbar()

        #self.part5_menubar()
        # 设置主窗口的属性
        #!!!!!!!!!!!!!!!!!!!!
        self.setGeometry(300, 300, self.m_image_width + 10, self.m_image_height + 10)
        self.setWindowTitle('mini image')

        # 显示窗口
        self.show()

    # 图像初始化
    def init_imgae(self):
        image_init_update.image_init(self)

    # 图像数据刷新
    def updata_image(self):
        image_init_update.image_update(self)

    # core 代码区域----------------------------------------------------------------------------

    # file menubar文件菜单初始化
    def file_menubar(self):
        m_init_file_menu.init_file_menu(self)

    # 打开文件信号发射函数
    def signal_open_file_emit(self):
        # 信号发射，执行该信号关联的函数
        m_init_file_menu.open_file(self)

    def signal_save_file_emit(self):
        m_init_file_menu.save_file(self)
    # part1 代码区域----------------------------------------------------------------------------

    # edit menurbar编辑菜单初始化
    def edit_menubar(self):
        m_edit.init_menue(self)

    # 显示调整hsv的窗口
    def hsv_show(self):
        self.widegt_hsv.show()

    def signal_rotate_emit(self):
        angle=0.0
        if self.sender().objectName() == "rotate_cw_action" or self.sender().objectName()=="rotate_cw_button":
            angle = 90.0
        if self.sender().objectName() == "rotate_ccw_action" or self.sender().objectName()=="rotate_ccw_button":
            angle = -90.0
        print(angle)
        m_edit.rotate_action(self,angle)
    def show_edit_widget(self):
        self.widegt_edit_second.show()
    # hsv调整信号发射函数
    def hsv_signal_emit(self):
        type = 0

        # 根据信号源的名字决定type的类型，调整H，S，V对应type分别为0 1 2
        if self.sender().objectName() == "sld_hsv_h":
            type = 0
        if self.sender().objectName() == "sld_hsv_s":
            type = 1
        if self.sender().objectName() == "sld_hsv_v":
            type = 2

        # 信号发射的value为信号源即滑动条的value
        # 信号发射，执行该信号关联的函数
        self.signal_edit_bar_1_hsv.emit(self, type, self.sender().value())

    def stage_change_emit(self):
        type=0
        if self.sender().objectName()=="cb_percent_bool":
            type=1
        if self.sender().objectName()=="cb_piexl_bool":
            type=2
        m_edit.state_change_cb_pix_percent(self,type)

    def signal_resize_button_clicked(self):
        m_edit.change_size_button_clicked(self)

    def signal_button_painter_rect(self):
        m_edit.button_action_painter_rect(self)

    def signal_gray_acition_emit(self):
        file_function_define.gray_process(self)

    def signal_invese_color_emit(self):
        file_function_define.inverse_color(self)
    def signal_threshold_emit(self):
        file_function_define.threshold_processing(self)
    # part2 代码区域----------------------------------------------------------------------------

    # process menubar图像菜单初始化
    def process_menubar(self):
        m_init_process.init_menu(self)

    # 模糊图像信号发射函数
    def signal_blur_emit(self):
        type = 0

        # 获取信号源即滑动条的value
        value = self.sender().value()

        # 根据信号源的名字决定type的类型
        if self.sender().objectName() == "mean_blur":
            type = 0

        # 信号发射，执行该信号关联的函数
        self.signal_processing_bar_blur.emit(self, type, value)

    def mean_blur_widegt_show(self):
        # 显示均匀模糊操作窗口
        self.widegt_mean_blur.show()

    def update_temp_image_for_blur(self):
        m_blur.update_temp_image(self)

    def button_mean_blur_clicked(self):
        self.m_image=self.temp_image_blur
        self.updata_image()
    # part3 代码区域----------------------------------------------------------------------------

    # style transfer menubar 风格迁移菜单初始化
    def style_transfer_menubar(self):
        m_init_style_transfer.init_style_transfer_menubar(self)

    # 显示基于神经网络的风格迁移操作窗口
    def show_neural_style_transfer_widget(self):
        self.widget_neural_style_transfer.show()

    # 信号发射，执行该信号关联的函数
    def signal_neural_style_emit(self):
        self.signal_neural_style_transfer.emit(self)

    def open_file_and_change_name(self):
        self.style_file_transfer=QFileDialog.getOpenFileNames(self, '选择文件',self.root_path+"/part3/images","photo(*.jpg *.png)")
        self.label_style_file.setText(self.style_file_transfer[0][0])
    # part4 代码区域----------------------------------------------------------------------------

    # part4 menubar part4菜单初始化
    def part4_menurbar(self):
        m_init_part4_menubar.init_part4_menubar(self)

    # 显示part4菜单
    def show_segmentation_human_widget(self):
        self.widget_segmentation_human.show()

    # 信号发射，执行该信号关联的函数
    def signal_segmentation_human_emit(self):
        self.signal_part4_segmentation_human.emit(self)

    '''
    # part5 代码区域仅为教程使用--------------------------------
    def part5_menubar(self):
        self.m_var="aaa"
        init_menu_part5.init_part5(self)
    def show_part4_submenu_widget(self):
        self.widegt_part5_submenu1.show()
    def signal_show_slider_value_emit(self):
        value=self.sender().value()
        self.signal_part5_submenu1.emit(self,value)
    '''