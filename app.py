class Pedido:
    def __init__(self):
        self.mostrar_opcoes();
        self.receber_opcao();
    
    def mostrar_opcoes(self):
        print('Menu: \n');
        print("""
              | Comida         | Bebida    | 
              | Bullguer Salad | Coca      |
              | Bullguer Bacon | Fanta     |
              | Bullguer-Smash | Dell Vale |
              | Bullguer Alho  | Sprite    |
        """);
        
    def receber_opcao(self): 
        pedido = {
        "comida": '',
        "bebida": ''
    };
        self.pedido['comida'] = str(input('Digite o nome do Hamburguer'));
        self.pedido['bebida'] = str(input('Digite o nome da Bebida'));
        print('Pedido Feito, Obrigado!');
        
        
        
Pedido();