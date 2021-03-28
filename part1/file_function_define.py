import cv2 as cv
def gray_process(instance):
    temp_image=cv.cvtColor(instance.m_image,cv.COLOR_RGB2GRAY)
    instance.m_image[:, :, 0] = temp_image
    instance.m_image[:, :, 1] = temp_image
    instance.m_image[:, :, 2] = temp_image
    instance.updata_image()

def inverse_color(instance):
    instance.m_image=255-instance.m_image
    instance.updata_image()

def threshold_processing(instance):
    ret,thresh1 = cv.threshold(instance.m_image,int(instance.textEdit_threshold.toPlainText()),255,cv.THRESH_BINARY)
    instance.m_image=thresh1
    instance.updata_image()
