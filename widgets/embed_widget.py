from PyQt5 import QtWidgets
from widgets.tab_widget import TabWidget
from widgets import embed_widget_ui

class EmbedWidget(TabWidget, embed_widget_ui.Ui_Form):
    def __init__(self):
        super(EmbedWidget, self).__init__(self)