import sys
from PyQt5.QtWidgets import QApplication
from giris_ui import Ui_MainWindow

from PyQt5.QtWidgets import *

class ui_windows(QMainWindow):
    def __init__(self):
        super(ui_windows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_secildi = False

        self.giris_sayfa_index = 0
        self.kayit_sayfa_index = 1
        self.bilgi_sayfa_index = 2

        self.ui.kayit_btn.clicked.connect(self.kayit_sayfa)
        self.ui.yukle_btn.clicked.connect(self.openFileNamesDialog)
        self.ui.kaydet.clicked.connect(self.kayit_ol)
        self.ui.giris_btn.clicked.connect(self.bilgi_yukle)
        self.ui.cikis_btn.clicked.connect(self.cikis)

        self.kayit = {}

        self.fotograflar()
        self.combo_box_yukle()
    
    def fotograflar(self):
        self.ui.image_label.setStyleSheet('''
        image: url(resources/robot.png)
        ''')

        self.ui.logo_label.setStyleSheet('''
        image: url(resources/icon.png)
        ''')

        self.ui.logo_label_2.setStyleSheet('''
        image: url(resources/icon.png)
        ''')
    
    def combo_box_yukle(self):
        for i in range(1, 32):
            self.ui.gun.addItem(str(i))

        for i in range(1, 13):
            self.ui.ay.addItem(str(i))
            self.ui.sinif.addItem(str(i))

        for i in range(1999, 2022):
            self.ui.yil.addItem(str(i))
            
        self.ui.cinsiyet.addItems(['Erkek', 'Kadın'])
    
    def kayit_sayfa(self):
        for i in [self.ui.kuallanci_adi, self.ui.ad, self.ui.soyad, self.ui.sifre_kayit, self.ui.sifre_kayit_tekrar,self.ui.yukle_label,self.ui.bolum]:
            i.clear()
        self.ui.stackedWidget.setCurrentIndex(self.kayit_sayfa_index)
    
    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog

        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;", options=options)
        if self.fileName:
            self.file_secildi = True

        file = self.fileName.split('/')
        fotograf_ismi = file[len(file) - 1]
        
        self.ui.yukle_label.setText(fotograf_ismi)
    
    def kayit_ol(self):
        if self.file_secildi and self.ui.kuallanci_adi.text() and self.ui.sifre_kayit.text() == self.ui.sifre_kayit_tekrar.text():
            self.kayit[self.ui.kuallanci_adi.text()] = {
                'ad': self.ui.ad.text(),
                'soyad': self.ui.soyad.text(),
                'sifre': self.ui.sifre_kayit.text(),
                'fotograf': self.fileName,
                'dogum': [self.ui.gun.currentText(), self.ui.ay.currentText(), self.ui.yil.currentText()],
                'cinsiyet': self.ui.cinsiyet.currentText(),
                'sinif': self.ui.sinif.currentText(),
                'bolum': self.ui.bolum.text()
            }
            self.file_secildi = False
            self.cikis()
    
    def bilgi_yukle(self):
        kullanci_adi = self.ui.kullanci.text()
        if kullanci_adi in self.kayit:
            girildi_kullanci = self.kayit[kullanci_adi]
            if self.ui.sifre.text() == girildi_kullanci['sifre']:

                self.ui.bilgi_image.setStyleSheet('''
                image: url({image})
                '''.replace("{image}", girildi_kullanci['fotograf']))

                self.ui.isim_label.setText(girildi_kullanci['ad'].upper() + " " + girildi_kullanci['soyad'].upper())
                self.ui.bilgi_kullanci.setText(kullanci_adi)
                self.ui.bilgi_dogum_gunu.setText('.'.join(girildi_kullanci['dogum']))
                self.ui.bilgi_cinsiyet.setText(girildi_kullanci['cinsiyet'])
                self.ui.bilgi_sinif.setText(girildi_kullanci['sinif'])
                self.ui.bilgi_bolum.setText(girildi_kullanci['bolum'])
                self.ui.stackedWidget.setCurrentIndex(self.bilgi_sayfa_index)
            
            else:
                self.ui.bilgi_label.setText('Girildiği şifre yanlış, lütfen tekrar deneyin.')
        
        else:
            self.ui.bilgi_label.setText('Girildiği kullancı adı yanlış, lütfen tekrar deneyin.')
    
    def cikis(self):
        self.ui.kullanci.clear()
        self.ui.sifre.clear()
        self.ui.bilgi_label.setText('Hoş geldiniz, devam etmek için lütfen giriş yapın.')
        self.ui.stackedWidget.setCurrentIndex(self.giris_sayfa_index)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ui_windows()

    win.show()
    sys.exit(app.exec_())