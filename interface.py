# interface.py
import tarefas
import persistencia

CAMINHO_ARQUIVO = "tarefas.json"
tarefas_atuais = persistencia.carregar_tarefas(CAMINHO_ARQUIVO)

def exibir_menu():
    while True:
        menu = input("""
        Escolha a opção desejada:
        1 - para Ver Tarefas
        2 - para Adicionar Tarefa
        3 - para Atualizar Tarefa
        4 - para Excluir Tarefa
        5 - para Sair
        """)
        if menu == "1":
            status_filtro = input("Filtrar por status (deixe em branco para todos): ")
            data_filtro = input("Filtrar por data (deixe em branco para todos): ")
            tarefas_filtradas = tarefas.listar_tarefas(tarefas_atuais, status_filtro, data_filtro)
            for nome, detalhes in tarefas_filtradas.items():
                print(f"Tarefa: {nome}\nDescrição: {detalhes['descricao']}\nData: {detalhes['data']}\nStatus: {detalhes['status']}\n")
        elif menu == "2":
            nome_tarefa = input("Digite o nome da tarefa: ")
            descricao_tarefa = input("Digite a descrição da tarefa: ")
            data_tarefa = input("Digite a data da tarefa (DD/MM/AAAA): ")
            status_tarefa = input("Digite o status da tarefa (pendente, em andamento, concluída): ")
            tarefas_atuais = tarefas.adicionar_tarefa(tarefas_atuais, nome_tarefa, descricao_tarefa, data_tarefa, status_tarefa)
            persistencia.salvar_tarefas(tarefas_atuais, CAMINHO_ARQUIVO)
            print("Tarefa adicionada com sucesso!")
        elif menu == "3":
            nome_tarefa = input("Digite o nome da tarefa que deseja atualizar: ")
            descricao_tarefa = input("Digite a nova descrição da tarefa (deixe em branco para não alterar): ")
            data_tarefa = input("Digite a nova data da tarefa (deixe em branco para não alterar): ")
            status_tarefa = input("Digite o novo status da tarefa (deixe em branco para não alterar): ")
            tarefas_atuais = tarefas.atualizar_tarefa(tarefas_atuais, nome_tarefa, descricao_tarefa, data_tarefa, status_tarefa)
            persistencia.salvar_tarefas(tarefas_atuais, CAMINHO_ARQUIVO)
            print("Tarefa atualizada com sucesso!")
        elif menu == "4":
            nome_tarefa = input("Digite o nome da tarefa que deseja excluir: ")
            tarefas_atuais = tarefas.remover_tarefa(tarefas_atuais, nome_tarefa)
            persistencia.salvar_tarefas(tarefas_atuais, CAMINHO_ARQUIVO)
            print(f"A tarefa '{nome_tarefa}' foi excluída com sucesso.")
        elif menu == "5":
            print("Saindo do aplicativo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    exibir_menu()
