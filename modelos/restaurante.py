class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        
    def __str__(self):
        return self.nome
    
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restauantes = [restaurante_praca, restaurante_pizza]
# print(dir(restaurante_praca))
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
print(restaurante_praca)
print(restaurante_pizza)
