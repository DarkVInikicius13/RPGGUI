import json

# ---------------
# Funções de Personagem
# -----------------

def EditarAtributos(Valor, Label): #deixar isso como um placeholder, dps tem q incluir um status pra mexermos no json 
    valor_atual = int(Label.text())
    novo_valor = valor_atual + Valor
    if novo_valor >= 0 and novo_valor <= 20:
        Label.setText(str(novo_valor))
    else:
        print("Insira um valor valido") #placeholder pra ver se ta dando certo

# ---------------
# Funções de Escrita
# -----------------

def EscritaJson():
    pass

# ---------------
# Funções de Leitura
# -----------------

def LeituraJson():
    pass