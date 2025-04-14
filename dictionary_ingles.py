import pandas as pd

# combinado = {**dicionario, **dicionario1}

# ingles = list(combinado.keys())
# portugues = list(combinado.values())

# df = pd.DataFrame({
#     "Inglês": ingles,
#     "Português": portugues
# })

# print(df)

# print(df.head())  # mostra as primeiras linhas
# print(df.tail())  # mostra as últimas linhas
# print(df.info())  # mostra informações sobre o DataFrame
# pd.set_option('display.max_rows', None)
# print(df)

############################################################################################################################

#     Inglês     Português
# 0       !ship     navio
# 1   agreement    acordo
# 2    anddress  endereço
# 3       apply   aplicar
# 4        bash     festa
# ..        ...       ...
# 57      where      onde
# 58       wind     vento
# 59       with       com
# 60    without       sem
# 61        yes       sim

# [62 rows x 2 columns]
#       Inglês Português

# 0      !ship     navio
# 1  agreement    acordo
# 2   anddress  endereço
# 3      apply   aplicar
# 4       bash     festa

#      Inglês    Português
# 57    where      onde
# 58     wind     vento
# 59     with       com
# 60  without       sem
# 61      yes       sim

# <class 'pandas.core.frame.DataFrame'>

# RangeIndex: 62 entries, 0 to 61

# Data columns (total 2 columns):

#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Inglês     62 non-null     object
#  1   Português  62 non-null     object
# dtypes: object(2)
# memory usage: 1.1+ KB
# None
#          Inglês            Português
# 0          ship                navio
# 1     agreement               acordo
# 2      anddress             endereço
# 3         apply              aplicar
# 4          bash                festa
# 5         begin              começar
# 6       between                entre
# 7          case                 caso
# 8       changes            alteração
# 9        choose             encolher
# 10     coalesce            aglutinar
# 11       commit       comprometer-se
# 12  constraints           restrições
# 13     custumer              cliente
# 14         data                dados
# 15      default               padrão
# 16        depth         profundidade
# 17     distinct             distinto
# 18         drop             derrubar
# 19         fail                falha
# 20      foreign          estrangeira
# 21      goodbye                tchau
# 22         hail              granizo
# 23       having                tendo
# 24        hello                  olá
# 25        inner             interior
# 26         join            juntar-se
# 27         keep               manter
# 28         left             esquerda
# 29       letter                carta
# 30          low                baixa
# 31        month                  mês
# 32           no                  não
# 33     overhead           sobrecarga
# 34      package               pacote
# 35  placeholder  marcador de posição
# 36         rain                chuva
# 37      rainfal                chuva
# 38        ready               pronto
# 39       record             registro
# 40      replace           substituir
# 41       report            relatório
# 42      revence             receitas
# 43          row                linha
# 44        setup          confirmação
# 45         snow                 neve
# 46        speed           velocidade
# 47       street                  rua
# 48    thank you             obrigado
# 49         then                então
# 50      thunder               trovão
# 51        tools          ferramentas
# 52           up            para cima
# 53       update          atualização
# 54       upload              carrega
# 55      weather                clima
# 56         when               quando
# 57        where                 onde
# 58         wind                vento
# 59         with                  com
# 60      without                  sem
# 61          yes                  sim


# while True:
#     palavra = input("Digite uma palavra (ou 'x' para sair): ")
#     if palavra.lower() == "x":
#         break
#     elif palavra in combinado:
#         print(combinado[palavra])
#     else:
#         print("Palavra não encontrada.")


import tkinter as tk
from tkinter import messagebox

dicionario = {
    '!ship': 'navio',
    'agreement': 'acordo',
    'anddress': 'endereço',
    'apply': 'aplicar',
    'bash': 'festa',
    'begin': 'começar',
    'between': 'entre',
    'case': 'caso',
    'changes': 'alteração',
    'choose': 'encolher',
    'coalesce': 'aglutinar',
    'commit': 'comprometer-se',
    'constraints': 'restrições',
    'custumer': 'cliente',
    'data': 'dados',
    'default': 'padrão',
    'depth': 'profundidade',
    'distinct': 'distinto',
    'drop': 'derrubar',
    'fail': 'falha',
    'foreign': 'estrangeira',
    'goodbye': 'tchau',
    'hail': 'granizo',
    'having': 'tendo',
    'hello': 'olá',
    'inner': 'interior',
    'join': 'juntar-se',
    'keep': 'manter',
    'left': 'esquerda',
    'letter': 'carta',
    'low': 'baixa',
    'month': 'mês',
    'no': 'não',
    'overhead': 'sobrecarga',
    'package': 'pacote',
    'placeholder': 'marcador de posição',
    'rain': 'chuva',
    'rainfal': 'chuva',
    'ready': 'pronto',
    'record': 'registro',
    'replace': 'substituir',
    'report': 'relatório',
    'revence': 'receitas',
    'row': 'linha',
    'setup': 'confirmação',
    'snow': 'neve',
    'speed': 'velocidade',
    'street': 'rua',
    'thank you': 'obrigado',
    'then': 'então',
    'thunder': 'trovão',
    'tools': 'ferramentas',
    'up': 'para cima',
    'update': 'atualização',
    'upload': 'carrega',
    'weather': 'clima',
    'when': 'quando',
    'where': 'onde',
    'wind': 'vento',
    'with': 'com',
    'without': 'sem',
    'yes': 'sim'

}

