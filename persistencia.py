# persistencia.py
import json

def carregar_tarefas(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def salvar_tarefas(tarefas, caminho_arquivo):
    with open(caminho_arquivo, "w") as file:
        json.dump(tarefas, file)
