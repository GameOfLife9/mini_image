import core.m_ui as m_ui

if __name__ == '__main__':
    app = m_ui.QApplication(m_ui.sys.argv)
    ex = m_ui.main_widget()
    m_ui.sys.exit(app.exec_())