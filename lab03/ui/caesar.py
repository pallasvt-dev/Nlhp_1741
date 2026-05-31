# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caesar.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)
import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "C:/Users/ASUS/AppData/Local/Programs/Python/Python311/Lib/site-packages/PyQt6/Qt6/plugins/platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(476, 430)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 20, 201, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.txt_plain_text = QPlainTextEdit(self.centralwidget)
        self.txt_plain_text.setObjectName(u"txt_plain_text")
        self.txt_plain_text.setGeometry(QRect(80, 80, 381, 91))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 47, 13))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 200, 47, 13))
        self.txt_key = QTextEdit(self.centralwidget)
        self.txt_key.setObjectName(u"txt_key")
        self.txt_key.setGeometry(QRect(80, 190, 381, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 260, 47, 13))
        self.txt_cipher_text = QPlainTextEdit(self.centralwidget)
        self.txt_cipher_text.setObjectName(u"txt_cipher_text")
        self.txt_cipher_text.setGeometry(QRect(80, 260, 381, 91))
        self.btn_encrypt = QPushButton(self.centralwidget)
        self.btn_encrypt.setObjectName(u"btn_encrypt")
        self.btn_encrypt.setGeometry(QRect(80, 360, 75, 23))
        self.btn_decrypt = QPushButton(self.centralwidget)
        self.btn_decrypt.setObjectName(u"btn_decrypt")
        self.btn_decrypt.setGeometry(QRect(380, 360, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 476, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CAESAR CIPHER", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Plaintext", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ciphertext", None))
        self.btn_encrypt.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.btn_decrypt.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
    # retranslateUi


# ===== THÊM LOGIC XỬ LÝ =====
from PySide6.QtWidgets import QMainWindow

# Caesar Cipher Implementation
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index + key) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypted_text.append(output_letter)
            else:
                encrypted_text.append(letter)  # Giữ nguyên ký tự không phải chữ cái
        return ''.join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                output_index = (letter_index - key) % alphabet_len
                output_letter = self.alphabet[output_index]
                decrypted_text.append(output_letter)
            else:
                decrypted_text.append(letter)  # Giữ nguyên ký tự không phải chữ cái
        return ''.join(decrypted_text)


# Lớp ứng dụng Caesar Cipher
class CaesarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Khởi tạo đối tượng Caesar Cipher
        self.caesar = CaesarCipher()
        
        # Kết nối các nút bấm với các hàm xử lý
        self.ui.btn_encrypt.clicked.connect(self.xu_ly_ma_hoa)
        self.ui.btn_decrypt.clicked.connect(self.xu_ly_giai_ma)

    def xu_ly_ma_hoa(self):
        """Hàm xử lý mã hóa Caesar"""
        try:
            plain_text = self.ui.txt_plain_text.toPlainText()
            key = int(self.ui.txt_key.toPlainText())
            
            if not plain_text:
                self.ui.txt_cipher_text.setPlainText("Vui lòng nhập văn bản!")
                return
            
            # Gọi hàm mã hóa
            cipher_text = self.caesar.encrypt_text(plain_text, key)
            self.ui.txt_cipher_text.setPlainText(cipher_text)
            
        except ValueError:
            self.ui.txt_cipher_text.setPlainText("Lỗi: Key phải là số nguyên!")
        except Exception as e:
            self.ui.txt_cipher_text.setPlainText(f"Lỗi: {str(e)}")

    def xu_ly_giai_ma(self):
        """Hàm xử lý giải mã Caesar"""
        try:
            cipher_text = self.ui.txt_cipher_text.toPlainText()
            key = int(self.ui.txt_key.toPlainText())
            
            if not cipher_text:
                self.ui.txt_plain_text.setPlainText("Vui lòng nhập văn bản mã hóa!")
                return
            
            # Gọi hàm giải mã
            plain_text = self.caesar.decrypt_text(cipher_text, key)
            self.ui.txt_plain_text.setPlainText(plain_text)
            
        except ValueError:
            self.ui.txt_plain_text.setPlainText("Lỗi: Key phải là số nguyên!")
        except Exception as e:
            self.ui.txt_plain_text.setPlainText(f"Lỗi: {str(e)}")


# ===== KHỞI CHẠY CHƯƠNG TRÌNH =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaesarApp()
    window.show()
    sys.exit(app.exec())

