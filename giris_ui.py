# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: #8D72E1;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(90, 70, 1101, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.giris_sayfa = QtWidgets.QWidget()
        self.giris_sayfa.setObjectName("giris_sayfa")
        self.giris_frame = QtWidgets.QFrame(self.giris_sayfa)
        self.giris_frame.setGeometry(QtCore.QRect(0, 0, 521, 581))
        self.giris_frame.setStyleSheet("QFrame#giris_frame{\n"
"background-color: #6C4AB6;\n"
"border: 1px solid #6C4AB6;\n"
"border-radius: 20px;\n"
"}")
        self.giris_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.giris_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.giris_frame.setObjectName("giris_frame")
        self.logo_label = QtWidgets.QLabel(self.giris_frame)
        self.logo_label.setGeometry(QtCore.QRect(90, 30, 51, 51))
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.kullanci = QtWidgets.QLineEdit(self.giris_frame)
        self.kullanci.setGeometry(QtCore.QRect(90, 310, 321, 51))
        self.kullanci.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.kullanci.setPlaceholderText("")
        self.kullanci.setObjectName("kullanci")
        self.sifre = QtWidgets.QLineEdit(self.giris_frame)
        self.sifre.setGeometry(QtCore.QRect(90, 420, 321, 51))
        self.sifre.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre.setObjectName("sifre")
        self.giris_btn = QtWidgets.QPushButton(self.giris_frame)
        self.giris_btn.setGeometry(QtCore.QRect(90, 490, 121, 41))
        self.giris_btn.setStyleSheet("QPushButton{\n"
"background-color: #5BB318;\n"
"border: 1px solid #5BB318;\n"
"border-radius: 10px;\n"
"color: white;\n"
"    font: 14pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #7DCE13;\n"
"}")
        self.giris_btn.setObjectName("giris_btn")
        self.kayit_btn = QtWidgets.QPushButton(self.giris_frame)
        self.kayit_btn.setGeometry(QtCore.QRect(290, 490, 121, 41))
        self.kayit_btn.setStyleSheet("QPushButton{\n"
"background-color: #FF1E00;\n"
"border: 1px solid #FF1E00;\n"
"border-radius: 10px;\n"
"color: white;\n"
"    font: 14pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff4000;\n"
"border: 1px solid #ff4000;\n"
"}")
        self.kayit_btn.setObjectName("kayit_btn")
        self.label_2 = QtWidgets.QLabel(self.giris_frame)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 321, 51))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.bilgi_label = QtWidgets.QLabel(self.giris_frame)
        self.bilgi_label.setGeometry(QtCore.QRect(90, 180, 321, 81))
        self.bilgi_label.setStyleSheet("font: 14pt \"Yu Gothic UI\";\n"
"color: rgb(218, 218, 218);")
        self.bilgi_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bilgi_label.setWordWrap(True)
        self.bilgi_label.setObjectName("bilgi_label")
        self.label_4 = QtWidgets.QLabel(self.giris_frame)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 141, 41))
        self.label_4.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.giris_frame)
        self.label_5.setGeometry(QtCore.QRect(90, 380, 141, 41))
        self.label_5.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.image_frame = QtWidgets.QFrame(self.giris_sayfa)
        self.image_frame.setGeometry(QtCore.QRect(580, 0, 521, 581))
        self.image_frame.setStyleSheet("QFrame#image_frame{\n"
"background-color: #6C4AB6;\n"
"border: 1px solid #6C4AB6;\n"
"border-radius: 20px;\n"
"}")
        self.image_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_frame.setObjectName("image_frame")
        self.image_label = QtWidgets.QLabel(self.image_frame)
        self.image_label.setGeometry(QtCore.QRect(80, 70, 361, 441))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.stackedWidget.addWidget(self.giris_sayfa)
        self.kayit_sayfa = QtWidgets.QWidget()
        self.kayit_sayfa.setObjectName("kayit_sayfa")
        self.kayit_frame = QtWidgets.QFrame(self.kayit_sayfa)
        self.kayit_frame.setGeometry(QtCore.QRect(0, 0, 1101, 581))
        self.kayit_frame.setStyleSheet("QFrame#kayit_frame{\n"
"background-color: #6C4AB6;\n"
"border: 1px solid #6C4AB6;\n"
"border-radius: 20px;\n"
"}")
        self.kayit_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.kayit_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.kayit_frame.setObjectName("kayit_frame")
        self.logo_label_2 = QtWidgets.QLabel(self.kayit_frame)
        self.logo_label_2.setGeometry(QtCore.QRect(90, 30, 51, 51))
        self.logo_label_2.setText("")
        self.logo_label_2.setObjectName("logo_label_2")
        self.ad = QtWidgets.QLineEdit(self.kayit_frame)
        self.ad.setGeometry(QtCore.QRect(290, 160, 201, 51))
        self.ad.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.ad.setPlaceholderText("")
        self.ad.setObjectName("ad")
        self.soyad = QtWidgets.QLineEdit(self.kayit_frame)
        self.soyad.setGeometry(QtCore.QRect(290, 220, 201, 51))
        self.soyad.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.soyad.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.soyad.setObjectName("soyad")
        self.kaydet = QtWidgets.QPushButton(self.kayit_frame)
        self.kaydet.setGeometry(QtCore.QRect(820, 490, 121, 41))
        self.kaydet.setStyleSheet("QPushButton{\n"
"background-color: #5BB318;\n"
"border: 1px solid #5BB318;\n"
"border-radius: 10px;\n"
"color: white;\n"
"    font: 14pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #7DCE13;\n"
"}")
        self.kaydet.setObjectName("kaydet")
        self.label_3 = QtWidgets.QLabel(self.kayit_frame)
        self.label_3.setGeometry(QtCore.QRect(380, 80, 321, 51))
        self.label_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(self.kayit_frame)
        self.label_6.setGeometry(QtCore.QRect(170, 160, 91, 41))
        self.label_6.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.kayit_frame)
        self.label_7.setGeometry(QtCore.QRect(170, 220, 101, 41))
        self.label_7.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.kayit_frame)
        self.label_8.setGeometry(QtCore.QRect(170, 280, 101, 41))
        self.label_8.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.kuallanci_adi = QtWidgets.QLineEdit(self.kayit_frame)
        self.kuallanci_adi.setGeometry(QtCore.QRect(290, 280, 201, 51))
        self.kuallanci_adi.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.kuallanci_adi.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.kuallanci_adi.setObjectName("kuallanci_adi")
        self.sifre_kayit = QtWidgets.QLineEdit(self.kayit_frame)
        self.sifre_kayit.setGeometry(QtCore.QRect(290, 340, 201, 51))
        self.sifre_kayit.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.sifre_kayit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre_kayit.setObjectName("sifre_kayit")
        self.label_9 = QtWidgets.QLabel(self.kayit_frame)
        self.label_9.setGeometry(QtCore.QRect(170, 340, 101, 41))
        self.label_9.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.sifre_kayit_tekrar = QtWidgets.QLineEdit(self.kayit_frame)
        self.sifre_kayit_tekrar.setGeometry(QtCore.QRect(290, 400, 201, 51))
        self.sifre_kayit_tekrar.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.sifre_kayit_tekrar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre_kayit_tekrar.setObjectName("sifre_kayit_tekrar")
        self.label_10 = QtWidgets.QLabel(self.kayit_frame)
        self.label_10.setGeometry(QtCore.QRect(170, 400, 101, 41))
        self.label_10.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.kayit_frame)
        self.label_11.setGeometry(QtCore.QRect(590, 160, 91, 41))
        self.label_11.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.kayit_frame)
        self.label_12.setGeometry(QtCore.QRect(590, 280, 101, 41))
        self.label_12.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.bolum = QtWidgets.QLineEdit(self.kayit_frame)
        self.bolum.setGeometry(QtCore.QRect(710, 400, 231, 51))
        self.bolum.setStyleSheet("background-color: #8D72E1;\n"
"font: 12pt \"Bahnschrift\";\n"
"border: 1px solid #8D72E1;\n"
"border-radius: 10px;\n"
"color: white;")
        self.bolum.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.bolum.setObjectName("bolum")
        self.label_13 = QtWidgets.QLabel(self.kayit_frame)
        self.label_13.setGeometry(QtCore.QRect(590, 340, 101, 41))
        self.label_13.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.kayit_frame)
        self.label_14.setGeometry(QtCore.QRect(590, 220, 101, 41))
        self.label_14.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.kayit_frame)
        self.label_15.setGeometry(QtCore.QRect(590, 400, 101, 41))
        self.label_15.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_15.setObjectName("label_15")
        self.yukle_btn = QtWidgets.QPushButton(self.kayit_frame)
        self.yukle_btn.setGeometry(QtCore.QRect(820, 160, 121, 41))
        self.yukle_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(89, 89, 89);\n"
