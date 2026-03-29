import sys
import json
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from core.JanelaCriacao import JanelaCriar
from core.JanelaPersonagem import JanelaAbrir

class Janela_Principal(QWidget): #monta a janela
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG GUI")
        self.setGeometry(500, 500, 350, 150)
        self.setWindowIcon(QIcon("images/icon.png"))
        
        self.Interface_Inicial()


    def Abrir_Criacao(self):
        self.ProxJanela = JanelaCriar()
        self.ProxJanela.show()
        self.close()

    def Abrir_Carregar(self):
        self.ProxJanela2 = JanelaAbrir()
        self.ProxJanela2.show()
        self.close()


    def Interface_Inicial(self):
        Criar = QPushButton("Criar Personagem")
        Carregar = QPushButton("Carregar Personagem")
        self.setStyleSheet(""" 
            QPushButton {
                        background-color: #8d55ed;
                        color: black;
                        border: 50px;
                        border-radius: 90px;
                        padding: 10px 20px;
                        font-size: 14px;
                           }
            """)

        hbox = QHBoxLayout()
        hbox.addWidget(Criar)
        hbox.addWidget(Carregar)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        Criar.clicked.connect(self.Abrir_Criacao)
        Carregar.clicked.connect(self.Abrir_Criacao)






if __name__ == "__main__": #cria o loop que mantém o app aberto se essa for a main.
    Aplicativo = QApplication(sys.argv)
    Janela = Janela_Principal()
    Janela.show()
    sys.exit(Aplicativo.exec_()) 