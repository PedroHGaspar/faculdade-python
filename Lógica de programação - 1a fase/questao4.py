print("Bem-vindos à empresa do Pedro Henrique Gaspar de Figueiredo")
# Peço perdão ao professor por que eu só notei agora nesse exercício 4 que todos os outros exercicios pediam o NOME COMPLETO, só não irei trocar os outros pois vai ficar estranho todos os prints no mesmo horário. A clássica ansiedade de querer pular enuncioado e ir direto pra resolução, peço desculpas e nas próximas não irei pular nada.

# lista global
lista_funcionarios = []
# id_global = {ID PESSOAL NÃO VAI PRO GIT}  # RU uninter


def cadastrar_funcionario(id):
    # cadastra um funcionario e add ele na lista
    import copy

    nome = input("Digite o nome do funcionário: ").strip()
    setor = input("Digite o setor do funcionário: ").strip()
    try:
        salario = float(input("Digite o salário do funcionário: ").strip())
    except ValueError:
        print("Salário inválido. O valor deve ser numérico.")
        return

    funcionario = {"ID": id, "Nome": nome, "Setor": setor, "Salário": salario}

    lista_funcionarios.append(copy.deepcopy(funcionario))
    print("Funcionário cadastrado com sucesso!")


def consultar_funcionarios():
    # consulta os funcionarios pela opcao escolhida
    while True:
        print("\nConsultar Funcionários")
        print("1. Consultar Todos")
        print("2. Consultar por ID")
        print("3. Consultar por Setor")
        print("4. Retornar ao Menu")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\nTodos os Funcionários:")
            for func in lista_funcionarios:
                print(func)
        elif opcao == "2":
            id = int(input("Digite o ID do funcionário: ").strip())
            encontrado = False
            for func in lista_funcionarios:
                if func["ID"] == id:
                    print("\nFuncionário encontrado:")
                    print(func)
                    encontrado = True
                    break
            if not encontrado:
                print("ID inválido.")
        elif opcao == "3":
            setor = input("Digite o setor: ").strip()
            encontrados = [
                func for func in lista_funcionarios if func["Setor"] == setor
            ]
            if encontrados:
                print("\nFuncionários do setor", setor, ":")
                for func in encontrados:
                    print(func)
            else:
                print("Nenhum funcionário encontrado para o setor informado.")
        elif opcao == "4":
            return
        else:
            print("Opção inválida. Tente novamente.")


def remover_funcionario():
    # remover um funcionario pelo id
    while True:
        try:
            id = int(input("Digite o ID do funcionário a ser removido: ").strip())
            global lista_funcionarios
            lista_funcionarios = [
                func for func in lista_funcionarios if func["ID"] != id
            ]
            print("Funcionário removido com sucesso!")
            return
        except ValueError:
            print("ID inválido. Tente novamente.")


# funcao principal
if __name__ == "__main__":
    while True:
        print("\nMenu Principal")
        print("1. Cadastrar Funcionário")
        print("2. Consultar Funcionário")
        print("3. Remover Funcionário")
        print("4. Encerrar Programa")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            id_global += 1
            cadastrar_funcionario(id_global)
        elif opcao == "2":
            consultar_funcionarios()
        elif opcao == "3":
            remover_funcionario()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
