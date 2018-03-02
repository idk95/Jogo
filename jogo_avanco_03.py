## Implementação do jogo 'Avanço'

from Game import *
from jogadores_avanco_03 import *
from jogar import *
from copy import deepcopy

class JogoAvanco(Game) :

    @staticmethod
    def outro_jogador(j) :
        return 'brancas' if j == 'pretas' else 'pretas'
    
    def __init__(self) :
        self.jogadores = ('brancas','pretas')
        self.sentido = {'brancas':1,'pretas':-1}        
        
        self.linhas = 7 # número de linhas
        self.cols = 7   # número de colunas
        self.objectivo = {'brancas':self.linhas,'pretas':1}
        tabuleiro_inicial = {'brancas':[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(2,7)],'pretas':[(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(7,7)]}
        movs_possiveis = self.movimentos_possiveis(tabuleiro_inicial,self.jogadores[0])
        self.initial = GameState(
            to_move = self.jogadores[0],
            utility = 0,
            board = tabuleiro_inicial,
            moves = movs_possiveis)
    
    def movimentos_possiveis(self,tabuleiro,jogador) :
        if jogador == 'brancas':
            white = jogador
            black = 'pretas'
        else:
            white = 'brancas'
            black = jogador
        
        def frente_livre(tab,peca,jog) :
            pecas_todas = tab['brancas']+tab['pretas']
            x = peca[0]+self.sentido[jog]
            y = peca[1]
            return (1 <= x <= self.linhas) and (x,y) not in pecas_todas
        
        def pode_comer_esq(tab,peca,jog) :
            x = peca[0]+self.sentido[jog]
            y = peca[1]+self.sentido[jog]
            return (x,y) in tab[JogoAvanco.outro_jogador(jog)]
        
        def pode_comer_dir(tab,peca,jog) :
            x = peca[0]+self.sentido[jog]
            y = peca[1]-self.sentido[jog]
            return (x,y) in tab[JogoAvanco.outro_jogador(jog)]
        
        def esq_livre(tab,peca,jog) :
            pecas_todas = tab['brancas']+tab['pretas']
            x = peca[0]+self.sentido[jog]
            y = peca[1]+self.sentido[jog]
            return (1 <= x <= self.linhas) and (1 <= y <= self.cols) and (x,y) not in pecas_todas
        
        def dir_livre(tab,peca,jog) :
            pecas_todas = tab['brancas']+tab['pretas']
            x = peca[0]+self.sentido[jog]
            y = peca[1]-self.sentido[jog]
            return (1 <= x <= self.linhas) and (1 <= y <= self.cols) and (x,y) not in pecas_todas
        
        movs_white = []
        for p in tabuleiro[white] :
            if frente_livre(tabuleiro,p,white) :
                movs_white.append(("avança",p))
            if pode_comer_esq(tabuleiro,p,white) :
                movs_white.append(("come-esq",p))
            if pode_comer_dir(tabuleiro,p,white) :
                movs_white.append(("come-dir",p))
            if dir_livre(tabuleiro,p,white) :
                movs_white.append(("avança-dir",p))
            if esq_livre(tabuleiro,p,white) :
                movs_white.append(("avança-esq",p))

        movs_black = []
        for p in tabuleiro[black] :
            if frente_livre(tabuleiro,p,black) :
                movs_black.append(("avança",p))
            if pode_comer_esq(tabuleiro,p,black) :
                movs_black.append(("come-esq",p))
            if pode_comer_dir(tabuleiro,p,black) :
                movs_black.append(("come-dir",p))
            if dir_livre(tabuleiro,p,black) :
                movs_black.append(("avança-dir",p))
            if esq_livre(tabuleiro,p,black) :
                movs_black.append(("avança-esq",p))

        return {white:movs_white, black:movs_black}
        
        
    def actions(self,state) :
        return state.moves[state.to_move]
    
    def result(self,state,move) :

        accao,peca = move
        jogador = state.to_move
        adversario = JogoAvanco.outro_jogador(jogador)
        tabuleiro = deepcopy(state.board)
        tabuleiro[jogador].remove(peca)
        if accao == 'avança' :
            x = peca[0]+self.sentido[jogador]
            y = peca[1]
            tabuleiro[jogador].append((x,y))
        elif accao == 'come-esq' :
            x = peca[0]+self.sentido[jogador]
            y = peca[1]+self.sentido[jogador]
            tabuleiro[jogador].append((x,y))
            tabuleiro[adversario].remove((x,y))
        elif accao == 'avança-esq' :
            x = peca[0]+self.sentido[jogador]
            y = peca[1]+self.sentido[jogador]
            tabuleiro[jogador].append((x,y))            
        elif accao == 'avança-dir' :
            x = peca[0]+self.sentido[jogador]
            y = peca[1]-self.sentido[jogador]
            tabuleiro[jogador].append((x,y))            
        else : # come-dir
            x = peca[0]+self.sentido[jogador]
            y = peca[1]-self.sentido[jogador]
            tabuleiro[jogador].append((x,y))
            tabuleiro[adversario].remove((x,y))
        estado = GameState(to_move = JogoAvanco.outro_jogador(jogador),
                           board = tabuleiro,
                           moves = self.movimentos_possiveis(tabuleiro,JogoAvanco.outro_jogador(jogador)),
                           utility = self.calcular_utilidade(tabuleiro,jogador))
        return estado

    
    def calcular_utilidade(self,tabuleiro,jogador) :
        def objectivo(linha,jogador) :
            return linha in [x for (x,_) in tabuleiro[jogador]]
        
        utilidade = 0
        adversario = JogoAvanco.outro_jogador(jogador)
        if objectivo(self.objectivo[jogador],jogador) \
           or tabuleiro[adversario] == []:
            utilidade = 1
        elif objectivo(self.objectivo[adversario],adversario) \
             or tabuleiro[jogador] == []:
            utilidade = -1
        
        return utilidade
    
    def utility(self, state, player):
        return self.calcular_utilidade(state.board,player)
    
    def terminal_test(self,state) :
        return state.moves == [] or any([self.utility(state,x) != 0 for x in self.jogadores])

    def display(self, state):
        board = state.board
        print("Tabuleiro actual:")
        for x in range(1, self.linhas + 1):
            for y in range(1, self.cols + 1):
                if (x,y) in board['brancas'] :
                    print('O', end=' ')
                elif (x,y) in board['pretas'] :
                    print('*', end=' ')
                else :
                    print('.',end=' ')
                    
            print()
        if self.terminal_test(state) :
            print("FIM do Jogo")
        else :
            print("Próximo jogador:{}\n".format(state.to_move))
            
if __name__ == '__main__' :
    ## Exemplos de interaccao
    jogo_avanco = JogoAvanco() 
    jog_humano = Jogador(jogo_avanco, nome = "José") 
    jog_aleat = Jogador(jogo_avanco, nome = "Ao Calhas", f = random_player)
    jog_alfabeta = Jogador(jogo_avanco,nome = "MaisPeças",f = jogador_avanco_F1)
    jog_alfabeta2 = Jogador(jogo_avanco, nome="MaisPeças2", f=jogador_avanco_F2)
    jog_alfabeta3 = Jogador(jogo_avanco, nome="MaisPeças3", f=jogador_avanco_F3)

    ## Execucao do jogo - um jogo(game, jogador1, jogador2, nivel, verbose)
    ## verbose pode ser True ou False, por omissao False
    resultado = n_pares_de_jogos(jogo_avanco, 10,jog_aleat, jog_alfabeta3,3, verbose = True)
    #resultado2 = n_pares_de_jogos(jogo_avanco, 10, jog_aleat, jog_alfabeta, 3)
    #resultado3 = n_pares_de_jogos(jogo_avanco, 10, jog_aleat, jog_alfabeta2, 3)
    print(resultado) # --> ResultadoJogo(Tipo=’vitoria’, Cor=’pretas’, Nome=’MaisPeças’)
    #print(resultado2)
    #print(resultado3)