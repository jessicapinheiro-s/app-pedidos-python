class IngredientesPedido:
    _ingredientes_pedido = ingredientes_por_item = [
        {
            'nome': 'Bullguer Salad',
            'ingredientes': [
                'pão de hambúrguer',
                'hambúrguer smash',
                'alface americana',
                'tomate',
                'queijo prato',
                'maionese da casa'
            ]
        },
        {
            'nome': 'Bullguer Bacon',
            'ingredientes': [
                'pão de hambúrguer',
                'hambúrguer smash',
                'queijo cheddar',
                'bacon crocante',
                'molho especial'
            ]
        },
        {
            'nome': 'Bullguer-Smash',
            'ingredientes': [
                'pão de hambúrguer',
                'hambúrguer smash',
                'queijo prato',
                'cebola caramelizada',
                'maionese da casa'
            ]
        },
        {
            'nome': 'Bullguer Alho',
            'ingredientes': [
                'pão de hambúrguer',
                'hambúrguer smash',
                'queijo mussarela',
                'maionese de alho',
                'cebola roxa'
            ]
        },
        {
            'nome': 'Sprite',
            'ingredientes': [
                'água gaseificada',
                'açúcar',
                'sabor natural de limão',
                'acidulante ácido cítrico',
                'conservador benzoato de sódio'
            ]
        },
        {
            'nome': 'Dell Vale',
            'ingredientes': [
                'suco de fruta concentrado',
                'água',
                'açúcar',
                'vitamina C',
                'corantes naturais'
            ]
        },
        {
            'nome': 'Fanta',
            'ingredientes': [
                'água gaseificada',
                'açúcar',
                'suco de laranja',
                'acidulante ácido cítrico',
                'corante beta-caroteno'
            ]
        },
        {
            'nome': 'Coca',
            'ingredientes': [
                'água gaseificada',
                'açúcar',
                'extrato de noz de cola',
                'cafeína',
                'acidulante ácido fosfórico',
                'aromatizantes naturais'
            ]
        }
    ];
    ingredientes_selected = null;

    def __init__(self, elemento_comida):
        self.elemento_comida = elemento_comida;
        this.ingredientes_selected = get_ingredients(self.elemento_comida);

    def filter_ingredientes_item(self, nome):
        resultado = list(filter(lambda item: item['nome'] == nome, ingredientes_pedido))
        return resultado[0]['ingredientes'] if resultado else None

    def get_ingredients(self, comida):
        return self.filter_ingredientes_item(comida)

