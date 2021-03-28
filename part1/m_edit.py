from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2 as cv
import numpy as np
from part1 import hsv_change
def init_menue(instance):
    # 连接信号，当该信号被发射后执行括号内被连接函数
    instance.signal_edit_bar_1_hsv.connect(hsv_change.hsv_change_fun)

    # 创建一个窗口，定义位置，标题等属性
    instance.widegt_hsv = QWidget()
    instance.widegt_hsv.setGeometry(300, 300, 280, 170)
    instance.widegt_hsv.setWindowTitle('色调/饱和度/明度调整')


    # --------------------------------------------------------------------slider_h
    # 创建一个滑动条，当该滑动条拖动释放时发射信号，该滑动条的父对象为widegt_hsv
    sld_hsv_h = QSlider(Qt.Horizontal, instance.widegt_hsv)
    sld_hsv_h.setGeometry(30, 40, 100, 30)
    sld_hsv_h.sliderReleased.connect(instance.hsv_signal_emit)

    # 为滑动条设置最小最大值，初始值等属性
    sld_hsv_h.setMinimum(-100)
    sld_hsv_h.setMaximum(100)
    sld_hsv_h.setSingleStep(1)
    sld_hsv_h.setValue(0)

    # 设置object name(可选)，主要是在某些情况下可以根据信号源的object name来选择下一步操作
    sld_hsv_h.setObjectName("sld_hsv_h")

    # 为该滑动条添加一个label，它的父对象为instance.widegt_hsv
    instance.widegt_hsv.label_hsv_h = QLabel(instance.widegt_hsv)
    instance.widegt_hsv.label_hsv_h.setText("色调")
    instance.widegt_hsv.label_hsv_h.setGeometry(0, 40, 30, 30)

    # --------------------------------------------------------------------slider_s（同上）
    sld_hsv_s = QSlider(Qt.Horizontal, instance.widegt_hsv)
    sld_hsv_s.setGeometry(30, 70, 100, 30)
    sld_hsv_s.sliderReleased.connect(instance.hsv_signal_emit)

    sld_hsv_s.setMinimum(-100)
    sld_hsv_s.setMaximum(100)
    sld_hsv_s.setSingleStep(1)
    sld_hsv_s.setValue(0)
    sld_hsv_s.setObjectName("sld_hsv_s")

    instance.widegt_hsv.label_hsv_s = QLabel(instance.widegt_hsv)
    instance.widegt_hsv.label_hsv_s.setText("饱和")
    instance.widegt_hsv.label_hsv_s.setGeometry(0, 70, 30, 30)

    # --------------------------------------------------------------------slider_v（同上）
    sld_hsv_v = QSlider(Qt.Horizontal, instance.widegt_hsv)
    sld_hsv_v.setGeometry(30, 100, 100, 30)
    sld_hsv_v.sliderReleased.connect(instance.hsv_signal_emit)

    sld_hsv_v.setMinimum(-100)
    sld_hsv_v.setMaximum(100)
    sld_hsv_v.setSingleStep(1)
    sld_hsv_v.setValue(0)
    sld_hsv_v.setObjectName("sld_hsv_v")

    instance.widegt_hsv.label_hsv_v = QLabel(instance.widegt_hsv)
    instance.widegt_hsv.label_hsv_v.setText("明度")
    instance.widegt_hsv.label_hsv_v.setGeometry(0, 100, 30, 30)

    # --------------------------------------------------------------

    # 创建一个action，当该action被触发时运行hsv_show
    # hsv_show的作用为显示HSV调整窗口widegt_hsv
    hsv_change_action = QAction('&色相/饱和度/明度', instance)
    hsv_change_action.triggered.connect(instance.hsv_show)

    gray_change_action = QAction('&灰度', instance)
    gray_change_action.triggered.connect(instance.signal_gray_acition_emit)

    inv_color_change_action = QAction('&反相', instance)
    inv_color_change_action.triggered.connect(instance.signal_invese_color_emit)

    init_threhold_widget(instance)
    threshold_action = QAction('&阈值', instance)
    threshold_action.triggered.connect(instance.widegt_threshold_ts.show)

    rotate_cw_action = QAction('&顺时针旋转', instance)
    rotate_cw_action.setObjectName("rotate_cw_action")
    rotate_cw_action.triggered.connect(instance.signal_rotate_emit)

    rotate_ccw_action = QAction('&逆时针旋转', instance)
    rotate_ccw_action.setObjectName("rotate_ccw_action")
    rotate_ccw_action.triggered.connect(instance.signal_rotate_emit)

    init_edit_widget_second(instance)
    init_resize_widget(instance)
    resize_action = QAction('&重新调整大小', instance)
    resize_action.triggered.connect(instance.widegt_resize_ts.show)

    edit_widget_action = QAction('&显示窗口', instance)
    edit_widget_action.triggered.connect(instance.show_edit_widget)


    # 添加一个菜单：调整，这个菜单在后面被添加成图像选项的子选项
    # 为该选项添加一个action hsv_change_action
    change_menu = QMenu('调整', instance)
    change_menu.addAction(hsv_change_action)
    change_menu.addAction(gray_change_action)
    change_menu.addAction(inv_color_change_action)
    change_menu.addAction(threshold_action)

    # 新增一个菜单选项：编辑
    # 编辑选项新增一个子菜单调整
    menubar = instance.menuBar()
    editMenu = menubar.addMenu('&编辑')
    editMenu.addMenu(change_menu)
    editMenu.addAction(rotate_cw_action)
    editMenu.addAction(rotate_ccw_action)
    editMenu.addAction(resize_action)
    editMenu.addAction(edit_widget_action)



