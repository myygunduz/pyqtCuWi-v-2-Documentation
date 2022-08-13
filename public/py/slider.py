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
slider = CuWi.QInput(CuWi.QType.QInputType.SLIDER, minVal = 0, maxVal = 100)
layout.addWidget(slider) #add button to layout

win.show()
app.exec()
