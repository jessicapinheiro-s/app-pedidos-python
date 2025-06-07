class Avaliacao:
    media_avaliacao = 0;
    quantidade_notas = 0;
    all_avaliacoes = [];
    
    def __init__(self, cliente, nota, item_pedido):
        self.cliente = cliente;
        self.item_pedido = item_pedido;
        self.nota = nota;
        
        self.verificar_tipo_input();
        self.definicao_inicial();
        self.validar_range_media();
        
    def definicao_inicial(self):
        self.__class__.quantidade_notas += 1;
        self.__class__.all_avaliacoes.append(self.nota);

    def verificar_tipo_input(self):
        if(not isinstance(self.nota, (int, float))):
            print("Insira um dado valido (Numero)");
            return;
            
    def validar_range_media(self):
        if(self.nota < 1 or self.nota > 5):
            print('Por favor selecione uma nota valida (1 a 5)');
    
    def somar_valores_arr(self, arr_to_sum):
        return sum(arr_to_sum);
            
    def calcular_media(self):
        all_notas = self.somar_valores_arr(self.__class__.all_avaliacoes);
        media = all_notas / len(self.__class__.all_avaliacoes) if all_notas else 0;
        self.__class__.media_avaliacao = media;