"border-radius: 10px;\n"
"color: rgb(89, 89, 89);\n"
"    font: 14pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(217, 217, 217);\n"
"}")
        self.yukle_btn.setObjectName("yukle_btn")
        self.gun = QtWidgets.QComboBox(self.kayit_frame)
        self.gun.setGeometry(QtCore.QRect(710, 220, 69, 31))
        self.gun.setObjectName("gun")
        self.ay = QtWidgets.QComboBox(self.kayit_frame)
        self.ay.setGeometry(QtCore.QRect(790, 220, 69, 31))
        self.ay.setObjectName("ay")
        self.yil = QtWidgets.QComboBox(self.kayit_frame)
        self.yil.setGeometry(QtCore.QRect(870, 220, 69, 31))
        self.yil.setObjectName("yil")
        self.cinsiyet = QtWidgets.QComboBox(self.kayit_frame)
        self.cinsiyet.setGeometry(QtCore.QRect(710, 280, 231, 31))
        self.cinsiyet.setObjectName("cinsiyet")
        self.sinif = QtWidgets.QComboBox(self.kayit_frame)
        self.sinif.setGeometry(QtCore.QRect(710, 340, 69, 31))
        self.sinif.setObjectName("sinif")
        self.yukle_label = QtWidgets.QLabel(self.kayit_frame)
        self.yukle_label.setGeometry(QtCore.QRect(710, 160, 91, 41))
        self.yukle_label.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.yukle_label.setText("")
        self.yukle_label.setObjectName("yukle_label")
        self.stackedWidget.addWidget(self.kayit_sayfa)
        self.bilgi_sayfa = QtWidgets.QWidget()
        self.bilgi_sayfa.setObjectName("bilgi_sayfa")
        self.bilgi_frame = QtWidgets.QFrame(self.bilgi_sayfa)
        self.bilgi_frame.setGeometry(QtCore.QRect(0, 0, 1101, 581))
        self.bilgi_frame.setStyleSheet("QFrame#bilgi_frame{\n"
"background-color: #6C4AB6;\n"
"border: 1px solid #6C4AB6;\n"
"border-radius: 20px;\n"
"}")
        self.bilgi_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bilgi_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bilgi_frame.setObjectName("bilgi_frame")
        self.bilgi_image = QtWidgets.QLabel(self.bilgi_frame)
        self.bilgi_image.setGeometry(QtCore.QRect(80, 70, 361, 441))
        self.bilgi_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bilgi_image.setText("")
        self.bilgi_image.setObjectName("bilgi_image")
        self.isim_label = QtWidgets.QLabel(self.bilgi_frame)
        self.isim_label.setGeometry(QtCore.QRect(560, 70, 321, 51))
        self.isim_label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.isim_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.isim_label.setObjectName("isim_label")
        self.label_16 = QtWidgets.QLabel(self.bilgi_frame)
        self.label_16.setGeometry(QtCore.QRect(560, 160, 101, 41))
        self.label_16.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: #d3e1f7;")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.bilgi_frame)
        self.label_17.setGeometry(QtCore.QRect(560, 200, 101, 41))
        self.label_17.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: #d3e1f7;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.bilgi_frame)
        self.label_18.setGeometry(QtCore.QRect(560, 240, 101, 41))
        self.label_18.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: #d3e1f7;")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.bilgi_frame)
        self.label_19.setGeometry(QtCore.QRect(560, 280, 101, 41))
        self.label_19.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: #d3e1f7;")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.bilgi_frame)
        self.label_20.setGeometry(QtCore.QRect(560, 120, 101, 41))
        self.label_20.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: #d3e1f7;")
        self.label_20.setObjectName("label_20")
        self.bilgi_kullanci = QtWidgets.QLabel(self.bilgi_frame)
        self.bilgi_kullanci.setGeometry(QtCore.QRect(720, 120, 211, 41))
        self.bilgi_kullanci.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.bilgi_kullanci.setObjectName("bilgi_kullanci")
        self.bilgi_dogum_gunu = QtWidgets.QLabel(self.bilgi_frame)
        self.bilgi_dogum_gunu.setGeometry(QtCore.QRect(720, 160, 211, 41))
        self.bilgi_dogum_gunu.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.bilgi_dogum_gunu.setObjectName("bilgi_dogum_gunu")
        self.bilgi_cinsiyet = QtWidgets.QLabel(self.bilgi_frame)
        self.bilgi_cinsiyet.setGeometry(QtCore.QRect(720, 200, 211, 41))
        self.bilgi_cinsiyet.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.bilgi_cinsiyet.setObjectName("bilgi_cinsiyet")
        self.bilgi_sinif = QtWidgets.QLabel(self.bilgi_frame)
        self.bilgi_sinif.setGeometry(QtCore.QRect(720, 240, 211, 41))
        self.bilgi_sinif.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.bilgi_sinif.setObjectName("bilgi_sinif")
        self.bilgi_bolum = QtWidgets.QLabel(self.bilgi_frame)
        self.bilgi_bolum.setGeometry(QtCore.QRect(720, 280, 211, 41))
        self.bilgi_bolum.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.bilgi_bolum.setObjectName("bilgi_bolum")
        self.cikis_btn = QtWidgets.QPushButton(self.bilgi_frame)
        self.cikis_btn.setGeometry(QtCore.QRect(790, 470, 121, 41))
        self.cikis_btn.setStyleSheet("QPushButton{\n"
"background-color: #FF1E00;\n"
"border: 1px solid #FF1E00;\n"
"border-radius: 10px;\n"
"color: white;\n"
"    font: 14pt \"Bahnschrift\";\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #ff4000;\n"
"border: 1px solid #ff4000;\n"
"}")
        self.cikis_btn.setObjectName("cikis_btn")
        self.bilgi_msg = QtWidgets.QLabel(self.bilgi_frame)
        self.bilgi_msg.setGeometry(QtCore.QRect(560, 340, 341, 101))
        self.bilgi_msg.setStyleSheet("font: 12pt \"Yu Gothic UI\";\n"
"color: rgb(255, 255, 255);")
        self.bilgi_msg.setText("")
        self.bilgi_msg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bilgi_msg.setObjectName("bilgi_msg")
        self.stackedWidget.addWidget(self.bilgi_sayfa)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NCT"))
        self.giris_btn.setText(_translate("MainWindow", "Giriş Yap"))
        self.kayit_btn.setText(_translate("MainWindow", "Kayıt Ol"))
        self.label_2.setText(_translate("MainWindow", "GİRİŞ YAP"))
        self.bilgi_label.setText(_translate("MainWindow", "Hoş geldiniz, devam etmek için lütfen giriş yapın."))
        self.label_4.setText(_translate("MainWindow", "Kullancı adı"))
        self.label_5.setText(_translate("MainWindow", "Şifre"))
        self.kaydet.setText(_translate("MainWindow", "Kayı Ol"))
        self.label_3.setText(_translate("MainWindow", "KAYIT OL"))
        self.label_6.setText(_translate("MainWindow", "Adı"))
        self.label_7.setText(_translate("MainWindow", "Soyad"))
        self.label_8.setText(_translate("MainWindow", "Kullancı adı"))
        self.label_9.setText(_translate("MainWindow", "Şifre"))
        self.label_10.setText(_translate("MainWindow", "Şifre tekrar"))
        self.label_11.setText(_translate("MainWindow", "Fotoğraf"))
        self.label_12.setText(_translate("MainWindow", "Cinsiyet"))
        self.label_13.setText(_translate("MainWindow", "Sınıf"))
        self.label_14.setText(_translate("MainWindow", "Doğum günü"))
        self.label_15.setText(_translate("MainWindow", "Bölüm"))
        self.yukle_btn.setText(_translate("MainWindow", "Yükle"))
        self.isim_label.setText(_translate("MainWindow", "KALEBU NDATIMANA"))
        self.label_16.setText(_translate("MainWindow", "Doğum günü:"))
        self.label_17.setText(_translate("MainWindow", "Cinsiyet:"))
        self.label_18.setText(_translate("MainWindow", "Sınıf:"))
        self.label_19.setText(_translate("MainWindow", "Bölüm:"))
        self.label_20.setText(_translate("MainWindow", "Kullancı adı:"))
        self.bilgi_kullanci.setText(_translate("MainWindow", "Kaleb236"))
        self.bilgi_dogum_gunu.setText(_translate("MainWindow", "23.06.2000"))
        self.bilgi_cinsiyet.setText(_translate("MainWindow", "Erkek"))
        self.bilgi_sinif.setText(_translate("MainWindow", "12"))
        self.bilgi_bolum.setText(_translate("MainWindow", "Makine Mühendisliği"))
        self.cikis_btn.setText(_translate("MainWindow", "Çikiş Yap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
