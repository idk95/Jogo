## Jogadores alfabeta para o jogo 'Avanço' (com funções de avaliação)

import alfabeta 

from jogo_avanco_03 import *

def vitoria_avanco(jogador, estado):
    obj = 7 if jogador == 'brancas' else 1
    cond1 = obj in [x for (x, _) in estado.board[jogador]]
    cond2 = estado.board[JogoAvanco.outro_jogador(jogador)] == []

    return cond1 or cond2

def f_aval_avanco_F1(estado,jogador):
    """
    Dados um estado e um jogador, devolve um valor numérico.
    """
    adversario = JogoAvanco.outro_jogador(jogador)
    if vitoria_avanco(jogador, estado):
        f = 3
    elif vitoria_avanco(adversario, estado):
        f = -3
    else:
        tabuleiro_jog = estado.board[jogador]
        tabuleiro_adv = estado.board[adversario]

        soma_distancias_jogador = 0
        soma_distancias_adversario = 0

        distancia_anterior = 0

        valor_maior_jog = 0
        valor_maior_adv = 0

        for posicao in tabuleiro_jog:
            if jogador == 'brancas':
                distancia = posicao[0]
            else:
                distancia = 8 - posicao[0]
            valor_maior_jog = max(distancia_anterior, distancia)
            soma_distancias_jogador += distancia
            distancia_anterior = distancia
        for posicao in tabuleiro_adv:
            if adversario == 'brancas':
                distancia = posicao[0]
            else:
                distancia = 8 - posicao[0]
            valor_maior_adv = max(distancia_anterior, distancia)
            soma_distancias_jogador += distancia
            distancia_anterior = distancia

        distancia_med_jog = soma_distancias_jogador / len(tabuleiro_jog)
        distancia_med_adv = soma_distancias_adversario / len(tabuleiro_adv)

        poss_captura_jog = 0
        poss_captura_adv = 0

        poss_avanco_jog = 0
        poss_avanco_adv = 0

        for mov in estado.moves[jogador]:
            if mov[0] == 'avança' or mov[0] == 'avança-esq' or mov[0] == 'avança-dir':
                poss_avanco_jog += 1
            elif mov[0] == 'come-esq' or mov[0] == 'come-dir':
                poss_captura_jog += 1

        for mov in estado.moves[adversario]:
            if mov[0] == 'avança' or mov[0] == 'avança-esq' or mov[0] == 'avança-dir':
                poss_avanco_adv += 1
            elif mov[0] == 'come-esq' or mov[0] == 'come-dir':
                poss_captura_adv += 1

        n_pecas_jog = len(tabuleiro_jog)
        n_pecas_adv = len(tabuleiro_adv)

        f = (valor_maior_jog * 0.4 + distancia_med_jog *0.2 + poss_captura_jog * 0.1 + poss_avanco_jog * 0.2 + n_pecas_jog * 0.1) - (valor_maior_adv * 0.4 + distancia_med_adv *0.2 + poss_captura_adv * 0.1 + poss_avanco_adv * 0.2 + n_pecas_adv * 0.1)


    return f

def f_aval_avanco_F2(estado,jogador):
    """
    Dados um estado e um jogador, devolve um valor numérico.
    """
    adversario = JogoAvanco.outro_jogador(jogador)
    if vitoria_avanco(jogador, estado):
        f = 7
    elif vitoria_avanco(adversario, estado):
        f = -7
    else:
        tabuleiro_jog = estado.board[jogador]
        tabuleiro_adv = estado.board[adversario]

        soma_distancias_jogador = 0
        soma_distancias_adversario = 0

        distancia_anterior = 0

        valor_maior_jog = 0
        valor_maior_adv = 0

        for posicao in tabuleiro_jog:
            if jogador == 'brancas':
                distancia = posicao[0]
            else:
                distancia = 8 - posicao[0]
            valor_maior_jog = max(distancia_anterior, distancia)
            soma_distancias_jogador += distancia
            distancia_anterior = distancia
        for posicao in tabuleiro_adv:
            if adversario == 'brancas':
                distancia = posicao[0]
            else:
                distancia = 8 - posicao[0]
            valor_maior_adv = max(distancia_anterior, distancia)
            soma_distancias_jogador += distancia
            distancia_anterior = distancia

        distancia_med_jog = soma_distancias_jogador / len(tabuleiro_jog)
        distancia_med_adv = soma_distancias_adversario / len(tabuleiro_adv)

        poss_captura_jog = 0
        poss_captura_adv = 0

        poss_avanco_jog = 0
        poss_avanco_adv = 0

        for mov in estado.moves[jogador]:
            if mov[0] == 'avança' or mov[0] == 'avança-esq' or mov[0] == 'avança-dir':
                poss_avanco_jog += 1
            elif mov[0] == 'come-esq' or mov[0] == 'come-dir':
                poss_captura_jog += 1

        for mov in estado.moves[adversario]:
            if mov[0] == 'avança' or mov[0] == 'avança-esq' or mov[0] == 'avança-dir':
                poss_avanco_adv += 1
            elif mov[0] == 'come-esq' or mov[0] == 'come-dir':
                poss_captura_adv += 1

        n_pecas_jog = len(tabuleiro_jog)
        n_pecas_adv = len(tabuleiro_adv)

        f = (valor_maior_jog * 0.2 + distancia_med_jog *0.1 + poss_captura_jog * 0.3 + poss_avanco_jog * 0.1 + n_pecas_jog * 0.3) - (valor_maior_adv * 0.2 + distancia_med_adv *0.1 + poss_captura_adv * 0.3 + poss_avanco_adv * 0.1 + n_pecas_adv * 0.3)


    return f

