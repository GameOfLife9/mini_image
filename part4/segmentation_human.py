'''
import cv2
import base64
import numpy as np

from aip import AipBodyAnalysis
def segmentation_human_function(instance):
    APP_ID = '23794757'
    API_KEY = 'f8G7GcANwLie5tbdQTEGWXmT'
    SECRET_KEY = 'nz2PH3Vx3Ph3xMW7CTchEXbrKt2Qp6OW'

    client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

    imgfile = instance.root_path+'/part4/images/test.jpg'
    ori_img = cv2.imread(imgfile)
    height, width, _ = ori_img.shape

    with open(imgfile, 'rb') as fp:
        img_info = fp.read()

    seg_res = client.bodySeg(img_info)
    labelmap = base64.b64decode(seg_res['labelmap'])
    nparr = np.fromstring(labelmap, np.uint8)
    labelimg = cv2.imdecode(nparr, 1)
    labelimg = cv2.resize(labelimg, (width, height), interpolation=cv2.INTER_NEAREST)
    new_img = np.where(labelimg == 1, 255, labelimg)
    maskfile = imgfile.replace('.jpg', '_mask.png')
    cv2.imwrite(maskfile, new_img)

    res_imgfile = imgfile.replace('.jpg', '_res.jpg')
    result = cv2.bitwise_and(ori_img, new_img)
    cv2.imwrite(res_imgfile, result)
'''
def segmentation_human_function(instance):
    print(" ")