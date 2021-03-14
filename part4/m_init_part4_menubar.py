from PyQt5.QtWidgets import QAction,QWidget,QPushButton
from part4 import segmentation_human
def init_part4_menubar(instance):
    # 连接信号，当该信号被发射后执行括号内被连接函数
    instance.signal_part4_segmentation_human.connect(segmentation_human.segmentation_human_function)

    # 创建一个窗口，定义位置，标题等属性
    instance.widget_segmentation_human=QWidget()
    instance.widget_segmentation_human.setGeometry(300, 300, 280, 170)
    instance.widget_segmentation_human.setWindowTitle('抠图（人像）')

    # 创建一个按钮，该按钮的父对象为instance.widget_segmentation_human
    # 当该按钮被点击时执行信号发射函数
    instance.button_widget_segmentation_human=QPushButton("执行",instance.widget_segmentation_human)
    instance.button_widget_segmentation_human.setGeometry(30, 30, 50, 50)
    instance.button_widget_segmentation_human.clicked.connect(instance.signal_segmentation_human_emit)

    # 创建一个action，当该action被触发时运行show_segmentation_human_widget
    # show_segmentation_human_widget的作用为显示抠图操作窗口widget_segmentation_human
    action_segmentation_human_widget_show = QAction('&抠图/人像', instance)
    action_segmentation_human_widget_show.triggered.connect(instance.show_segmentation_human_widget)

    # 新增一个菜单选项：Part4
    # Part4选项新增一个Action：抠图（人像）
    menubar = instance.menuBar()
    tempMenu = menubar.addMenu('&Part4')
    tempMenu.addAction(action_segmentation_human_widget_show)