def f_aval_avanco_F3(estado,jogador):
    """
    Dados um estado e um jogador, devolve um valor numérico.
    """
    adversario = JogoAvanco.outro_jogador(jogador)
    if vitoria_avanco(jogador, estado):
        f = 6
    elif vitoria_avanco(adversario, estado):
        f = -6
    else:
        tabuleiro_jog = estado.board[jogador]
        tabuleiro_adv = estado.board[adversario]

        soma_distancias_jogador = 0
        soma_distancias_adversario = 0

        distancia_anterior = 0

        valor_maior_jog = 0
        valor_maior_adv = 0

        for posicao in tabuleiro_jog:
            if jogador == 'brancas':
                distancia = posicao[0]
            else:
                distancia = 8 - posicao[0]
            valor_maior_jog = max(distancia_anterior, distancia)
            soma_distancias_jogador += distancia
            distancia_anterior = distancia
        for posicao in tabuleiro_adv:
            if adversario == 'brancas':
                distancia = posicao[0]
            else:
                distancia = 8 - posicao[0]
            valor_maior_adv = max(distancia_anterior, distancia)
            soma_distancias_jogador += distancia
            distancia_anterior = distancia

        distancia_med_jog = soma_distancias_jogador / len(tabuleiro_jog)
        distancia_med_adv = soma_distancias_adversario / len(tabuleiro_adv)

        poss_captura_jog = 0
        poss_captura_adv = 0

        poss_avanco_jog = 0
        poss_avanco_adv = 0

        for mov in estado.moves[jogador]:
            if mov[0] == 'avança' or mov[0] == 'avança-esq' or mov[0] == 'avança-dir':
                poss_avanco_jog += 1
            elif mov[0] == 'come-esq' or mov[0] == 'come-dir':
                poss_captura_jog += 1

        for mov in estado.moves[adversario]:
            if mov[0] == 'avança' or mov[0] == 'avança-esq' or mov[0] == 'avança-dir':
                poss_avanco_adv += 1
            elif mov[0] == 'come-esq' or mov[0] == 'come-dir':
                poss_captura_adv += 1

        n_pecas_jog = len(tabuleiro_jog)
        n_pecas_adv = len(tabuleiro_adv)

        f = (valor_maior_jog * 0.2 + distancia_med_jog *0.2 + poss_captura_jog * 0.2 + poss_avanco_jog * 0.2 + n_pecas_jog * 0.2) - (valor_maior_adv * 0.2 + distancia_med_adv *0.2 + poss_captura_adv * 0.2 + poss_avanco_adv * 0.2 + n_pecas_adv * 0.2)


    return f

    
def jogador_avanco_F1(jogo,estado, nivel = 5) :
    """
    Esta funcao está associada a um jogador concreto (valor do atributo 'funcao' do tipo Jogador) 
    e determina com que algoritmo vai o jogador jogar.
    """
    return alfabeta.alphabeta_search(estado, jogo, nivel, eval_fn=f_aval_avanco_F1)

def jogador_avanco_F2(jogo,estado, nivel = 5) :
    """
    Esta funcao está associada a um jogador concreto (valor do atributo 'funcao' do tipo Jogador) 
    e determina com que algoritmo vai o jogador jogar.
    """
    return alfabeta.alphabeta_search(estado, jogo, nivel, eval_fn=f_aval_avanco_F2)

def jogador_avanco_F3(jogo,estado, nivel = 5) :
    """
    Esta funcao está associada a um jogador concreto (valor do atributo 'funcao' do tipo Jogador) 
    e determina com que algoritmo vai o jogador jogar.
    """
    return alfabeta.alphabeta_search(estado, jogo, nivel, eval_fn=f_aval_avanco_F3)
