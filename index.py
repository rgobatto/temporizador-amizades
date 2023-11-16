"""
---OBEJTIVOS---
Visualizar há quanto tempo não vejo os meus amigos;
Prorizar usando classificação do Número de Dumbar;
Atualizar um arquivo CSV;
Visualização dos dados de maneira compreensível e bonita:
    Planilha;
    Webapp;
    Site;

---TAREFAS---
[X] Criar função que adiciona os dados (dicionário)
[X] Criar interface para adição de novos dados
[] Salvar dados em arquivo CSV
[] Importar dado numa planilha excel
[] Abrir planilha sempre que dados forem atualizados
"""

from datetime import datetime

listaNomes = [
    {
        "Nome": "Wando",
        "Data": "10/11/23",
        "Visitas": 1,
        "Temporizador": 1,
    }
]
hoje = datetime.now()
formatoData = "%d/%m/%y"

def adicionarAmizade():
    inputNome = input("Nome da pessoa: ")
    nome = inputNome
    amizade = dict(Nome = nome, Data = "", Visitas = 0, Temporizador = 0)
    listaNomes.append(amizade)
    print("Sua amizade foi incluída na lista")

def adicionarVisita():
    nome = input("Nome da pessoa: ")
    data = input("Data da visita no formato dd/mm/aa: ")
    dataFormatada = datetime.strptime(data, formatoData)
    amizade = next(i for i in listaNomes if i["Nome"] == nome)

    delta = hoje - dataFormatada
    deltaFormatado = delta.days

    amizade.update({"Data": data})
    amizade.update({"Visitas": amizade["Visitas"] + 1})
    amizade.update({"Temporizador": deltaFormatado})
    print("A data em que você visitou essa pessoa foi atualizada")

def escolher():
    resposta = input("Digite 1 para adicionar amizade ou 2 para adicionar visita: ")
    if resposta == "1":
        adicionarAmizade()
    elif resposta == "2":
        adicionarVisita()
    escolher()

escolher()