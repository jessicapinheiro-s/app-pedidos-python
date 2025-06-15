from restauranteAvaliacao import Avaliacao;
from ingredientesPedido import IngredientesPedido;

class Pedido(IngredientesPedido):
    comidas_dispo = [
        {
            'nome': 'Bullguer Salad',
            'disponivel': True,
            'valor': 25.00
        },
        {
            'nome': 'Bullguer Bacon',
            'disponivel': True,
            'valor': 27.00
        },
        {
            'nome': 'Bullguer-Smash',
            'disponivel': True,
            'valor': 26.00
        },
        {
            'nome': 'Bullguer Alho',
            'disponivel': True,
            'valor': 24.50
        },
        {
            'nome': 'Sprite',
            'disponivel': True,
            'valor': 6.78
        },
        {
            'nome': 'Dell Vale',
            'disponivel': True,
            'valor': 7.43
        },
        {
            'nome': 'Fanta',
            'disponivel': True,
            'valor': 9.34
        },
        {
            'nome': 'Coca',
            'disponivel': True,
            'valor': 8.50
        }
    ]

    def __init__(self):
        self.mostrar_opcoes();
        self.receber_opcao();
        super().__init__(self.comidas_dispo[0]['nome']);


    def ativo(prop_value):
        if (prop_value == True):
            return

    def apenas_disponiveis(arr_comidas):
        if (arr_comidas):
            apenas_comidas_disponiveis = filter(arr_comidas, ativo)
            return apenas_comidas_disponiveis
        else:
            return []

    def mostrar_opcoes(self):
        print('Menu: \n')

        if (apenas_disponiveis(comidas_dispo).length > 0):
            opcoes_output_for_user = ''

            for item_menu in apenas_disponiveis(comidas_dispo):
                opcoes_output_for_user += f"| {item_menu['nome']} | {item_menu['valor']}\n"

            print("""
                    | Comida         | Bebida    | 
                    |----------------|-----------|
            """ + opcoes_output_for_user)
        else:
            print("Não há itens Disponiveis no Cardapio")

    def receber_opcao(self):
        pedido = {
            "comida": '',
            "bebida": ''
        }
        self.pedido['comida'] = str(
            input('Digite o nome do Hamburguer')).lower()
        self.pedido['bebida'] = str(input('Digite o nome da Bebida')).lower()
        print('Pedido Feito, Obrigado!')

    def avaliar_pedido(self):
        se_avaliar = str(
            input("""
                    Você gostaria de avaliar o seu pedido?
                    Sim - Não
                """));
        if(se_avaliar == 'Sim'):
            avaliacao = Avaliacao();
            nota_avalicao = input('Defina uma nota para a Avaliação: ');
            

Pedido()
