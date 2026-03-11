import sys
import json
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class Janela_Principal(QMainWindow): #monta a janela
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG GUI")
        self.setGeometry(620, 300, 960, 540)
        self.setWindowIcon(QIcon("images/icon.png"))


if __name__ == "__main__": #cria o loop que mantém o app aberto se essa for a main.
    Aplicativo = QApplication(sys.argv)
    Janela = Janela_Principal()
    Janela.show()
    sys.exit(Aplicativo.exec_()) 