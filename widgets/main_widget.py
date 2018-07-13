from PyQt5 import QtWidgets
from widgets.tab_widget import TabWidget
from widgets import main_widget_ui

class MainWidget(TabWidget, main_widget_ui.Ui_MainWidget):
    def __init__(self, sample, params):
        super(MainWidget, self).__init__(self)
        self.testNameLabel.setText(sample.getName()+":")
        self.dateLabel.setText(sample.getDate())
        self.limitLabel.setText(str(sample.getStandard()))
        if len(params) > 0:
            self.passLabel.setText("Fail")
        else:
            self.passLabel.setText("Pass")
        self.failsLabel.setText(str(params))