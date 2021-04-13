from PyQt5.QtGui import QPainter,QPixmap,QPen,QBrush,QPolygon,QColor, QFont
from PyQt5.QtCore import Qt,QPoint
def m_paint_evet(self,event):

    x = self.startPoint.x()
    y = self.startPoint.y() + 16
    now_x = self.endPoint.x()
    now_y = self.endPoint.y() + 16
    w = now_x - x
    h = now_y - y
    x_last = self.lastPoint.x()
    y_last = self.lastPoint.y() + 16

    if self.drawBreak:

        self.temp = self.pixmap.copy()
        pp = QPainter(self.temp)
        if self.pic_cut_bool:
            #print("asad")
            pp.drawRect(x, y, w, h)
            #return
        if self.button_use_pen_bool:
            pp.setPen(self.qpen)
        elif self.button_use_brush_bool:
            pp.setBrush(self.qbrush)
        else:
            print("erro:in paint_event.py")
        if self.drawRect_able:
            pp.drawRect(x, y, w, h)

        elif self.drawLine_able:
            pp.drawLine(x, y, now_x, now_y)

        elif self.drawCircle_able:
            pp.drawEllipse(x, y, (w * w + h * h) ** 0.5, (w * w + h * h) ** 0.5)
        elif self.drawEllipse_able:
            pp.drawEllipse(x, y, w, h)
        elif self.drawLeftRow_able:

            points = QPolygon([QPoint(x, y + h * 0.5), QPoint(x + w * 0.5, now_y), QPoint(x + w * 0.5, y + h * 0.75),
                               QPoint(now_x, y + h * 0.75), QPoint(now_x, y + h * 0.25),
                               QPoint(x + w * 0.5, y + h * 0.25), QPoint(x + w * 0.5, y)])

            pp.drawPolygon(points)
        painter = QPainter(self.lbl.pixmap())
        painter.drawPixmap(0, 0, self.temp)
    elif self.drawConti:
        if self.drawLineAsPen_able:
            painter = QPainter(self.lbl.pixmap())
            painter.setPen(self.qpen)
            painter.drawLine(x_last, y_last, now_x, now_y)
            painter.end()
        elif self.drawErase_able:
            painter = QPainter(self.lbl.pixmap())
            mpen = QPen()
            mpen.setColor(Qt.white)
            mpen.setWidth(10)
            painter.setPen(mpen)
            painter.drawPoint(now_x, now_y)
            painter.end()
