
from PySide2.QtWidgets import (QPushButton,
                               QVBoxLayout, QWidget, QLineEdit)
from PySide2.QtCore import Slot

from processingurls import ProcessingUrl


class URLForm(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # create a textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 25)
        self.textbox.resize(200, 200)

        # create a button
        self.button = QPushButton("Send", self)
        self.button.move(20, 300)
        self.layout = QVBoxLayout()

        # add the button and the textbox to the layout
        self.layout.addWidget(self.textbox)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # connect the button to onsubmit
        self.button.clicked.connect(self.onsubmit)

    @Slot()
    def onsubmit(self):
        ProcessingUrl(self.textbox.text()).asynchronous_requests()
        self.textbox.clear()
        return


