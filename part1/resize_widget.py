from PyQt5.QtWidgets import QWidget,QCheckBox,QLabel,QTextEdit,QPushButton
import cv2 as cv
def init_resize_widget(instance):
    instance.widegt_resize_ts = QWidget()
    instance.widegt_edit_second.setGeometry(300, 300, 600, 500)

    instance.cb_percent_bool = QCheckBox('百分比', instance.widegt_resize_ts)
    instance.cb_percent_bool.setChecked(True)
    instance.cb_percent_bool.setGeometry(30,30,100,30)
    instance.cb_percent_bool.setObjectName("cb_percent_bool")
    instance.cb_percent_bool.stateChanged.connect(instance.signal_emit_by_name)
    instance.cb_percent_bool.setEnabled(False)

    instance.cb_piexl_bool = QCheckBox('像素', instance.widegt_resize_ts)
    instance.cb_piexl_bool.setChecked(False)
    instance.cb_piexl_bool.setGeometry(120,30,100,30)
    instance.cb_piexl_bool.setObjectName("cb_piexl_bool")
    instance.cb_piexl_bool.stateChanged.connect(instance.signal_emit_by_name)
    instance.cb_piexl_bool.setEnabled(True)

    label_h=QLabel(instance.widegt_resize_ts)
    label_h.setGeometry(30,60,100,30)
    label_h.setText("水平(H)：")

    instance.textEdit_h = QTextEdit(instance.widegt_resize_ts)
    instance.textEdit_h.setGeometry(130,60,100,30)
    instance.textEdit_h.setText("100")

    label_v = QLabel(instance.widegt_resize_ts)
    label_v.setGeometry(30, 90, 100, 30)
    label_v.setText("竖直(V)：")

    instance.textEdit_v = QTextEdit(instance.widegt_resize_ts)
    instance.textEdit_v.setGeometry(130,90,100,30)
    instance.textEdit_v.setText("100")

    button_resize_h_v=QPushButton("确定",instance.widegt_resize_ts)
    button_resize_h_v.setGeometry(70,150,100,30)
    button_resize_h_v.setObjectName("Resize_button")
    button_resize_h_v.clicked.connect(instance.signal_emit_by_name)

def state_change_cb_pix_percent(instance,type):
    if type==2:
        instance.cb_percent_bool.setObjectName("temp")

        instance.textEdit_h.setText(str(instance.m_image.shape[1]))
        instance.textEdit_v.setText(str(instance.m_image.shape[0]))

        instance.cb_piexl_bool.setEnabled(False)
        instance.cb_percent_bool.setEnabled(True)
        instance.cb_percent_bool.setChecked(False)

        instance.cb_percent_bool.setObjectName("cb_percent_bool")
    if type==1:
        instance.cb_piexl_bool.setObjectName("temp")

        instance.cb_percent_bool.setEnabled(False)
        instance.cb_piexl_bool.setEnabled(True)
        instance.cb_piexl_bool.setChecked(False)

        instance.textEdit_h.setText("100")
        instance.textEdit_v.setText("100")
        instance.cb_piexl_bool.setObjectName("cb_piexl_bool")

def change_size_button_clicked(instance):
    var_1=int(instance.textEdit_v.toPlainText())
    var_2=int(instance.textEdit_h.toPlainText())
    temp_image=instance.m_image
    print(var_1/100.0,var_2/100.0)
    if instance.cb_percent_bool.isChecked()==True:
        instance.m_image=cv.resize(temp_image,None,fx=var_2/100.0, fy=var_1/100.0, interpolation = cv.INTER_CUBIC)
    if instance.cb_piexl_bool.isChecked()==True:
        instance.m_image=cv.resize(temp_image,(var_2,var_1), interpolation = cv.INTER_CUBIC)
    instance.updata_image()