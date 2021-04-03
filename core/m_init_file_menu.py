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

    #文件保存
    save_file_Action = QAction('&保存', self)
    save_file_Action.triggered.connect(self.signal_save_file_emit)

    self.statusBar()
    menubar = self.menuBar()


    fileMenu = menubar.addMenu('&文件')

    fileMenu.addAction(exitAction)
    fileMenu.addAction(open_file_Action)
    fileMenu.addAction(save_file_Action)

def open_file(self):
    open_file_path = QFileDialog.getOpenFileNames(self, '选择文件',self.root_path,"photo(*.jpg *.png)")

    if open_file_path[0] is not None:
        new_image=cv.imread(open_file_path[0][0])
        new_image=cv.cvtColor(new_image, cv.COLOR_BGR2RGB)
        self.m_image = new_image
        #print(self.m_image.shape)

        self.updata_image()

def save_file(self):
    save_file_path=QFileDialog.getSaveFileName(self,"保存",self.root_path ,".jpg;;")
    if save_file_path is not None:
        temp_image=cv.cvtColor(self.m_image, cv.COLOR_RGB2BGR)
        cv.imwrite(save_file_path[0]+save_file_path[1],temp_image)
        print(save_file_path)