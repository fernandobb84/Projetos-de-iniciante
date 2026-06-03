class Controle:
    def __init__(self, primeiroNome, sobrenome, endereco, idade, rg, cpf, sexo):
        self.primeiroNome = primeiroNome
        self.sobrenome = str(sobrenome)
        self.endereco = str(endereco)
        self.idade = int(idade)
        self.rg = str(rg)
        self.cpf = str(cpf)
        self.sexo = str(sexo)


class Aluno(Controle):
    def __init__(self, primeiroNome, sobrenome, endereco, idade, rg, cpf, sexo, ra):
        super().__init__(primeiroNome, sobrenome, endereco, idade, rg, cpf,sexo)
        self.ra = int(ra)

class Professor(Controle):
    def __init__(self, primeiroNome, sobrenome, endereço, idade, rg, cpf, sexo, matricula):
        super().__init__(primeiroNome, sobrenome, endereço, idade, rg, cpf, sexo)
        self.matricula = int(matricula)


aluno1 = Aluno("Lucas","Fernandes","Av saulo",19,"Mg-10200202","1200200200","M",2020020020)
professor1 = Professor("Mauro", "Felix", "Hauros", 59, "MG-21.323.236", "134.789.246-10", "M", 20020020)

print(
    f"Nome do aluno: {aluno1.primeiroNome} {aluno1.sobrenome}, RA: {aluno1.ra}")
print(
    f"Nome do professor: {professor1.primeiroNome} {professor1.sobrenome}, Matrícula: {professor1.matricula}")
