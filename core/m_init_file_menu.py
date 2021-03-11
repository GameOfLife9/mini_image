from PyQt5.QtWidgets import QAction,qApp,QFileDialog
import cv2 as cv
def init_file_menu(self):
    self.signal_file_bar_openfile.connect(open_file)
    # 程序退出
    exitAction = QAction('&退出', self)
    exitAction.setShortcut('Ctrl+Q')
    exitAction.setStatusTip('Exit application')
    exitAction.triggered.connect(qApp.quit)

    # 文件打开
    open_file_Action = QAction('&打开', self)
    open_file_Action.triggered.connect(self.signal_open_file_emit)

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