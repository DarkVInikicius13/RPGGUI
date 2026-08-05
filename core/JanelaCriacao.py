from PyQt5.QtWidgets import QWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon

class Janela_Criacao(QWidget): #monta a janela
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG GUI")
        self.setGeometry(500, 500, 350, 150)
        self.setWindowIcon(QIcon("images/icon.png"))

        self.Nome = QLabel("Nome do Personagem: ", self)
        self.Nome_Input = QLineEdit(self)
        
        self.Interface_Criacao()

    def Interface_Criacao(self):
        
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        
        hbox.addWidget(self.Nome)
        hbox.addWidget(self.Nome_Input)

        vbox.addLayout(hbox)
        self.setLayout(vbox)