from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
import sys
import os
from mouse_to_file import *
from play_csv import *

class myWindow(QMainWindow):
    num = file_number

    def __init__(self):
        super(myWindow, self).__init__()
        self.button_record = QPushButton("record")

        self.input_play = QLineEdit()
        self.button_play = QPushButton("play")

        self.initUI()
        self.show()
    
    def initUI(self):
        layout = QGridLayout()

        layout.addWidget(self.button_record, 0, 0)
        self.button_record.pressed.connect(self.button_record_pressed)
        
        layout.addWidget(self.input_play, 0, 1)
        self.input_play.textChanged.connect(self.input_play_change)
        layout.addWidget(self.button_play, 0, 2)
        self.button_play.pressed.connect(self.button_play_pressed)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def button_record_pressed(self):
        events = record_mouse()
        print(events)
        id = find_csv_ind()
        print(id)
        events_to_csv(events[1:], id)

    def input_play_change(self, text):
        self.num = int(text)
        
    def button_play_pressed(self):
        draw_csv(self.num)

def window():
    app = QApplication(sys.argv)
    win = myWindow()

    sys.exit(app.exec())

window()