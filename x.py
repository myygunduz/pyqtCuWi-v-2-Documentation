import sys
import os
from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout,QComboBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Dosya(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        combo = QComboBox(self)
        self.baslat = QPushButton("dosya aç ")
        self.ara= QPushButton("arat")
        self.icerikler = QTextEdit()
        self.istek = QLineEdit()
        self.yazdir = QPushButton("yazdır")
        self.uyari = QLabel(">Dosya adı girerken uzantsını yandan seçebilirsiniz\n>Eğer uzantı yoksa aradığınız dosya türü yoktur")
        self.temizle = QPushButton("temizle")
        self.geri_bildirim = QLabel("")


        combo.addItem(".jpg")
        combo.addItem(".txt")
        combo.addItem(".exe")
        combo.addItem(".py")



        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.istek)
        h_box.addWidget(combo)
        h_box.addWidget(self.baslat)
        h_box.addWidget(self.yazdir)
        h_box.addWidget(self.temizle)
        h_box.addStretch()

        v_box =QVBoxLayout()
        v_box.addWidget(self.icerikler)
        v_box.addStretch()
        v_box.addWidget(self.uyari)
        v_box.addStretch()
        v_box.addLayout(h_box)

        v_box.addWidget(self.ara)

        v_box.addWidget(self.geri_bildirim)
        v_box.addStretch()

        self.setLayout(v_box)


        combo.activated[str].connect(self.onActivated)
        self.baslat.clicked.connect(self.dosya_ac)
        self.yazdir.clicked.connect(self.yazici)
        self.temizle.clicked.connect(self.temizleyici)
        self.ara.clicked.connect(self.aranan_dosya)


        self.setGeometry(400,150,600,600)
        self.setWindowTitle('Dosya tarayıcı')
        self.show()

    def onActivated(self, text):

        self.istenen_dosya="{}{}".format(self.istek.text(),str(text))
        


    def dosya_ac(self):
        print(os.getcwd())
        dosya_ismi = QFileDialog.getOpenFileName(self,"dosya aranıyor",os.getenv("Masaüstü"))
        self.istenen_dosya=dosya_ismi[0]
        if(self.istenen_dosya.endswith(".jpg") or self.istenen_dosya.endswith(".png") or self.istenen_dosya.endswith(".jpeg")):
            self.geri_bildirim.setText("resim dosyası açıldı")
            self.icerikler.setHtml("<img src='{}'>".format(self.istenen_dosya))

        else:
            with open(self.istenen_dosya,"r") as file:
                self.icerikler.setText(file.read())

    def yazici(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, "dosya kaydet",
                                                 os.getenv("Desktop"))  # dosyayı kaydet modunda açarız

        with open(dosya_ismi[0], "w")as file:
            file.write(self.icerikler)
    def temizleyici(self):
        self.istek.clear()
        self.icerikler.clear()

    def aranan_dosya(self):
        if(os.path.exists(self.istenen_dosya)):
            self.geri_bildirim.setText("dosya mevcuttur")
            #if file's extension is py,txt,json open and write
            #if file's extension is jpg, png, jpeg open and show
            if(self.istenen_dosya.endswith(".jpg") or self.istenen_dosya.endswith(".png") or self.istenen_dosya.endswith(".jpeg")):
                self.geri_bildirim.setText("resim dosyası açıldı")
                self.icerikler.setHtml("<img src='{}'>".format(self.istenen_dosya))
            else:
                with open(self.istenen_dosya,"r") as file:
                    self.icerikler.setText(file.read())
            

        else:
            self.geri_bildirim.setText("dosya bulunamadı dosya konumunu değiştirin")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dosya()
    sys.exit(app.exec_())