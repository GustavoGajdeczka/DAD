import datetime

class Pessoa:
    def __init__(self, nome, nascimento, cpf):
        self.__nome = nome
        self.__nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
        self.__cpf = cpf

    def def_nome(self, nome):
        self.__nome = nome
    
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
    
    def get_nome(self):
        return self.__nome

    def get_nascimento(self):
        return self.__nascimento
    
    def get_cpf(self):
        return self.__cpf

def main():
    operacao = 0
    lista = []

    while True:
        operacao = int(input("== Options \n= 1 - Insert \n= 2 - Print\n= 3 - Sort\n= 4 - Exit\n= "))

        if operacao == 1:
            nome = input("Informe o nome da pessoa: ")
            nascimento = input("Informe o nascimento da pessoa: ")
            cpf = input("Informe o CPF: ")

            lista.append(Pessoa(nome, nascimento, cpf))
        elif operacao == 2:
            for pessoa in lista:
                pessoa_nascimento = '{}/{}/{}'.format(pessoa.get_nascimento().day, pessoa.get_nascimento().month, pessoa.get_nascimento().year)
                print(pessoa.get_nome() + " - " + pessoa_nascimento + " - " + str(pessoa.get_cpf()))
        elif operacao == 3:
            n = len(lista) - 1
            for index in range(n):
                for aux in range(n):
                    if lista[aux].get_nascimento() > lista[aux + 1].get_nascimento():
                        auxiliar = lista[aux]
                        lista[aux] = lista[aux + 1]
                        lista[aux + 1] = auxiliar
                    n -= 1 
        elif operacao == 4:
            break
        else:
            print("=== Operação Invalida ===")


if __name__ == '__main__':
    main()