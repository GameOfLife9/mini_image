import cv2 as cv
from PyQt5.QtGui import QPixmap,QImage
from PyQt5.QtWidgets import QLabel
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
    self.lbl.setScaledContents(True)
    self.lbl.setGeometry(0, 0, self.m_image_width, self.m_image_height)

    self.setGeometry(300, 300, self.m_image_width + 10, self.m_image_height + 10)

def image_update(self):
    print(self.m_image.shape)
    self.m_QImage = QImage(self.m_image[:], self.m_image.shape[1], self.m_image.shape[0], self.m_image.shape[1] * 3,
                           QImage.Format_RGB888)

    self.m_image_width = 600
    self.m_image_height = self.m_image.shape[0] / self.m_image.shape[1] * self.m_image_width

    #self.m_image_width = self.m_image.shape[1]
    #self.m_image_height = self.m_image.shape[0]

    self.pixmap = QPixmap(self.m_QImage)

    self.lbl.setPixmap(self.pixmap)
    self.lbl.resize(self.m_image_width, self.m_image_height)
    self.lbl.setScaledContents(True)
    self.lbl.setGeometry(0, 0, self.m_image_width, self.m_image_height)

    self.setGeometry(300, 300, self.m_image_width+10, self.m_image_height+10)