import cv2 as cv
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtWidgets import QLabel
import numpy as np
def image_init(self):
    self.m_QImage = QImage(self.m_image[:], self.m_image.shape[1], self.m_image.shape[0], self.m_image.shape[1] * 3,
                           QImage.Format_RGB888)

    self.m_image_width = 600
    self.m_image_height = self.m_image.shape[0] / self.m_image.shape[1] * self.m_image_width

    #self.m_image_width = self.m_image.shape[1]
    #self.m_image_height = self.m_image.shape[0]

    self.pixmap = QPixmap(self.m_QImage)

    self.lbl = QLabel(self)
    self.lbl.setPixmap(self.pixmap)
    self.lbl.resize(self.m_image_width, self.m_image_height)
    self.lbl.setGeometry(0, 0, self.m_image_width, self.m_image_height)

    self.setGeometry(300, 300, self.m_image_width + 10, self.m_image_height + 10)


def image_update(self):
    self.m_QImage = QImage(self.m_image[:], self.m_image.shape[1], self.m_image.shape[0], self.m_image.shape[1] * 3,
                           QImage.Format_RGB888)

    self.m_image_width = 600
    self.m_image_height = self.m_image.shape[0] / self.m_image.shape[1] * self.m_image_width

    #self.m_image_width = self.m_image.shape[1]
    #self.m_image_height = self.m_image.shape[0]

    self.pixmap = QPixmap(self.m_QImage)

    self.lbl.setPixmap(self.pixmap)
    self.lbl.resize(self.m_image_width, self.m_image_height)
    self.lbl.setGeometry(0, 0, self.m_image_width, self.m_image_height)

    self.setGeometry(self.geometry().x(), self.geometry().y(), self.m_image_width+10, self.m_image_height+10)



def buffer_update(self):
    self.lbl.setPixmap(self.pixmap)
    self.lbl.resize(self.m_image_width, self.m_image_height)
    self.lbl.setGeometry(0, 0, self.m_image_width, self.m_image_height)

    #self.setGeometry(self.geometry().x(), self.geometry().y(), self.m_image_width+10, self.m_image_height+10)

def qtpixmap_to_cvimg(qtpixmap):

    qimg = qtpixmap.toImage()
    temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
    temp_shape += (4,)
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]
    result=cv.cvtColor(result,cv.COLOR_BGR2RGB)
    return result