dicionario1 = {
    'hello': 'olá',
    'goodbye': 'tchau',
    'thank you': 'obrigado',
    'yes': 'sim',
    'no': 'não',
    'how are you': 'como você está',
    'i am fine': 'estou bem',
    'what is your name': 'qual é o seu nome',
    'my name is': 'meu nome é',
    'i am': 'eu sou',
    'you are': 'você é',
    'he is': 'ele é',
    'she is': 'ela é',
    'it is': 'é',
    'we are': 'nós somos',
    'they are': 'eles são',
    'i like': 'eu gosto',
    'you like': 'você gosta',
    'he likes': 'ele gosta',
    'she likes': 'ela gosta',
    'i love': 'eu amo',
    'you love': 'você ama',
    'he loves': 'ele ama',
    'she loves': 'ela ama',
    'good': 'bom',
    'bad': 'ruim',
    'big': 'grande',
    'small': 'pequeno',
    'happy': 'feliz',
    'sad': 'triste',
    'hot': 'quente',
    'cold': 'frio',
    'water': 'água',
    'food': 'comida',
    'house': 'casa',
    'car': 'carro',
    'tree': 'árvore',
    'dog': 'cachorro',
    'cat': 'gato',
    'sun': 'sol',
    'moon': 'lua',
    'day': 'dia',
    'night': 'noite',
    'friend': 'amigo',
    'family': 'família',
    'school': 'escola',
    'work': 'trabalho',
    'play': 'brincar',
    'run': 'correr',
    'jump': 'pular',
    'read': 'ler',
    'write': 'escrever',
    'help' : 'ajuda'
}

dicionario_data_science = {
    'algorithm': 'algoritmo',
    'analysis': 'análise',
    'artificial intelligence': 'inteligência artificial',
    'big data': 'grandes dados',
    'classification': 'classificação',
    'clustering': 'agrupamento',
    'data': 'dados',
    'data mining': 'mineração de dados',
    'data science': 'ciência de dados',
    'database': 'banco de dados',
    'deep learning': 'aprendizado profundo',
    'feature': 'característica',
    'forecasting': 'previsão',
    'hypothesis': 'hipótese',
    'insight': 'percepção',
    'intelligence': 'inteligência',
    'learning': 'aprendizado',
    'machine learning': 'aprendizado de máquina',
    'model': 'modelo',
    'neural network': 'rede neural',
    'pattern': 'padrão',
    'prediction': 'previsão',
    'probability': 'probabilidade',
    'regression': 'regressão',
    'sample': 'amostra',
    'statistics': 'estatística',
    'supervised learning': 'aprendizado supervisionado',
    'test': 'teste',
    'training': 'treinamento',
    'unsupervised learning': 'aprendizado não supervisionado',
    'visualization': 'visualização'
}


combinado = {**dicionario, **dicionario1, **dicionario_data_science}

class DicionarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dicionário Inglês-Português")
        self.root.configure(background='#2196F3')
        self.root.geometry("500x300")

        self.label = tk.Label(root, text="Digite uma palavra:", bg='#f0f0f0')
        self.label.place(relx=0.5, rely=0.3, anchor='center')

        self.entry = tk.Entry(root, width=50)
        self.entry.place(relx=0.5, rely=0.4, anchor='center')

        self.button = tk.Button(root, text="Traduzir", command=self.traduzir)
        self.button.place(relx=0.5, rely=0.5, anchor='center')

        self.resultado = tk.Label(root, text="", bg='#4CAF50')
        self.resultado.place(relx=0.5, rely=0.6, anchor='center')

    def traduzir(self):
        palavra = self.entry.get().lower()
        if palavra in combinado:
            self.resultado.config(text=combinado[palavra])
        else:
            self.resultado.config(text="Palavra não encontrada.")

root = tk.Tk()
app = DicionarioApp(root)
root.mainloop()

