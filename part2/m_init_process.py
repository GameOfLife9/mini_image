from PyQt5.QtWidgets import QAction,QMenu,QWidget,QSlider,QLabel,QPushButton
from PyQt5.QtCore import Qt
from part2 import m_blur
def init_menu(instance):
    # 连接信号，当该信号被发射后执行括号内被连接函数
    instance.signal_processing_bar_blur.connect(m_blur.blur)

    # 创建一个窗口，定义位置，标题等属性
    instance.widegt_mean_blur=QWidget()
    instance.widegt_mean_blur.setWindowTitle('均值模糊')

    # 创建一个滑动条，当该滑动条拖动释放时发射信号
    instance.sld_mean_blur=QSlider(Qt.Horizontal, instance.widegt_mean_blur)
    instance.sld_mean_blur.setGeometry(30, 40, 100, 30)
    instance.sld_mean_blur.sliderReleased.connect(instance.signal_blur_emit)

    # 为滑动条设置最小最大值，初始值等属性
    instance.sld_mean_blur.setMinimum(3)
    instance.sld_mean_blur.setMaximum(11)
    instance.sld_mean_blur.setSingleStep(2)
    instance.sld_mean_blur.setValue(3)

    # 设置object name(可选)，主要是在某些情况下可以根据信号源的object name来选择下一步操作
    instance.sld_mean_blur.setObjectName("mean_blur")

    # 创建一个action，当该action被触发时运行mean_blur_widegt_show
    # mean_blur_widegt_show的作用为显示模糊操作窗口widegt_mean_blur
    blur_mean_action = QAction('&均值模糊', instance)
    blur_mean_action.triggered.connect(instance.mean_blur_widegt_show)

    # 添加一个菜单：模糊，这个菜单在后面被添加成图像选项的子选项
    # 为该选项添加一个action blur_mean_action
    change_menu = QMenu('模糊', instance)
    change_menu.addAction(blur_mean_action)

    # 新增一个菜单选项：图像
    # 图像选项新增一个子菜单模糊
    menubar = instance.menuBar()
    editMenu = menubar.addMenu('&图像')
    editMenu.addMenu(change_menu)
