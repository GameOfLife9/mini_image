from PyQt5.QtWidgets import QWidget,QPushButton,QComboBox,QLabel,QColorDialog,QLineEdit
from PyQt5.QtGui import QPainter,QPixmap,QPen,QBrush,QColor
from PyQt5.QtCore import Qt,QPoint

def init_painter_widget(instance):
    instance.button_use_pen_bool = True
    instance.button_use_brush_bool = False

    init_var_painter(instance)
    setBoolFalse(instance)

    instance.widegt_painter_ts = QWidget()
    instance.widegt_painter_ts.setGeometry(300, 300, 600, 500)

    creat_button(instance, "画矩形", "painter_button_draw_Rect", 50, 50)
    creat_button(instance, "画直线", "painter_button_draw_Line", 150, 50)
    creat_button(instance, "铅笔", "painter_button_draw_LineAsPen", 250, 50)
    creat_button(instance,"画圆","painter_button_draw_Circle",350,50)
    creat_button(instance,"画椭圆","painter_button_draw_Ellipse",50,150)
    creat_button(instance,"画箭头","painter_button_draw_LeftRow",150,150)
    creat_button(instance,"橡皮擦","painter_button_draw_Erase",250,150)

    creatBrushComboBox(instance)

    instance.button_get_color=QPushButton("设置笔刷画笔颜色",instance.widegt_painter_ts)
    instance.button_get_color.setGeometry(50,300,128,64)
    instance.button_get_color.setObjectName("button_get_color")
    instance.button_get_color.clicked.connect(instance.signal_draw_emit_by_name)

    instance.color_label_painter=QLabel(instance.widegt_painter_ts)
    instance.color_label_painter.setGeometry(200,300,96,64)
    instance.color_label_painter.setStyleSheet("background-color:rgb(0,0,0)")

    button_use_pen=QPushButton("使用画笔",instance.widegt_painter_ts)
    button_use_pen.setGeometry(300,300,84,64)
    button_use_pen.setObjectName("button_use_pen")
    button_use_pen.clicked.connect(instance.signal_draw_emit_by_name)

    button_use_brush=QPushButton("使用笔刷",instance.widegt_painter_ts)
    button_use_brush.setGeometry(400,300,84,64)
    button_use_brush.setObjectName("button_use_brush")
    button_use_brush.clicked.connect(instance.signal_draw_emit_by_name)

    label_painter_pen_size=QLabel("画笔大小",instance.widegt_painter_ts)
    label_painter_pen_size.setGeometry(50,400,96,36)

    instance.le_painter_pen_size = QLineEdit("5",instance.widegt_painter_ts)
    instance.le_painter_pen_size.setGeometry(150,400,36,36)
    instance.le_painter_pen_size.setObjectName("le_painter_pen_size")
    instance.le_painter_pen_size.textChanged.connect(instance.signal_draw_emit_by_name)

def change_color_action(self):
    c = QColorDialog.getColor()
    color_r = c.getRgb()[0]
    color_g = c.getRgb()[1]
    color_b = c.getRgb()[2]
    color_a = c.getRgb()[3]
    color_str = "rgba("+str(color_r)
    color_str = color_str + "," + str(color_g)
    color_str = color_str + "," + str(color_b)
    color_str = color_str + "," + str(color_a)+")"
    self.color_label_painter.setStyleSheet("background-color:"+color_str)

    self.qpen.setColor(QColor(color_r,color_g,color_b,color_a))
    self.qbrush.setColor(QColor(color_r,color_g,color_b,color_a))
def creatBrushComboBox(instance):
    lbl_cb=QLabel("笔刷模式",instance.widegt_painter_ts)
    lbl_cb.setGeometry(50, 250, 100, 31)

    cb = QComboBox(instance.widegt_painter_ts)
    cb.setGeometry(150,250,250,31)
    cb.addItem("SolidPattern")
    cb.addItem("Nobrush")
    cb.addItem("HorPattern")
    cb.addItem("VerPattern")
    cb.addItem("CrossPattern")
    cb.addItem("BDiagPattern")
    cb.addItem("FDiagPattern")
    cb.addItem("DiagCrossPattern")
    cb.addItem("LinearPattern")
    cb.addItem("RadialGradientPattern")
    cb.addItem("ConicalGradientPattern")
    cb.addItem("Dense1Pattern")
    cb.addItem("Dense2Pattern")
    cb.addItem("Dense3Pattern")
    cb.addItem("Dense4Pattern")
    cb.addItem("Dense5Pattern")
    cb.addItem("Dense6Pattern")
    cb.addItem("Dense7Pattern")
    cb.currentIndexChanged[str].connect(instance.change_brush_pattern)

def creat_button(instance,name,ObjName,x,y):
    painter_button=QPushButton(name,instance.widegt_painter_ts)
    painter_button.setGeometry(x,y,81,81)
    painter_button.setObjectName(ObjName)
    painter_button.clicked.connect(instance.signal_draw_emit_by_name)
def init_var_painter(self):
    self.temp = QPixmap()  # 辅助画布
    self.startPoint = QPoint()  # 起点
    self.lastPoint = QPoint()
    self.endPoint = QPoint()  # 终点

    self.qpen = QPen()
    self.qpen.setWidth(5)
    self.qpen.setColor(Qt.black)

    self.qbrush = QBrush()
    self.qbrush.setStyle(Qt.VerPattern)
    self.qbrush.setColor(Qt.black)
def setBoolFalse(self):
    self.drawRect_able = False
    self.drawLine_able = False
    self.drawLineAsPen_able = False
    self.drawConti = False
    self.drawBreak = False
    self.drawCircle_able = False
    self.drawEllipse_able = False
    self.drawLeftRow_able = False
    self.drawErase_able = False

    #for pic cut
    self.pic_cut_bool=False
