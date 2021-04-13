from part1 import  m_edit,file_function_define,resize_widget,rotate_function,painter_widegt,text_input_widegt
def signal_emit_name(self,name):

    if name=="Resize_button":
        resize_widget.change_size_button_clicked(self)
    elif name=="Gray_Change_Action":
        file_function_define.gray_process(self)
    elif name=="Inv_Color":
        file_function_define.inverse_color(self)
    elif name=="button_threshold":
        file_function_define.threshold_processing(self)
    elif name=="cb_percent_bool" or "cb_piexl_bool":
        if name=="cb_percent_bool":
            resize_widget.state_change_cb_pix_percent(self, 1)
        if name=="cb_piexl_bool":
            resize_widget.state_change_cb_pix_percent(self, 2)

    if name=="rotate_cw_action" or "rotate_cw_button":
        rotate_function.rotate_action(self, 90.0)
    elif name=="rotate_ccw_action" or "rotate_ccw_button":
        rotate_function.rotate_action(self, -90.0)

def signal_draw_emit_name(self,name):
    if name=="painter_button_draw_Rect":
        self.drawRect_able=True
        self.drawBreak=True
    elif name=="painter_button_draw_Line":
        self.drawLine_able=True
        self.drawBreak = True
    elif name=="painter_button_draw_Circle":
        self.drawCircle_able=True
        self.drawBreak = True
    elif name=="painter_button_draw_Ellipse":
        self.drawEllipse_able=True
        self.drawBreak = True
    elif name=="painter_button_draw_LeftRow":
        self.drawLeftRow_able=True
        self.drawBreak = True

    if name=="painter_button_draw_LineAsPen":
        self.drawLineAsPen_able=True
        self.drawConti = True
    elif name=="painter_button_draw_Erase":
        self.drawErase_able=True
        self.drawConti = True

    if name=="button_get_color":
        painter_widegt.change_color_action(self)
    elif name=="button_use_pen":
        self.button_use_pen_bool = True
        self.button_use_brush_bool = False
    elif name=="button_use_brush":
        self.button_use_pen_bool = False
        self.button_use_brush_bool = True
    elif name == "le_painter_pen_size":
        self.qpen.setWidth(int(self.le_painter_pen_size.text()))

def signal_part1_reat_emit_by_name(self,name):
    if name=="text_input_button":
        text_input_widegt.text_line_edit_init(self)
    elif name=="button_get_color_text_input":
        text_input_widegt.change_input_color_action(self)
    elif name == "button_get_font_text_input":
        text_input_widegt.change_input_font_action(self)
    elif name=="pic_cut_action":
        self.pic_cut_bool=True
        self.drawBreak=True
