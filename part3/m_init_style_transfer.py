from PyQt5.QtWidgets import QAction,QWidget,QPushButton
from part3 import neural_style_transfer_core
def init_style_transfer_menubar(instance):
    # 连接信号，当该信号被发射后执行括号内被连接函数
    instance.signal_neural_style_transfer.connect(neural_style_transfer_core.neual_style_transfer)

    # 创建一个窗口，定义位置，标题等属性
    instance.widget_neural_style_transfer=QWidget()
    instance.widget_neural_style_transfer.setGeometry(300, 300, 280, 170)
    instance.widget_neural_style_transfer.setWindowTitle('基于神经网络的风格迁移')

    # 创建一个按钮，该按钮的父对象为instance.widget_neural_style_transfer
    # 当该按钮被点击时执行信号发射函数
    instance.button_neural_style_stop=QPushButton("开始",instance.widget_neural_style_transfer)
    instance.button_neural_style_stop.setGeometry(30, 30, 50, 50)
    instance.button_neural_style_stop.clicked.connect(instance.signal_neural_style_emit)

    # 创建一个action，当该action被触发时运行show_neural_style_transfer_widget
    # show_neural_style_transfer_widget的作用为显示风格迁移操作窗口widget_neural_style_transfer
    action_neural_style_widget_show = QAction('&基于神经网络的风格迁移', instance)
    action_neural_style_widget_show.triggered.connect(instance.show_neural_style_transfer_widget)

    # 新增一个菜单选项：艺术风格迁移
    # 艺术风格迁移选项新增一个Action：基于神经网络的风格迁移
    menubar = instance.menuBar()
    tempMenu = menubar.addMenu('&艺术风格迁移')
    tempMenu.addAction(action_neural_style_widget_show)