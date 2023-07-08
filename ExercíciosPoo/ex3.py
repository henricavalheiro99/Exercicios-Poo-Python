class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarLados(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
    
    def retornarLados(self):
        print(f"o valor da base é: {self.base} e o valor da altura é: {self.altura}")

    def Area(self, base, altura):
        a = base * altura
        return a 
    
    def Perimetro(self, base, altura):
        p = (2 * base) + (2 * altura)
        return p
    
base1 = float(input("Digite o valor da base: "))
altura1 = float(input("Digite o valor da altura: "))

r = Retangulo(base1, altura1)
print(f"A quantide de pisos de área é: {r.Area(base1, altura1)} m² e a quantidade de rodapes de perímetro é: {r.Perimetro(base1, altura1)} m²") 