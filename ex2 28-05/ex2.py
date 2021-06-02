class Imovel:
    def __init__(self, endereco, preco):
        self.__endereco = endereco
        self.__preco = preco

    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.__endereco = endereco
        self.__preco = preco
        self.__adicional = adicional
    
    def get_adicional(self):
        return (self.__preco + self.__adicional)
    def set_adicional(self, adicional):
        self.__adicional = adicional
        self.__preco += adicional
    def imprime_adicional(self):
        print("Adicional: ", self.get_adicional)

class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.__endereco = endereco
        self.__preco = preco
        self.__desconto = desconto
    
    def get_desconto(self):
        return (self.__preco - self.__desconto)

    def set_desconto(self, desconto):
        self.__desconto = desconto
        self.__preco -= desconto 

    def imprime_desconto(self):
        print("Desconto: ", self.__desconto)

def escolha(index, imovel):
    print("= Escolha uma operação \n" +
                "= 0 - Obter endereço \n" +
                "= 1 - Definir endereço \n" +
                "= 2 - Obter Preco \n" +
                "= 3 - Definir Preco")
    if (index == 0):
        print("= 4 - Obter Adicional \n" +
        "= 5 - Definir Adicional \n" +
        "= 6 - Imprimir Adicional")
    
    
    opera = int(input())
    if (opera == 0):
        imovel.get_endereco()
    elif(opera == 1):
        imovel.set_endereco(input("= Insira o endereço: "))
    elif(opera == 2):
        imovel.get_preco()
    elif(opera == 3):
        imovel.set_preco(float(input("= Insira o preço: ")))
    elif(opera == 4 and index == 0):
        imovel.get_adicional()
    elif(opera == 4 and index == 2):
        imovel.get_desconto()
    elif(opera == 5 and index == 2):
        imovel.set_desconto()
    elif(opera == 5 and index == 0):
        imovel.set_adicional()
    elif(opera == 6 and index == 0):
        imovel.imprime_adicional()
    elif(opera == 6 and index == 2):
        imovel.imprime_desconto()
    elif(opera == 7):
        return False
    

def main():
    termina = True
    while True:
        print("== Imobiliaria ==\n")
        print("Escolha um Imovel: \n= 0 - Novo  (++) \n= 1 - Usado (==) \n= 2 - Velho (--)\n")
        nivel = int(input())
        endereco = input("= Insira o endereço: ")
        preco = float(input("= Insira o preço: "))

        if nivel == 0:
            adicional = input("= Insira o adicional: ")
            imovel = Novo(endereco, preco, adicional)
            while termina:
                print("= Escolha uma operação \n" +
                    "= 0 - Obter endereço \n" +
                    "= 1 - Definir endereço \n" +
                    "= 2 - Obter Preco \n" +
                    "= 3 - Definir Preco")
                print("= 4 - Obter Adicional \n" +
                    "= 5 - Definir Adicional \n" +
                    "= 6 - Imprimir Adicional")
                print("= 7 - Sair")
                opera = int(input())
                if opera == 0:
                    print(imovel.get_endereco())
                elif opera == 1:
                    imovel.set_endereco(input("= Insira o endereço: "))
                elif opera == 2:
                    print(imovel.get_preco())
                elif opera == 3:
                    imovel.set_preco(float(input("= Insira o preço: ")))
                elif opera == 7:
                    termina = False
                elif opera == 4:
                    print(imovel.get_adicional())
                elif opera == 5:
                    imovel.set_adicional()
                elif opera == 6:
                    imovel.imprime_adicional()
                
        elif(nivel == 1):
            imovel = Imovel(endereco, preco)
            while termina:
                print("= Escolha uma operação \n" +
                    "= 0 - Obter endereço \n" +
                    "= 1 - Definir endereço \n" +
                    "= 2 - Obter Preco \n" +
                    "= 3 - Definir Preco")
                print("= 4 - Sair")
                opera = int(input())
                if  opera == 0:
                    print(imovel.get_endereco())
                elif opera == 1:
                    imovel.set_endereco(input("= Insira o endereço: "))
                elif opera == 2 :
                    print(imovel.get_preco())
                elif opera == 3 :
                    imovel.set_preco(float(input("= Insira o preço: ")))
                elif opera == 4:
                    termina = False
           
        elif(nivel == 2):
            desconto = input("= Insira o desconto: ")
            imovel = Novo(endereco, preco, desconto)
            while termina:
                print("= Escolha uma operação \n" +
                    "= 0 - Obter endereço \n" +
                    "= 1 - Definir endereço \n" +
                    "= 2 - Obter Preco \n" +
                    "= 3 - Definir Preco")
                print("= 4 - Obter Desconto \n" +
                    "= 5 - Definir Desconto \n" +
                    "= 6 - Imprimir Desconto")
                print("= 7 - Sair")
                opera = int(input())
                if opera == 0:
                    print(imovel.get_endereco())
                elif opera == 1:
                    imovel.set_endereco(input("= Insira o endereço: "))
                elif opera == 2:
                    print(imovel.get_preco())
                elif opera == 3:
                    imovel.set_preco(float(input("= Insira o preço: ")))
                elif opera == 7:
                    termina = False
                elif opera == 4:
                    print(imovel.get_desconto())
                elif opera == 5:
                    imovel.set_desconto()
                elif opera == 6:
                    imovel.imprime_desconto()
                

if __name__ == '__main__':
    main()