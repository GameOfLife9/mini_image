import cv2 as cv
def blur(intstance,type,value):
    #根据type的类型选择不同模糊方法，比如均值模糊，高斯模糊
    if type==0:
        intstance.m_image=cv.blur(intstance.m_image,(value,value))
    intstance.updata_image()