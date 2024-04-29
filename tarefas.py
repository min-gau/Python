# tarefas.py
def adicionar_tarefa(tarefas, nome_tarefa, descricao_tarefa, data_tarefa, status_tarefa):
    tarefas[nome_tarefa] = {"descricao": descricao_tarefa, "data": data_tarefa, "status": status_tarefa}
    return tarefas

def listar_tarefas(tarefas, status_filtro='', data_filtro=''):
    filtradas = {}
    for nome, detalhes in tarefas.items():
        if (status_filtro in detalhes["status"] or not status_filtro) and (data_filtro == detalhes["data"] or not data_filtro):
            filtradas[nome] = detalhes
    return filtradas

def atualizar_tarefa(tarefas, nome_tarefa, descricao_tarefa=None, data_tarefa=None, status_tarefa=None):
    if nome_tarefa in tarefas:
        if descricao_tarefa is not None:
            tarefas[nome_tarefa]["descricao"] = descricao_tarefa
        if data_tarefa is not None:
            tarefas[nome_tarefa]["data"] = data_tarefa
        if status_tarefa is not None:
            tarefas[nome_tarefa]["status"] = status_tarefa
    return tarefas

def remover_tarefa(tarefas, nome_tarefa):
    if nome_tarefa in tarefas:
        del tarefas[nome_tarefa]
    return tarefas
