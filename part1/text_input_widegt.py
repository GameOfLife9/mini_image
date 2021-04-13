from PyQt5.QtWidgets import QWidget,QPushButton,QLabel,QColorDialog,QFontDialog
from PyQt5.QtGui import QColor,QFont,QPainter
from PyQt5.QtCore import Qt,QRectF
from core import image_init_update
def init_text_widget(instance):
    instance.widegt_text_input_ts = QWidget()
    instance.widegt_text_input_ts.setGeometry(300, 300, 369, 369)

    text_input_button=QPushButton("添加文字",instance.widegt_text_input_ts)
    text_input_button.setGeometry(50,50,81,81)
    text_input_button.setObjectName("text_input_button")
    text_input_button.clicked.connect(instance.signal_part1_reat_emit_by_name)

    button_get_color_text_input=QPushButton("文字颜色",instance.widegt_text_input_ts)
    button_get_color_text_input.setGeometry(50,150,128,64)
    button_get_color_text_input.setObjectName("button_get_color_text_input")
    button_get_color_text_input.clicked.connect(instance.signal_part1_reat_emit_by_name)

    instance.color_label_text_input=QLabel(instance.widegt_text_input_ts)
    instance.color_label_text_input.setGeometry(200,150,96,64)
    instance.color_label_text_input.setStyleSheet("background-color:rgb(0,0,0)")

    button_get_font_text_input=QPushButton("字体设置",instance.widegt_text_input_ts)
    button_get_font_text_input.setGeometry(50,250,128,64)
    button_get_font_text_input.setObjectName("button_get_font_text_input")
    button_get_font_text_input.clicked.connect(instance.signal_part1_reat_emit_by_name)

    #for text input init var
    instance.drawing=False
    instance.drawToImage=False

    instance.qp_text_input = QPainter(instance.lbl.pixmap())
    instance.qp_text_input.setPen(QColor(0, 0, 0))
    instance.font_dialog=QFontDialog(instance)
    instance.qp_text_input.setFont(instance.font_dialog.currentFont())

    instance.label_text_input_font_fam=QLabel("字体:"+str(instance.font_dialog.currentFont().family()),instance.widegt_text_input_ts)
    instance.label_text_input_font_fam.setGeometry(200,240,128,32)

    instance.label_text_input_font_style=QLabel("样式:"+str(instance.font_dialog.currentFont().style()),instance.widegt_text_input_ts)
    instance.label_text_input_font_style.setGeometry(200,260,96,32)

    instance.label_text_input_font_size=QLabel("大小:"+str(instance.font_dialog.currentFont().pointSize()),instance.widegt_text_input_ts)
    instance.label_text_input_font_size.setGeometry(200,280,96,32)


def change_input_font_action(self):

    res=self.font_dialog.exec()
    self.qp_text_input.setFont(self.font_dialog.currentFont())
    self.label_text_input_font_fam.setText("字体:"+str(self.font_dialog.currentFont().family()))
    self.label_text_input_font_style.setText("样式:"+str(self.font_dialog.currentFont().style()))
    self.label_text_input_font_size.setText("大小:" + str(self.font_dialog.currentFont().pointSize()))

def change_input_color_action(self):
    c = QColorDialog.getColor()
    color_r = c.getRgb()[0]
    color_g = c.getRgb()[1]
    color_b = c.getRgb()[2]
    color_a = c.getRgb()[3]
    color_str = "rgba(" + str(color_r)
    color_str = color_str + "," + str(color_g)
    color_str = color_str + "," + str(color_b)
    color_str = color_str + "," + str(color_a) + ")"
    self.color_label_text_input.setStyleSheet("background-color:" + color_str)

    self.qp_text_input.setPen(QColor(color_r, color_g, color_b, color_a))

def text_line_edit_init(self):
    self.drawing = True
    self.setCursor(Qt.IBeamCursor)

#TODO: dont forget change ctrl to enter
def enter_key_press_event(self,event):

    self.qp_text_input.begin(self)
    #self.qp_text_input.setFont(self.font_text_input)
    qrf = QRectF(self.label_text_input.geometry().topLeft(), self.label_text_input.geometry().bottomRight())
    self.label_text_input.setGeometry(0, 0, 0, 0)
    self.qp_text_input.drawText(qrf, Qt.AlignCenter, self.label_text_input.toPlainText())
    self.label_text_input.setText("")
    self.qp_text_input.end()
    self.m_image = image_init_update.qtpixmap_to_cvimg(self.lbl.pixmap())
    self.updata_image()
    self.drawToImage = False