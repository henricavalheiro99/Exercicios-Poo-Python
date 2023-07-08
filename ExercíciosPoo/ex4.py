class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, envelheceAnos):
        self.idade += envelheceAnos
        if self.idade <= 21:
           self.crescer(0.005)
    
    def engordar(self, engordaKilos):
        self.peso += engordaKilos
    
    def emagrecer(self, emagreceKilos):
        self.peso -= emagreceKilos

    def crescer(self, altura):
        self.altura += altura

    def retornaTudo(self):
        print(f"{self.nome} possui {self.idade} anos, pesa {self.peso} Kg e possui {self.altura} m de altura")

envelhece = int(input("Anos que a pessoa envelhece: "))
engorda = int(input("Kilos que a pessoa engorda: "))
emagrece = int(input("Kilos que a pessoa emagrece: "))

p = Pessoa("Muliro", 16, 70, 1.70)
p.envelhecer(envelhece)
p.engordar(engorda)
p.emagrecer(emagrece)
p.retornaTudo()
