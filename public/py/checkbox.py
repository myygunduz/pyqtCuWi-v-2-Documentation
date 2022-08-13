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
checkbox = CuWi.QInput(CuWi.QType.QInputType.CHECKBOX, "Checkbox 1")
layout.addWidget(checkbox) #add button to layout

checkbox2 = CuWi.QInput(CuWi.QType.QInputType.CHECKBOX, "Checkbox 2")
layout.addWidget(checkbox2) #add button to layout

win.show()
app.exec()
