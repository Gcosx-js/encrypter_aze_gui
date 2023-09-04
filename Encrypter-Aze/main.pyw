import sys
import ctypes
from PyQt5 import QtGui
from functions import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pin_screen_ui import Ui_Form as pin_screen
from pin_screen_reg_ui import Ui_Form as pin_screen_reg
from os import system as temizle
from menu_screen_ui import Ui_Form as menu_screen
from functions_aes import *
import easygui as e
import pyperclip
from use_about_screen import About_screen_c as dev_sc
main_data_dosyasinin_yolu = 'data.config'
try:
    class Main_menu(QWidget):
        def __init__(self):
            super().__init__()
            self.menu_ui = menu_screen()
            self.menu_ui.setupUi(self)
            self.menu_ui.kopyala_movie.mousePressEvent = self.label_tiklanma
            if acari_yoxla() != 'key_none':
                self.menu_ui.yaradilmis_acar_lineedit.setText(acari_yoxla())
                
                
            self.copy_key_gif = QMovie(r'gifler\copy_icon.gif')
            self.menu_ui.kopyala_movie.setScaledContents(True)
            self.menu_ui.kopyala_movie.setMovie(self.copy_key_gif)
            self.copy_key_gif.start()
            self.menu_ui.yeni_acar_yarat_btn.clicked.connect(self.acar_yarat_basildi)
            self.menu_ui.menu_acar_yarad.clicked.connect(self.menu_btn_basildi)
            self.menu_ui.menu_haqqinda.clicked.connect(self.menu_btn_basildi)
            self.menu_ui.menu_metn_sifr.clicked.connect(self.menu_btn_basildi)
            self.menu_ui.menu_qovluq_sifr.clicked.connect(self.menu_btn_basildi)
            self.menu_ui.menu_cixis.clicked.connect(self.menu_btn_basildi)
            self.menu_ui.qovluq_sec_btn.clicked.connect(self.qovluq_sec)
            self.menu_ui.yadda_saxla_btn.clicked.connect(self.yadda_saxla_btn_basildi)
            self.menu_ui.qovluq_sifrele_baslat.clicked.connect(self.qovluq_sifrele_baslat_basildi)
            self.menu_ui.metn_sifrele_baslat_btn.clicked.connect(self.metn_sifrele_baslat_basildi)
            self.developer_screen = dev_sc()
            self.menu_ui.developer_btn.clicked.connect(self.developer_sc_kec)
            self.menu_ui.metn_sfirele_kopyala_btn.clicked.connect(self.metn_kopyala)
            self.menu_ui.metn_sifrele_sifirla_btn.clicked.connect(self.sifirla)
            
            
            
        def metn_kopyala(self):
            text = self.menu_ui.metn_sfirele_plaintext.toPlainText()
            if text !='':
                pyperclip.copy(text)
                QMessageBox.information(self,'Məlumat','Mətn kopyalandı')
            
        def sifirla(self):
            self.menu_ui.metn_sfirele_plaintext.setPlainText('')
        def developer_sc_kec(self):
            self.developer_screen.show()
            
        def metn_sifrele_baslat_basildi(self):
            text = self.menu_ui.metn_sfirele_plaintext.toPlainText()
            if text !='':
                index = self.menu_ui.metn_sifrele_combobox.currentIndex()
                if index == 0:
                    sifreli_metn =  encrypt_text(text)
                    self.menu_ui.metn_sfirele_plaintext.setPlainText(str(sifreli_metn))
                else:
                    desifreli_metn =  decrypt_text(text)
                    self.menu_ui.metn_sfirele_plaintext.setPlainText(str(desifreli_metn))
                    
                    
                
        def qovluq_sifrele_baslat_basildi(self):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Təsdiq sorğusu!")
            dialog.setText("Diqqət! Davam etmədən öncə edəcəyiniz prosesin digərinə əks olduğundan əmin olun. Əgər deşifrəli faylı yenidən deşifrə edərsəniz faylı bərpa etmək mümkün olmayacaqdır.")
            dialog.setIcon(QMessageBox.Question)
            dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            dialog.setDefaultButton(QMessageBox.Yes)
            result = dialog.exec_()
            if result == QMessageBox.Yes:
                qovluq_path = self.menu_ui.qovluq_path_lineedit.text()
                if qovluq_path !='':
                    qovluq_box_index = self.menu_ui.qovluq_sifrele_combobox.currentIndex()
                    if acari_yoxla() !='key_none':
                        if qovluq_box_index ==0:
                            lock(qovluq_path,bytes(acari_yoxla()[:32], encoding='utf-8'))
                            QMessageBox.information(self,'Məlumat','Qovluq uğurla şifrələndi!')
                        else:
                            acar = acari_yoxla()
                            unlock(qovluq_path,bytes(acari_yoxla()[:32], encoding='utf-8'))
                            QMessageBox.information(self,'Məlumat','Qovluq uğurla deşifrələndi!')
                    else:
                        QMessageBox.critical(self,'Xəta','Şifrələmə üçün açar tapılmadı!')
                else:
                    QMessageBox.critical(self,'Xəta','Zəhmət olmasa qovluğun yolun daxil edin!')
        
        
            
        def yadda_saxla_btn_basildi(self):
            if self.menu_ui.acari_daxil_et_lineedit.text() != '':
                yeni_acar = self.menu_ui.acari_daxil_et_lineedit.text()
                self.menu_ui.yaradilmis_acar_lineedit.setText(str(yeni_acar))
                acari_yenile(yeni_acar)
                QMessageBox.information(self,'Məlumat','Açar uğurla yadda saxlanıldı!')
                self.menu_ui.acari_daxil_et_lineedit.setText('')
            else:
                QMessageBox.critical(self,'Xəta','Açarı daxil etməlisiniz!')
                
            
        def stop_label_gif(self):
            self.copy_key_gif.stop()
            self.copy_key_gif = QMovie(r'gifler\copy_icon.gif')
            self.menu_ui.kopyala_movie.setScaledContents(True)
            self.menu_ui.kopyala_movie.setMovie(self.copy_key_gif)
            self.copy_key_gif.start()
        def label_tiklanma(self,event):
            self.copy_text = self.menu_ui.yaradilmis_acar_lineedit.text()
            if self.copy_text !='':
                pyperclip.copy(self.copy_text)
                self.copy_key_gif = QMovie(r'gifler\verified_icon.gif')
                self.menu_ui.kopyala_movie.setScaledContents(True)
                self.menu_ui.kopyala_movie.setMovie(self.copy_key_gif)
                self.copy_key_gif.start()
                self.copy_key_timer = QTimer()
                self.copy_key_timer.timeout.connect(self.stop_label_gif)
                self.copy_key_timer.start(2000)
        
        def acar_yarat_basildi(self):
            if self.menu_ui.yaradilmis_acar_lineedit.text() == '':
                self.menu_ui.yaradilmis_acar_lineedit.setText(str(acar_yarat_gen()))
            else:
                dialog = QMessageBox(self)
                dialog.setWindowTitle("Təsdiq sorğusu!")
                dialog.setText("Diqqət! Açarı yeniləmədən öncə hər hansısa qovluğun vəya mətnin şifrəli olmadığından əmin olun. Əks halda açarı geri qaytarmaq mümkün deyil!")
                dialog.setIcon(QMessageBox.Question)
                dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                dialog.setDefaultButton(QMessageBox.Yes)
                result = dialog.exec_()
                if result == QMessageBox.Yes:
                    self.menu_ui.yaradilmis_acar_lineedit.setText(str(acar_yarat_gen()))
        
        
        
        
        def qovluq_sec(self):
            folder_path = QFileDialog.getExistingDirectory(self, 'Qovluq seç','path')
            if folder_path:
                self.menu_ui.qovluq_path_lineedit.setText(folder_path)
                
            
        def menu_btn_basildi(self):
            self.btns_qss()
            sender = self.sender()
            if sender == self.menu_ui.menu_acar_yarad:
                self.menu_ui.stackedWidget.setCurrentIndex(3)
            elif sender == self.menu_ui.menu_cixis:
                sys.exit()
            elif sender == self.menu_ui.menu_metn_sifr:
                self.menu_ui.stackedWidget.setCurrentIndex(0)
            elif sender == self.menu_ui.menu_qovluq_sifr:
                self.menu_ui.stackedWidget.setCurrentIndex(1)
            elif sender == self.menu_ui.menu_haqqinda:
                self.menu_ui.stackedWidget.setCurrentIndex(2)  
            
            sender.setStyleSheet("QPushButton{\n"
    "    color:white;\n"
    "    border:1px solid white;\n"
    "    border-radius:20px;\n"
    "    background-color:transparent;\n"
    "    \n"
    "}\n"
    "QPushButton:hover{\n"
    "    color:white;\n"
    "    border:1px solid white;\n"
    "    border-radius:20px;\n"
    "    background-color: rgba(255, 255, 255,0.2);\n"
    "    \n"
    "}\n"
    "QPushButton:pressed{\n"
    "    color:white;\n"
    "    border:1px solid white;\n"
    "    border-radius:20px;\n"
    "    background-color: rgba(255, 255, 255,0.3);\n"
    "    \n"
    "}\n"
    "")
            
            
            
        def btns_qss(self):
            for i in (self.menu_ui.menu_acar_yarad,self.menu_ui.menu_haqqinda,self.menu_ui.menu_metn_sifr,self.menu_ui.menu_qovluq_sifr):
                i.setStyleSheet("QPushButton{\n"
    "    color:white;\n"
    "    border:1px solid transparent;\n"
    "    border-radius:20px;\n"
    "    background-color:transparent;\n"
    "    \n"
    "}\n"
    "QPushButton:hover{\n"
    "    color:white;\n"
    "    border:1px solid transparent;\n"
    "    border-radius:20px;\n"
    "    background-color: rgba(255, 255, 255,0.2);\n"
    "    \n"
    "}\n"
    "QPushButton:pressed{\n"
    "    color:white;\n"
    "    border:1px solid transparent;\n"
    "    border-radius:20px;\n"
    "    background-color: rgba(255, 255, 255,0.3);\n"
    "    \n"
    "}\n"
    "")
        
            




    class Pin_reg_screen(QWidget):
        def __init__(self):
            super().__init__()
            self.reg_ui = pin_screen_reg()
            self.reg_ui.setupUi(self)
            self.pin_input_str = ''
            self.setWindowTitle('Şifrə təyin edin')
            self.pin_input_int = 0
            self.logine_kec = Login_screen()
            self.reg_ui.imtina_btn.clicked.connect(self.imtina_btn_event)
            self.reg_ui.pushButton.clicked.connect(lambda checked,v='1':self.btn_event(v))
            self.reg_ui.pushButton_2.clicked.connect(lambda checked,v='2':self.btn_event(v))
            self.reg_ui.pushButton_3.clicked.connect(lambda checked,v='3':self.btn_event(v))
            self.reg_ui.pushButton_4.clicked.connect(lambda checked,v='4':self.btn_event(v))
            self.reg_ui.pushButton_5.clicked.connect(lambda checked,v='5':self.btn_event(v))
            self.reg_ui.pushButton_6.clicked.connect(lambda checked,v='6':self.btn_event(v))
            self.reg_ui.pushButton_7.clicked.connect(lambda checked,v='7':self.btn_event(v))
            self.reg_ui.pushButton_8.clicked.connect(lambda checked,v='8':self.btn_event(v))
            self.reg_ui.pushButton_9.clicked.connect(lambda checked,v='9':self.btn_event(v))
            self.reg_ui.pushButton_10.clicked.connect(lambda checked,v='0':self.btn_event(v))
            self.reg_ui.pushButton_delete.clicked.connect(self.delete_btn)
            self.login_gif = QMovie(r'gifler\login_icon.gif')
            self.reg_ui.login_logos.setScaledContents(True)
            self.reg_ui.login_logos.setMovie(self.login_gif)
            self.login_gif.start()
        
        def imtina_btn_event(self):
            sys.exit()
        def delete_btn(self):
            if self.pin_input_int > 0:
                if self.pin_input_int ==1:
                    self.pin_ui.lineEdit.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")
                    self.pin_input_str = ''




                elif self.pin_input_int == 2:
                    self.pin_ui.lineEdit_2.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")       
                    self.pin_input_str = self.pin_input_str[0:2]





                elif self.pin_input_int ==3:
                    self.pin_ui.lineEdit_3.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")
                    self.pin_input_str = self.pin_input_str[0:3]






                elif self.pin_input_int == 4:
                    self.pin_ui.lineEdit_4.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")
                    self.pin_input_str = self.pin_input_str[0:4]
                self.pin_input_int -=1
        def disconnect_all_btns(self):
                        self.reg_ui.pushButton.clicked.disconnect()
                        self.reg_ui.pushButton_2.clicked.disconnect()
                        self.reg_ui.pushButton_3.clicked.disconnect()
                        self.reg_ui.pushButton_4.clicked.disconnect()
                        self.reg_ui.pushButton_5.clicked.disconnect()
                        self.reg_ui.pushButton_6.clicked.disconnect()
                        self.reg_ui.pushButton_7.clicked.disconnect()
                        self.reg_ui.pushButton_8.clicked.disconnect()
                        self.reg_ui.pushButton_9.clicked.disconnect()
                        self.reg_ui.pushButton_10.clicked.disconnect()
                        self.reg_ui.pushButton_delete.clicked.disconnect()
        def btn_event(self,value):
            if self.pin_input_int < 4:
                self.pin_input_int +=1
                self.pin_input_str +=str(value)
                if self.pin_input_int == 1:
                    self.reg_ui.lineEdit.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
    }""")
                elif self.pin_input_int == 2:
                    self.reg_ui.lineEdit_2.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
    }""")       
                elif self.pin_input_int ==3:
                    self.reg_ui.lineEdit_3.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
    }""")
                elif self.pin_input_int == 4:
                    self.reg_ui.lineEdit_4.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
                                                        
    }""")           
                    dialog = QMessageBox(self)
                    dialog.setWindowTitle("Təsdiq sorğusu!")
                    dialog.setText("Şifrəniz təsdiq olunsunmu? Əgər şifrəni unudarsanız proqramı sıfırlamalı olacaqsız!")
                    dialog.setIcon(QMessageBox.Question)
                    dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    dialog.setDefaultButton(QMessageBox.Yes)
                    result = dialog.exec_()
                    if result == QMessageBox.Yes:
                        sifre_update(main_data_dosyasinin_yolu,self.pin_input_str)
                        self.close()
                        self.logine_kec.show()




    class Login_screen(QWidget):
        def __init__(self):
            super().__init__()
            self.pin_ui = pin_screen()
            self.pin_ui.setupUi(self)
            self.menu_kec = Main_menu()
            self.setWindowTitle('Davam etmək üçün zəhmət olmasa şifrə daxil edin')
            self.pin_ui.imtina_btn.pressed.connect(self.exit_app)
            self.pin_input_int = 0
            self.pin_input_str = ''
            self.cehd_sayi = int(cehdi_yoxla(main_data_dosyasinin_yolu))
            if check_ban_time(main_data_dosyasinin_yolu)==False:
                QMessageBox.critical(self,'Güvənlik','Hesabınız blokdadır. Zəhmət olmasa biraz sonra yenidən cəhd edin!')
                sys.exit()
        
                

            self.pin_ui.pushButton.clicked.connect(lambda checked,v='1':self.btn_event(v))
            self.pin_ui.pushButton_2.clicked.connect(lambda checked,v='2':self.btn_event(v))
            self.pin_ui.pushButton_3.clicked.connect(lambda checked,v='3':self.btn_event(v))
            self.pin_ui.pushButton_4.clicked.connect(lambda checked,v='4':self.btn_event(v))
            self.pin_ui.pushButton_5.clicked.connect(lambda checked,v='5':self.btn_event(v))
            self.pin_ui.pushButton_6.clicked.connect(lambda checked,v='6':self.btn_event(v))
            self.pin_ui.pushButton_7.clicked.connect(lambda checked,v='7':self.btn_event(v))
            self.pin_ui.pushButton_8.clicked.connect(lambda checked,v='8':self.btn_event(v))
            self.pin_ui.pushButton_9.clicked.connect(lambda checked,v='9':self.btn_event(v))
            self.pin_ui.pushButton_10.clicked.connect(lambda checked,v='0':self.btn_event(v))
            self.pin_ui.pushButton_delete.clicked.connect(self.delete_btn)
            self.login_gif = QMovie(r'gifler\login_icon.gif')
            self.pin_ui.login_logos.setScaledContents(True)
            self.pin_ui.login_logos.setMovie(self.login_gif)
            self.login_gif.start()

        def disconnect_all_btns(self):
                        self.pin_ui.pushButton.clicked.disconnect()
                        self.pin_ui.pushButton_2.clicked.disconnect()
                        self.pin_ui.pushButton_3.clicked.disconnect()
                        self.pin_ui.pushButton_4.clicked.disconnect()
                        self.pin_ui.pushButton_5.clicked.disconnect()
                        self.pin_ui.pushButton_6.clicked.disconnect()
                        self.pin_ui.pushButton_7.clicked.disconnect()
                        self.pin_ui.pushButton_8.clicked.disconnect()
                        self.pin_ui.pushButton_9.clicked.disconnect()
                        self.pin_ui.pushButton_10.clicked.disconnect()
                        self.pin_ui.pushButton_delete.clicked.disconnect()
        def btn_event(self,value):
            if self.pin_input_int < 4:
                self.pin_input_int +=1
                self.pin_input_str +=str(value)
                if self.pin_input_int == 1:
                    self.pin_ui.lineEdit.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
    }""")
                elif self.pin_input_int == 2:
                    self.pin_ui.lineEdit_2.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
    }""")       
                elif self.pin_input_int ==3:
                    self.pin_ui.lineEdit_3.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
    }""")
                elif self.pin_input_int == 4:
                    self.pin_ui.lineEdit_4.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        background-color: rgb(255, 135, 15);\n
        border-radius:20px;\n
                                                        
    }""")           
                    
                    
                    if self.pin_input_str == sifre_yoxla(main_data_dosyasinin_yolu):
                        self.pin_ui.welcome_label.setText('Uğurlu giriş! Ana ekrana yönləndirilmək üzrəsiniz!')
                        self.login_gif = QMovie(r'gifler\login_verified_new.gif')
                        self.menu_kec_timer = QTimer(self)
                        self.menu_kec_timer.timeout.connect(self.menu_timer_func)
                        self.menu_kec_timer.start(4000)
                        cehdi_yenile(main_data_dosyasinin_yolu,4)
                        self.login_gif_timer = QTimer()
                        self.login_gif_timer.timeout.connect(self.login_gif_stop)
                        self.login_gif_timer.start(1250)
                        self.pin_ui.login_logos.setScaledContents(True)
                        self.pin_ui.login_logos.setMovie(self.login_gif)
                        self.login_gif.start()
                        self.disconnect_all_btns()

                    else:
                        if self.cehd_sayi != 0:
                            self.cehd_sayi -=1
                            cehdi_yenile(main_data_dosyasinin_yolu,self.cehd_sayi)
                            if self.cehd_sayi > 0:
                                self.pin_ui.welcome_label.setText(f'{self.cehd_sayi} cəhd qaldı!')
                                self.pin_input_int = 0
                                self.pin_input_str = ''
                                self.pin_ui.lineEdit.setStyleSheet("""
            QLineEdit{
                border: 1px solid rgba(80,80,80.0.5);\n
                border-radius:20px;\n
            }""")

                                self.pin_ui.lineEdit_2.setStyleSheet("""
                QLineEdit{
                    border: 1px solid rgba(80,80,80.0.5);\n
                    border-radius:20px;\n
                }""")       

                                self.pin_ui.lineEdit_3.setStyleSheet("""
                QLineEdit{
                    border: 1px solid rgba(80,80,80.0.5);\n
                    border-radius:20px;\n
                }""")
                                self.pin_ui.lineEdit_4.setStyleSheet("""
                QLineEdit{
                    border: 1px solid rgba(80,80,80.0.5);\n
                    border-radius:20px;\n
            }""")
                            else:
                                cari_vaxti_yaz(main_data_dosyasinin_yolu)
                                self.disconnect_all_btns()
                                self.pin_ui.welcome_label.setText('Hesabınız bloklandı. 15 dəqiqə sonra yenidən cəhd edin!')
                        else:
                            self.disconnect_all_btns()
                            cari_vaxti_yaz(main_data_dosyasinin_yolu)
                            self.pin_ui.welcome_label.setText('Hesabınız bloklandı. 15 dəqiqə sonra yenidən cəhd edin!')
                        

                    


        def menu_timer_func(self):
            self.close()
            self.menu_kec.show()
        def exit_app(self):
            sys.exit()

        def login_gif_stop(self):
            self.login_gif.stop()

        def delete_btn(self):
            if self.pin_input_int > 0:
                if self.pin_input_int ==1:
                    self.pin_ui.lineEdit.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")
                    self.pin_input_str = ''


                elif self.pin_input_int == 2:
                    self.pin_ui.lineEdit_2.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")       
                    self.pin_input_str = self.pin_input_str[0:2]


                elif self.pin_input_int ==3:
                    self.pin_ui.lineEdit_3.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")
                    self.pin_input_str = self.pin_input_str[0:3]

                elif self.pin_input_int == 4:
                    self.pin_ui.lineEdit_4.setStyleSheet("""
    QLineEdit{
        border: 1px solid rgba(80,80,80.0.5);\n
        border-radius:20px;\n
    }""")
                    self.pin_input_str = self.pin_input_str[0:4]
                self.pin_input_int -=1
                    


    if __name__ == "__main__":
        
        if sifre_yoxla(main_data_dosyasinin_yolu) != 'none':
            if len(sifre_yoxla(main_data_dosyasinin_yolu)) == 4:
                app = QApplication(sys.argv)
                window = Login_screen()
                window.show()
                sys.exit(app.exec_())
                temizle('cls')
            else:
                app = QApplication(sys.argv)
                window = Pin_reg_screen()
                window.show()
                sys.exit(app.exec_())
                temizle('cls')
        else:
            basliq = ("Encrypter-Aze")
            ikon = 0x10
            alfa = 0x100
            mesaj = ('Xoş gəlmisiniz. Qeydiyyatdan keçərək proqramı istifadə edə bilərsiniz.Proqramda sizin təhlükəsizliyiniz üçün bəzi xəbərdarlıq mesajları və əngəlləyici funksiyalar var.\
                    Ən əsası qovluq şifrələməsi istifadə edərkən daha öncə bu proqram haqqında məlumatınızın olduğundan \
                        əmin olun. Şifrələmə sonrası açarı yeniləməməyə diqqət edin.\n\nXoş istifadələr!')
            ctypes.windll.user32.MessageBoxW(None, mesaj, basliq, 0x40 | 0x0, 500, 300)
            app = QApplication(sys.argv)
            window = Pin_reg_screen()
            window.show()
            sys.exit(app.exec_())
            temizle('cls')
        
except Exception as t:
    e.msgbox(f'Xəta: {t}')
