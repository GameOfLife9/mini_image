import cv2 as cv
def blur(intstance,type,value):
    if type==0:
        intstance.m_image=cv.blur(intstance.m_image,(value,value))
    intstance.updata_image()