#import Module
import PyQtCuWi2 as CuWi
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout

#create window
app = QApplication([])
win = QWidget()

#create layout
layout = QHBoxLayout()
win.setLayout(layout)

#create QMedia Widget
media = CuWi.QMedia('./pyqtcuwi.png')
media.setFixedHeight(100)
layout.addWidget(media) #add media to layout

win.show()
app.exec()
