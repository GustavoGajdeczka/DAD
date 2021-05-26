import random
class Aluno:
    def __init__(self, matricula, nome):
        self.__nome = nome
        self.__matricula = matricula
        self.__nota1 = -1
        self.__nota2 = -1
        self.__nota3 = -1
    
    def leitura(self, nota):
        if nota < 0 or nota > 10:
            print("!! Nota invalida !!")
            nota = float(input("= Insira a nota novamente: "))
        if self.__nota1 < 0:
            self.__nota1 = nota
            return 0
        elif self.__nota2 < 0:
            self.__nota2 = nota
            return 0
        elif self.__nota3 < 0:
            self.__nota3 = nota
            return 0
        else:
            return "Todas as notas ja foram cadastradas!"
    
    def getAluno(self):
        return [
            self.__nome, 
            self.__matricula, 
            round(((self.__nota1 + self.__nota2 + self.__nota3) / 3), 1)]

def aprovado(turma):
    aprovado = []
    for x in turma:
        if x[2] > 7:
            aprovado.append(x[0])
    return aprovado

def exame(turma):
    exame = []
    for x in turma:
        if x[2] < 7:
            exame.append(x[0])
    return exame

def media(turma):
    media = []
    for passnum in range(len(turma)-1,0,-1):
        for i in range(passnum):
            if turma[i][2]>turma[i+1][2]:
                temp = turma[i]
                turma[i] = turma[i+1]
                turma[i+1] = temp
    for x in turma:
        media.append([x[0], x[2]])
    return media

def main():
    turma = []
    print("== Universidade ==\n")
    print("= 0 - preenchimento AUTOMATICO e aleatorio de 10 alunos")
    print("= 1 - preenchimento MANUAL")
    regime = int(input())


    while True:
        if regime == 0:
            nomes = ["André","Enrico","Henry", "Antônio","Enzo","Ian", "Augusto","Erick","Isaac","Gustavo"]
            for x in range(10):
                aluno = Aluno(random.randint(0, 30), nomes[x])
                for x in range(3):
                    aluno.leitura(random.randint(5, 10))
                turma.append(aluno.getAluno())
            break
        else:
            aluno = Aluno(
                input("= Informe a sua matricula: "),
                input("= Informe o seu nome: ")
            )
            for x in range(3):
                aluno.leitura(float(input("= Insira a nota %i: " % (x + 1))))
            turma.append(aluno.getAluno())
            print("\n= 0 - Adicionar outro aluno\n= 1 - conferir as notas")
            if int(input("")) != 0:
                break
        
    print("# Alunos aprovados: ", aprovado(turma))
    print("# Alunos em exame: ", exame(turma))
    mediaTurma = media(turma)
    print("# Alunos Ordenados por média: ", mediaTurma)
    print("# Aluno com maior media: ", mediaTurma[-1])
    print("# Aluno com menor media: ", mediaTurma[0])

if __name__ == '__main__':
    main()



