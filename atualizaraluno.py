# Form implementation generated from reading ui file 'atualizaraluno.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

#Conexão com o BD
import mysql.connector
conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="", database="escola")
cursor = conexao.cursor()
print("Conectado ao BD.")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 297)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.botao_atualizar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botao_atualizar.setObjectName("botao_atualizar")
        self.botao_atualizar.clicked.connect(self.atualizar)
        self.gridLayout.addWidget(self.botao_atualizar, 7, 1, 1, 1)
        self.line_nome = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_nome.setObjectName("line_nome")
        self.gridLayout.addWidget(self.line_nome, 2, 1, 1, 1)
        self.combo_curso = QtWidgets.QComboBox(parent=self.centralwidget)
        self.combo_curso.setObjectName("combo_curso")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.combo_curso.addItem("")
        self.gridLayout.addWidget(self.combo_curso, 3, 1, 1, 1)
        self.label_turno = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_turno.setObjectName("label_turno")
        self.gridLayout.addWidget(self.label_turno, 4, 0, 1, 1)
        self.label_curso = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 3, 0, 1, 1)
        self.label_extra = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_extra.setObjectName("label_extra")
        self.gridLayout.addWidget(self.label_extra, 5, 0, 1, 1)
        self.label_nome = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 2, 0, 1, 1)
        self.label_obs = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_obs.setObjectName("label_obs")
        self.gridLayout.addWidget(self.label_obs, 6, 0, 1, 1)
        self.text_obs = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_obs.setObjectName("text_obs")
        self.gridLayout.addWidget(self.text_obs, 6, 1, 1, 1)
        self.label_codigo = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_codigo.setObjectName("label_codigo")
        self.gridLayout.addWidget(self.label_codigo, 0, 0, 1, 1)
        self.line_codigo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.line_codigo.setObjectName("line_codigo")
        self.gridLayout.addWidget(self.line_codigo, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radio_manha_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_manha_2.setChecked(True)
        self.radio_manha_2.setObjectName("radio_manha_2")
        self.horizontalLayout_4.addWidget(self.radio_manha_2)
        self.radio_tarde_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_tarde_2.setObjectName("radio_tarde_2")
        self.horizontalLayout_4.addWidget(self.radio_tarde_2)
        self.radio_noite_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radio_noite_2.setObjectName("radio_noite_2")
        self.horizontalLayout_4.addWidget(self.radio_noite_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.check_atleta_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.check_atleta_2.setObjectName("check_atleta_2")
        self.horizontalLayout_5.addWidget(self.check_atleta_2)
        self.check_bolsista_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.check_bolsista_2.setObjectName("check_bolsista_2")
        self.horizontalLayout_5.addWidget(self.check_bolsista_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 1, 1, 1)
        self.botao_abrir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.botao_abrir.setObjectName("botao_abrir")
        self.botao_abrir.clicked.connect(self.abrir)
        self.gridLayout.addWidget(self.botao_abrir, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_atualizar.setText(_translate("MainWindow", "ATUALIZAR"))
        self.combo_curso.setItemText(0, _translate("MainWindow", "Edificações"))
        self.combo_curso.setItemText(1, _translate("MainWindow", "Eletrotécnica"))
        self.combo_curso.setItemText(2, _translate("MainWindow", "Informática"))
        self.combo_curso.setItemText(3, _translate("MainWindow", "Mecânica"))
        self.label_turno.setText(_translate("MainWindow", "Turno:"))
        self.label_curso.setText(_translate("MainWindow", "Curso:"))
        self.label_extra.setText(_translate("MainWindow", "Extra:"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_obs.setText(_translate("MainWindow", "Obs.:"))
        self.label_codigo.setText(_translate("MainWindow", "Código:"))
        self.radio_manha_2.setText(_translate("MainWindow", "Manhã"))
        self.radio_tarde_2.setText(_translate("MainWindow", "Tarde"))
        self.radio_noite_2.setText(_translate("MainWindow", "Noite"))
        self.check_atleta_2.setText(_translate("MainWindow", "Atleta"))
        self.check_bolsista_2.setText(_translate("MainWindow", "Bolsista"))
        self.botao_abrir.setText(_translate("MainWindow", "Abrir"))

    def abrir(self):
        codigo = self.line_codigo.text()
        sql = "SELECT * FROM aluno WHERE codigo = " + codigo
        cursor.execute(sql)
        dados = cursor.fetchall()
        
        if len(dados) > 0 :  #o registro existe
            self.line_nome.setText(dados[0][1])
            self.combo_curso.setCurrentText(dados[0][2])
            
            if dados[0][3] == "Manhã":
                self.radio_manha_2.setChecked(True)
            elif dados[0][3] == "Tarde":
                self.radio_tarde_2.setChecked(True)
            elif dados[0][3] == "Noite":
                self.radio_noite_2.setChecked(True)
            
            if dados[0][4] == "Sim":
                self.check_atleta_2.setChecked(True)
            else:
                self.check_atleta_2.setChecked(False)
            
            if dados[0][5] == "Sim":
                self.check_bolsista_2.setChecked(True)
            else:
                self.check_bolsista_2.setChecked(False)
            
            self.text_obs.setPlainText(dados[0][6])
            
            #bloquear o campo código
            self.line_codigo.setReadOnly(True)
            
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Registro não encontrado.")
            msg.exec()
            
            #limpar os campos
            self.line_nome.setText("")
            self.combo_curso.setCurrentIndex(0)
            self.radio_manha_2.setChecked(True)
            self.check_atleta_2.setChecked(False)
            self.check_bolsista_2.setChecked(False)
            self.text_obs.setPlainText("")
    
    
        
    def atualizar(self):
        codigo = self.line_codigo.text()
        nome   = self.line_nome.text()
        curso  = self.combo_curso.currentText()
        
        turno  = ""
        if self.radio_manha_2.isChecked():
            turno = "Manhã"
        elif self.radio_tarde_2.isChecked():
            turno = "Tarde"
        elif self.radio_noite_2.isChecked():
            turno = "Noite"
        
        atleta = "Não"
        if self.check_atleta_2.isChecked():
            atleta = "Sim"
        
        bolsista = "Não"
        if self.check_bolsista_2.isChecked():
            bolsista = "Sim"
        
        obs = self.text_obs.toPlainText()
        
        sql = '''UPDATE aluno SET
                nome = %s,
                curso = %s,
                turno = %s,
                atleta = %s,
                bolsista = %s,
                obs = %s 
                WHERE codigo = %s'''
        
        cursor.execute(sql, (nome, curso, turno, atleta,
                             bolsista, obs, codigo) )
        
        conexao.commit()
        
        msg = QMessageBox()
        msg.setWindowTitle("Aviso")
        msg.setText("Registro atualizado com sucesso.")
        msg.exec()
        
        #limpar os campos
        self.line_nome.setText("")
        self.combo_curso.setCurrentIndex(0)
        self.radio_manha_2.setChecked(True)
        self.check_atleta_2.setChecked(False)
        self.check_bolsista_2.setChecked(False)
        self.text_obs.setPlainText("")
        
        #desbloquar o campo código
        self.line_codigo.setReadOnly(False)
        
        
        
        
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
