from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Felipe', 10)
restaurante_praca.receber_avaliacao('Ole', 7)
restaurante_praca.receber_avaliacao('Gustavo', 2)

def main():
    Restaurante.listar_restauantes()

if __name__ == '__main__':
    main()