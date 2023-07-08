class Bola():
    def __init__(self, cor, circunferência, material):
        self.cor = cor 
        self.circunferência = circunferência
        self.material = material
    
    def trocaCor(self, novo):
        self.cor = novo
    
    def mostraCor(self):
        print(f"A cor da bola é: {self.cor}")

bola1 = Bola("azul", 20, "plástico")
bola1.trocaCor("vermelho")
bola1.mostraCor()