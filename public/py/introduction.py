#import Module
import PyQtCuWi2 as CuWi
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

#create window
app = QApplication([])
win = QWidget()

#create layout
layout = QHBoxLayout()
win.setLayout(layout)

#create QInput Widget
button = CuWi.QInput(CuWi.QType.QInputType.BUTTON, "Button")
layout.addWidget(button) #add button to layout

win.show()
app.exec()
