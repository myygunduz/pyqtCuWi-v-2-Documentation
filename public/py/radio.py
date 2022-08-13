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
radiobutton = CuWi.QInput(CuWi.QType.QInputType.RADIO, "RadioButton 1")
radiobutton.addGroup("Group1")
layout.addWidget(radiobutton) #add button to layout

radiobutton2 = CuWi.QInput(CuWi.QType.QInputType.RADIO, "RadioButton 2")
radiobutton2.addGroup("Group1")
layout.addWidget(radiobutton2) #add button to layout

win.show()
app.exec()
