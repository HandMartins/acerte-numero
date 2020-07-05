import random


class ChuteNumero:
    def __init__(self):
        self.range_min = 1
        self.range_max = 100
        self.escolha_user = 0
        self.resposta_correta = 0
        self.tentativa = False

    def GeraResult(self):
        self.resposta_correta = random.randint(self.range_min, self.range_max)
        print(self.resposta_correta)
        
    def ValorUsuario(self):
        try:
            self.escolha_user = int(input("Escolha um número entre 1 e 100 "))

        except ValueError:
            print("Valor digitado não corresponde a um valor aceito pelo sistema, favor digitar apenas números de 1 à 100")
            self.ValorUsuario()


    def Inicio(self):
        self.ValorUsuario()
        self.GeraResult()
        self.resposta_correta = self.resposta_correta
        
        while self.tentativa != True:
            
            if self.escolha_user == self.resposta_correta:
                print("Parabéns vc acertou! O valor correto é: ",self.resposta_correta)
                self.tentativa = True
                

            elif self.escolha_user < self.resposta_correta:
                print("O seu valor está abaixo do escolhido pelo sistema")
                self.tentativa = False
                self.ValorUsuario()
                

            elif self.escolha_user > self.resposta_correta:
                print("O seu valor está acima do escolhido pelo sistema")
                self.tentativa = False
                self.ValorUsuario()
               

            else:
                print("Valor digitado não corresponde a um valor aceito pelo sistema, favor digitar apenas números de 1 à 100")
                self.tentativa = False
                self.ValorUsuario()

        print("Fechando o programa")        



ChuteNumero().Inicio()
