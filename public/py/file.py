#import Module
import PyQtCuWi2 as CuWi
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

#create window
app = QApplication([])
win = QWidget()

#create layout
layout = QVBoxLayout()
win.setLayout(layout)

#create QInput Widget
file = CuWi.QInput(CuWi.QType.QInputType.FILE)
layout.addWidget(file) #add button to layout

win.show()
app.exec()