def init_threhold_widget(instance):
    instance.widegt_threshold_ts = QWidget()
    instance.widegt_threshold_ts.setGeometry(300, 300, 600, 500)

    label_ts=QLabel(instance.widegt_threshold_ts)
    label_ts.setGeometry(30,30,100,30)
    label_ts.setText("阈值")

    instance.textEdit_threshold = QTextEdit(instance.widegt_threshold_ts)
    instance.textEdit_threshold.setGeometry(130,30,100,30)
    instance.textEdit_threshold.setText("127")

    button_threshold = QPushButton("确定", instance.widegt_threshold_ts)
    button_threshold.setGeometry(70, 100, 100, 30)
    button_threshold.clicked.connect(instance.signal_threshold_emit)


def init_resize_widget(instance):
    instance.widegt_resize_ts = QWidget()
    instance.widegt_edit_second.setGeometry(300, 300, 600, 500)

    instance.cb_percent_bool = QCheckBox('百分比', instance.widegt_resize_ts)
    instance.cb_percent_bool.setChecked(True)
    instance.cb_percent_bool.setGeometry(30,30,100,30)
    instance.cb_percent_bool.setObjectName("cb_percent_bool")
    instance.cb_percent_bool.stateChanged.connect(instance.stage_change_emit)
    instance.cb_percent_bool.setEnabled(False)

    instance.cb_piexl_bool = QCheckBox('像素', instance.widegt_resize_ts)
    instance.cb_piexl_bool.setChecked(False)
    instance.cb_piexl_bool.setGeometry(120,30,100,30)
    instance.cb_piexl_bool.setObjectName("cb_piexl_bool")
    instance.cb_piexl_bool.stateChanged.connect(instance.stage_change_emit)
    instance.cb_piexl_bool.setEnabled(True)

    label_h=QLabel(instance.widegt_resize_ts)
    label_h.setGeometry(30,60,100,30)
    label_h.setText("水平(H)：")

    instance.textEdit_h = QTextEdit(instance.widegt_resize_ts)
    instance.textEdit_h.setGeometry(130,60,100,30)
    instance.textEdit_h.setText("100")

    label_v = QLabel(instance.widegt_resize_ts)
    label_v.setGeometry(30, 90, 100, 30)
    label_v.setText("竖直(V)：")

    instance.textEdit_v = QTextEdit(instance.widegt_resize_ts)
    instance.textEdit_v.setGeometry(130,90,100,30)
    instance.textEdit_v.setText("100")

    button_resize_h_v=QPushButton("确定",instance.widegt_resize_ts)
    button_resize_h_v.setGeometry(70,150,100,30)
    button_resize_h_v.clicked.connect(instance.signal_resize_button_clicked)

