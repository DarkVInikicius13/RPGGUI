from PyQt5.QtWidgets import QWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import shutil
from core.Character import EditarAtributos

class Janela_Criacao(QWidget): #monta a janela
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG GUI")
        self.setGeometry(500, 250, 500, 720)
        self.setWindowIcon(QIcon("images/icon.png"))

        #Inicio da definição das caixas de texto para criação dos personagens.

        self.Nome = QLabel("Nome do Personagem: ", self)
        self.Nome_Input = QLineEdit(self)
        
        self.Idade = QLabel("Idade: ", self)
        self.Idade_Input = QLineEdit(self)
        
        self.Peso = QLabel("Peso do Personagem: ", self)
        self.Peso_Input = QLineEdit(self)
        
        self.Raça = QLabel("Raça do Personagem: ", self)
        self.Raça_Input = QLineEdit(self)

        self.Altura = QLabel("Altura do Personagem: ", self)
        self.Altura_Input = QLineEdit(self)
        
        self.ImagemEtiqueta = QLabel("Nenhuma imagem selecionada")
        self.BotaoEscolherImagem = QPushButton("Escolher imagem")
        self.BotaoEscolherImagem.clicked.connect(self.Selecionar_Imagem)

        self.ForcaLabel = QLabel("0")
        self.ForcaImage = QLabel("Teste") #Deixar como imagem aqui pq tem q adicionar dps 
        self.BotaoEditarForcaMais = QPushButton("+")
        self.BotaoEditarForcaMenos = QPushButton("-")
        self.BotaoEditarForcaMais.clicked.connect(lambda: EditarAtributos(+1, self.ForcaLabel))
        self.BotaoEditarForcaMenos.clicked.connect(lambda: EditarAtributos(-1, self.ForcaLabel))

        self.AgilidadeLabel = QLabel("0")
        self.AgilidadeImage = QLabel("Teste")
        self.BotaoEditarAgilidadeMais = QPushButton("+")
        self.BotaoEditarAgilidadeMenos = QPushButton("-")
        self.BotaoEditarAgilidadeMais.clicked.connect(lambda: EditarAtributos(+1, self.AgilidadeLabel))
        self.BotaoEditarAgilidadeMenos.clicked.connect(lambda: EditarAtributos(-1, self.AgilidadeLabel))

        self.DefesaLabel = QLabel("0")
        self.DefesaImage = QLabel("Teste")
        self.BotaoEditarDefesaMais = QPushButton("+")
        self.BotaoEditarDefesaMenos = QPushButton("-")
        self.BotaoEditarDefesaMais.clicked.connect(lambda: EditarAtributos(+1, self.DefesaLabel))
        self.BotaoEditarDefesaMenos.clicked.connect(lambda: EditarAtributos(-1, self.DefesaLabel))

        self.PoderLabel = QLabel("0")
        self.PoderImage = QLabel("Teste")
        self.BotaoEditarPoderMais = QPushButton("+")
        self.BotaoEditarPoderMenos = QPushButton("-")
        self.BotaoEditarPoderMais.clicked.connect(lambda: EditarAtributos(+1, self.PoderLabel))
        self.BotaoEditarPoderMenos.clicked.connect(lambda: EditarAtributos(-1, self.PoderLabel))

        self.FocoLabel = QLabel("0")
        self.FocoImage = QLabel("Teste")
        self.BotaoEditarFocoMais = QPushButton("+")
        self.BotaoEditarFocoMenos = QPushButton("-")
        self.BotaoEditarFocoMais.clicked.connect(lambda: EditarAtributos(+1, self.FocoLabel))
        self.BotaoEditarFocoMenos.clicked.connect(lambda: EditarAtributos(-1, self.FocoLabel))

        #Fim
        
        self.Interface_Criacao()

    def Interface_Criacao(self): #Aqui é só a interface, parte estética.
        self.BackgroundLabel = QLabel(self)
        self.BackgroundLabel.setGeometry(0, 0, 500, 720)
        Background = QPixmap("images/Background.png").scaled(self.size(), aspectRatioMode= Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.BackgroundLabel.setPixmap(Background)

    
    def Selecionar_Imagem(self):
        caminho, _ = QFileDialog.getOpenFileName(
            self,
            "Escolha uma imagem",
            "",
            "Imagens (*.png *.jpg *.jpeg *.bmp *.webp)"
        )

        if caminho:
            shutil.copy(caminho, "images/") #copia o arquivo para a pasta de imagens do app
            if IOError:
                print("Erro ao carregar")
            else:
                print("Arquivo carregado com sucesso")

            pixmap = QPixmap(caminho)
            pixmap = pixmap.scaled(
                self.ImagemEtiqueta.width(),
                self.ImagemEtiqueta.height()
            )
            self.ImagemEtiqueta.setPixmap(pixmap)
