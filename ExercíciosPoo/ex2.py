class Quadrado():
    def __init__(self, lado):
        self.lado = lado
    
    def mudaLado(self, novoLado):
        self.lado = novoLado

    def retornaLado(self):
        print(f"O valor do lado é: {self.lado}")
    
    def area(self):
        a = self.lado * self.lado
        return a 

q1 = Quadrado(4)
q1.mudaLado(3)
print(q1.area())
