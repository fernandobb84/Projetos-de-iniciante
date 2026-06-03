import random

ra_utilizados = []
lista_de_funcionarios = []



def buscar():
    if not lista_de_funcionarios:
        print("Sem funcionarios cadastrados!")
        return
    else:
        busca = input("Digite o NOME ou RA do funcionario: ").strip().capitalize()
        encontrou = False
        for pesquisa in lista_de_funcionarios:
            if str(pesquisa['ra']) == busca or pesquisa['nome'] == busca:
                print(f"-->\n{'='*30}Funcionario encontrado!{'='*30}\nNome--> {pesquisa["nome"]}\nCargo--> {pesquisa["cargo"]}\nRa--> {pesquisa["ra"]}\n{'='*60}")
                encontrou = True
        if not encontrou:
            print("Não foi encontrado.")




def visualizar_lista():
     if not lista_de_funcionarios:
        print("Nenhum Funcionario cadastrado. Digite 1 para cadastrada.")
     else:
         for visulizar in lista_de_funcionarios:
             print(f"Visualizar lista\n{'='*30}\nNome:{visulizar["nome"]}\nIdade:{visulizar["idade"]}\nCargo:{visulizar["cargo"]}\nRa:{visulizar["ra"]}\n{'='*30}")




def gerar_ra():
    ra = random.randint(1000,9000)                    
    while ra in ra_utilizados:
        ra = random.randint(1,1000)
    
    ra_utilizados.append(ra)
    return ra




def adicionar_funcionario():
    print(f"{'-'*30}Adiciona um novo funcionario{'-'*30}")
    nome = input("Digite seu nome: ").capitalize()
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            break
        except ValueError:
            print("Formatado de idade invalido.Digite um numero.")        
    cargo = input("Qual é seu cargo: ").capitalize()
    ra = gerar_ra()
    login = {
                 "nome":nome,
                 "idade":idade,
                 "cargo":cargo,
                 "ra":ra
                }   
    lista_de_funcionarios.append(login)
    print(f"\n<<< {nome} foi cadastrado com sucesso! RA:{ra} >>>\n")



def main():
    while True:
        print("Menu")
        try:
            opcao = int(input("1.Adicionar\n2.Visualizar Lista\n3.Buscar Funcionario\n0.Sair\nDigite sua opção: "))
        except ValueError:
            print('Valor inserido não suportado. Tente Novamente')
            continue

        match opcao:
            case 1:
                adicionar_funcionario()
            case 2:
                visualizar_lista()
            case 3:
                buscar()
            case 0:
                break

main()
