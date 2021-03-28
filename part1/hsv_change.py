import cv2 as cv
def hsv_change_fun(instance,type,h):
    image=cv.cvtColor(instance.m_image, cv.COLOR_RGB2HSV)
    row = image.shape[0]
    col = image.shape[1]

    for i in range(0,row-1):
        for j in range(0,col-1):
            image[i][j][type]=image[i][j][type]+h

            if type==0:
                if image[i][j][type]>179:
                    image[i][j][type]=179
            else:
                if image[i][j][type]>255:
                    image[i][j][type]=255

            if image[i][j][type] < 0:
                image[i][j][type] = 0

    instance.m_image=cv.cvtColor(image, cv.COLOR_HSV2RGB)
    instance.updata_image()