def change_size_button_clicked(instance):
    var_1=int(instance.textEdit_v.toPlainText())
    var_2=int(instance.textEdit_h.toPlainText())
    temp_image=instance.m_image
    print(var_1/100.0,var_2/100.0)
    if instance.cb_percent_bool.isChecked()==True:
        instance.m_image=cv.resize(temp_image,None,fx=var_2/100.0, fy=var_1/100.0, interpolation = cv.INTER_CUBIC)
    if instance.cb_piexl_bool.isChecked()==True:
        instance.m_image=cv.resize(temp_image,(var_2,var_1), interpolation = cv.INTER_CUBIC)
    instance.updata_image()

def state_change_cb_pix_percent(instance,type):
    if type==2:
        instance.cb_percent_bool.setObjectName("temp")

        instance.textEdit_h.setText(str(instance.m_image.shape[1]))
        instance.textEdit_v.setText(str(instance.m_image.shape[0]))

        instance.cb_piexl_bool.setEnabled(False)
        instance.cb_percent_bool.setEnabled(True)
        instance.cb_percent_bool.setChecked(False)

        instance.cb_percent_bool.setObjectName("cb_percent_bool")
    if type==1:
        instance.cb_piexl_bool.setObjectName("temp")

        instance.cb_percent_bool.setEnabled(False)
        instance.cb_piexl_bool.setEnabled(True)
        instance.cb_piexl_bool.setChecked(False)

        instance.textEdit_h.setText("100")
        instance.textEdit_v.setText("100")
        instance.cb_piexl_bool.setObjectName("cb_piexl_bool")


def init_edit_widget_second(instance):
    instance.widegt_edit_second = QWidget()
    instance.widegt_edit_second.setGeometry(300, 300, 400, 600)

    rotate_ccw_button=QPushButton(instance.widegt_edit_second)
    rotate_ccw_button.setIcon(creat_icon(instance.root_path+"/part1/ccw.jfif",40,40))
    rotate_ccw_button.setIconSize(QSize(40,40))
    rotate_ccw_button.setGeometry(40,40,40,40)
    rotate_ccw_button.setObjectName("rotate_ccw_button")
    rotate_ccw_button.clicked.connect(instance.signal_rotate_emit)

    rotate_cw_button=QPushButton(instance.widegt_edit_second)
    rotate_cw_button.setIcon(creat_icon(instance.root_path+"/part1/cw.jfif",40,40))
    rotate_cw_button.setIconSize(QSize(40,40))
    rotate_cw_button.setGeometry(90,40,40,40)
    rotate_cw_button.setObjectName("rotate_cw_button")
    rotate_cw_button.clicked.connect(instance.signal_rotate_emit)

    button_painter_rect=QPushButton(instance.widegt_edit_second)
    button_painter_rect.clicked.connect(instance.signal_button_painter_rect)
def button_action_painter_rect(self):
    painter = QPainter(self.widegt_edit_second)
    painter.begin(self.widegt_edit_second)

    pen = QPen(Qt.red, 3, Qt.SolidLine)  # 直线

    painter.setPen(pen)
    painter.drawLine(20, 40, 2500, 4000)

    pen.setStyle(Qt.DashLine)  # 线虚线
    painter.setPen(pen)
    painter.drawLine(20, 80, 2500, 800)

    pen.setStyle(Qt.DashDotDotLine)  # 双点划线
    painter.setPen(pen)
    painter.drawLine(20, 120, 2500, 1200)

    pen.setStyle(Qt.DotLine)  # 点虚线
    painter.setPen(pen)
    painter.drawLine(20, 160, 250, 160)

    pen.setStyle(Qt.DashDotDotLine)
    painter.setPen(pen)
    painter.drawLine(20, 200, 250, 200)

    pen.setStyle(Qt.CustomDashLine)  # 自定义点划线
    pen.setDashPattern([1, 10, 5, 8])
    painter.setPen(pen)
    painter.drawLine(20, 240, 250, 240)

    painter.end()


def creat_icon(path,w,h):
    img_ccw = QImage(path)
    pixmap_ccw = QPixmap(img_ccw)
    fitPixmap_ccw = pixmap_ccw.scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
    icon_ccw = QIcon(fitPixmap_ccw)
    return icon_ccw

def rotate_action(instance,angle):
    instance.m_image = rotate_bound(instance.m_image,angle)
    instance.updata_image()


def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv.warpAffine(image, M, (nW, nH))



