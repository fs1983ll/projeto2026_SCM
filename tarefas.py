# Sistema de gerenciamento de tarefas
# Projeto: projeto2026_SCM

tarefa = []

def adicionar_tarefa(descricao):
	tarefas.append(descricao)
	print("Tarefa adicionada com sucesso!")

def lista_tarefas():
	print("\nLISTA DE TAREFAS")
	for numero, tarefa in enumerate(tarefas, start=1):
		print(f"{numero} - {tarefa}")

adicionar_tarefa("Criar documentação do projeto")
adicionar_tarefa("Testar funcionalidades")
adicionar_tarefa("Atualizar o repositório Github")

listar_tarefas()