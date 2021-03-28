from PyQt5.QtWidgets import QWidget,QSlider,QLabel,QAction,QMenu
from PyQt5.QtCore import Qt
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
    instance.sld_hsv_h = QSlider(Qt.Horizontal, instance.widegt_hsv)
    instance.sld_hsv_h.setGeometry(30, 40, 100, 30)
    instance.sld_hsv_h.sliderReleased.connect(instance.hsv_signal_emit)

    # 为滑动条设置最小最大值，初始值等属性
    instance.sld_hsv_h.setMinimum(-100)
    instance.sld_hsv_h.setMaximum(100)
    instance.sld_hsv_h.setSingleStep(1)
    instance.sld_hsv_h.setValue(0)

    # 设置object name(可选)，主要是在某些情况下可以根据信号源的object name来选择下一步操作
    instance.sld_hsv_h.setObjectName("sld_hsv_h")

    # 为该滑动条添加一个label，它的父对象为instance.widegt_hsv
    instance.widegt_hsv.label_hsv_h = QLabel(instance.widegt_hsv)
    instance.widegt_hsv.label_hsv_h.setText("色调")
    instance.widegt_hsv.label_hsv_h.setGeometry(0, 40, 30, 30)

    # --------------------------------------------------------------------slider_s（同上）
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

    # --------------------------------------------------------------------slider_v（同上）
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

    # 创建一个action，当该action被触发时运行hsv_show
    # hsv_show的作用为显示HSV调整窗口widegt_hsv
    hsv_change_action = QAction('&色相/饱和度/明度', instance)
    hsv_change_action.triggered.connect(instance.hsv_show)

    # 添加一个菜单：调整，这个菜单在后面被添加成图像选项的子选项
    # 为该选项添加一个action hsv_change_action
    change_menu = QMenu('调整', instance)
    change_menu.addAction(hsv_change_action)

    # 新增一个菜单选项：编辑
    # 编辑选项新增一个子菜单调整
    menubar = instance.menuBar()
    editMenu = menubar.addMenu('&编辑')
    editMenu.addMenu(change_menu)

