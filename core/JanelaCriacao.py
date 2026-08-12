from PyQt5.QtWidgets import QWidget, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
import shutil
from core.Character import EditarAtributos

class Janela_Criacao(QWidget): #monta a janela
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPG GUI")
        self.setGeometry(500, 500, 350, 150)
        self.setWindowIcon(QIcon("images/icon.png"))

        #Inicio da definição das caixas de texto para criação dos personagens.
        self.Nome = QLabel("Nome do Personagem: ", self)
        self.Nome_Input = QLineEdit(self)
        
        self.Idade = QLabel("Idade: ", self)
        self.Idade_Input = QLineEdit(self)
        
        self.Peso = QLabel("Peso do Personagem: ", self)
        self.Peso_Input = QLineEdit(self)
        
        self.Genero = QLabel("Gênero do Personagem: ", self)
        self.Genero_Input = QLineEdit(self)
        
        self.ImagemEtiqueta = QLabel("Nenhuma imagem selecionada")
        self.BotaoEscolherImagem = QPushButton("Escolher imagem")
        self.BotaoEscolherImagem.clicked.connect(self.Selecionar_Imagem)

        self.ForcaLabel = QLabel("0")
        self.ForcaImage = QLabel("Teste")
        self.BotaoEditarForcaMais = QPushButton("+")
        self.BotaoEditarForcaMenos = QPushButton("-")
        self.BotaoEditarForcaMais.clicked.connect(lambda: EditarAtributos(+1, self.ForcaLabel)) #placeholder para entender como montar a função depois
        self.BotaoEditarForcaMenos.clicked.connect(lambda: EditarAtributos(-1, self.ForcaLabel))

        #Fim
        
        self.Interface_Criacao()

    def Interface_Criacao(self): #Aqui é só a interface, parte estética.
        
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        
        hbox.addWidget(self.Nome)
        hbox.addWidget(self.Nome_Input)

        hbox.addWidget(self.Idade)
        hbox.addWidget(self.Idade_Input)
        
        hbox.addWidget(self.Peso)
        hbox.addWidget(self.Peso_Input)
        
        hbox.addWidget(self.Genero)
        hbox.addWidget(self.Genero_Input)

        hbox.addWidget(self.ImagemEtiqueta)
        hbox.addWidget(self.BotaoEscolherImagem)

        hbox.addWidget(self.ForcaLabel)
        hbox.addWidget(self.BotaoEditarForcaMais)
        hbox.addWidget(self.BotaoEditarForcaMenos)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    
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
