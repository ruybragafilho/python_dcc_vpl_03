from abc import ABC, abstractmethod

# Definicao da classe abstrata Item
class Item( ABC ):

    # Inicializador da classe abstrata Item
    def __init__( self, nome, valor ):
        self.__nome = nome
        self.__valor = valor
        

    # get nome
    @property
    def nome( self ):
        return self.__nome

   # get valor
    @property
    def valor( self ):
        return self.__valor


    #set nome
    @nome.setter
    def nome( self, nome ):
        self.__nome = nome

    #set valor
    @valor.setter
    def valor( self, valor ):
        self.__valor = valor        


    # metodo abstrato que retorna o valor do descoto do item
    @abstractmethod
    def desconto( self ):
        pass

    # metodo abstrato que retorna o tipo do item
    @abstractmethod
    def tipoItem( self ):
        pass

# fim da definicao da classe abstrata Item    
    


# Definicao da classe Livro
class Livro( Item ):

    # Inicializador da classe Livro
    def __init__( self, nome, valor ):
        super().__init__( nome, valor )   


    # metodo que retorna o valor do descoto do item
    def desconto( self ):
        return 0.03

    # metodo que retorna o tipo do item
    def tipoItem( self ):
        return "Livro"

# Fim da definicao da classe Livro



# Definicao da classe Brinquedo    
class Brinquedo( Item ):

    # Inicializador da classe Brinquedo
    def __init__( self, nome, valor ):
        super().__init__( nome, valor )   


    # metodo que retorna o valor do descoto do item
    def desconto( self ):
        return 0.05

    # metodo que retorna o tipo do item
    def tipoItem( self ):
        return "Brinquedo"

# Fim da definicao da classe Brinquedo        



# Definicao da classe Eletronico   
class Eletronico( Item ):

    # Inicializador da classe Eletronico
    def __init__( self, nome, valor ):
        super().__init__( nome, valor )   


    # metodo que retorna o valor do descoto do item
    def desconto( self ):
        return 0.08

    # metodo que retorna o tipo do item
    def tipoItem( self ):
        return "Eletronico"

# Fim da definicao da classe Eletronico          
    


# Definicao da classe CestaCompras   
class CestaCompras:

    # Inicializador da classe CestaCompras
    def __init__( self ):
        self.__itens = {}


   # get itens
    @property
    def itens( self ):
        return self.__itens       


    # metodo adicionar_item, que adiciona o item 
    # e a quantidade na sacola de compras
    def adicionar_item( self, item, qtde ):
        self.__itens[item] = qtde


    # metodo imprime o relatorio final da compra 
    def relatorio_final( self ):
        self.__valorTotal()
        self.__valorTotalPorItem()


    # Metodo auxiliar que calcula e imprime o valor total da compra
    def __valorTotal( self ):
        
        vt = 0.0
        for i, q in self.__itens.items():
            vt += q * (i.valor * (1-i.desconto()))
        print( "%.2f" % (vt) )


    # Metodo auxiliar que calcula e imprime o valor total por item
    def __valorTotalPorItem( self ):
        
        vt = 0.0
        for i, q in self.__itens.items():
            print( "%s, %s, %i, %.2f, %.2f, %.2f" % (i.tipoItem(), i.nome, q, i.valor, q*i.valor, q*(i.valor * (1-i.desconto()))) )


# Fim da definicao da classe CestaCompras  



