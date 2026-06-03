alunos = []

def add_aluno():
      nome = input("Insira o nome do aluno: ").capitalize()
      idade = int(input("Insira a idade: "))
      nota = float(input("Insira a nota: "))
      
      if nota <= 0 or nota >= 10:
         print('Formato de nota errado. Digite uma nota de 0 a 10')
      else:   
         cadastro = {
            "nome":nome,
            "idade":idade,
            "nota":nota     
          }
         alunos.append(cadastro)

def listar_alunos():
   if len(alunos) == 0:
      print('\nSem alunos cadastro.\n')
   for aluno in alunos:
      print(f"{"="*30}\nALUNO:{aluno['nome']}\nIDADE:{aluno['idade']}\nNOTA:{aluno['nota']}\n{"="*30}")       
print(f"\n{"="*30}\n")      

def buscar_alunos(encontrar_aluno):
   if len(alunos) == 0:
      print("Sem alunos Cadastrados.")
      return
   for aluno in alunos:
      if aluno['nome'].lower() == encontrar_aluno.lower():
         print(F"\nO aluno {encontrar_aluno.capitalize()} foi encontrado.\nNome:{aluno['nome']}\nIdade:{aluno['idade']}\n")
         break
      else:
         print('Nenhum aluno encontrado.')

def remover_alunO(remover_aluno):
    if len(alunos) == 0:
      print("Sem alunos Cadastrados.")
      return
    for aluno in alunos:
      if aluno['nome'].lower() == remover_aluno.lower():
         alunos.remove(aluno)
         print(f"O aluno {remover_aluno} foi removido com sucesso.")
         return
      else:
         print('Esse aluno não foi encontrado.')
  
def media_geral():
           if len(alunos) == 0:
               print("Sem alunos Cadastrados.")
               return
           
           soma = 0
           quantidade = len(alunos)

           for n in alunos:
              soma += n['nota']
              media_total = soma / quantidade
              print(f'A media geral das notas é: {media_total:.2f}')
              return media_total   
           else:
              print('Nenhuma nota encontrada.') 


while True:
    print(f'==========Menu===========\n1.Adicionar Aluno\n2.Listar Alunos\n3.Buscar Aluno\n4.Remover Aluno\n5.Media Geral\n6. Sair\n{"="*30}')

    opcao = int(input("DIGITE SUA OPÇÃO: "))
    if opcao in (1,2,3,4,5,6):
         match opcao:
              case 1:
                add_aluno()
              case 2:
                listar_alunos()
              case 3:
                encontrar_aluno = input('Digite o aluno que você deseja procurar: ').lower()
                buscar_alunos(encontrar_aluno)
              case 4:
                remover_aluno = input("Digite o aluno que vc deseja remover: ")
                remover_alunO(remover_aluno)
              case 5:
                media_geral()
              case 6:
               break
    else:
       print('\nEntrada Invalida. Digite uma opção valida.\n')
