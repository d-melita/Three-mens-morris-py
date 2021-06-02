#Segundo Projeto de FP - Jogo do Moinho - Diogo Melita ist199202

#TAD Posicao
#Representacao interna: lista de dois elementos em que o primeiro corresponde 
#a coluna e o segundo elemento corresponde a linha. eg: ['a', '1']

#cria_posicao: string x string -> posicao
#cria_copia_posicao: posicao -> posicao
#obter_pos_c: posicao -> str
#ober_pos_l: posicao -> str
#eh_posicao: universal -> booleano
#posicoes_iguais: posicao x posicao -> booleano
#posicao_para_str: posicao -> str
#obter_posicoes_adjacentes: posicao -> tuplo de posicoes

def cria_posicao(c, l):
    '''cria_posicao(c, l) recebe duas cadeias de caracteres correspondentes a
    coluna c e a linha l de uma posicao e devolve a posicao correspondente. 
    Caso os argumentos dados sejam invalidos e gerado um ValueError com a 
    mensagem 'cria_posicao: argumentos invalidos'.'''
    if type(c) != str or type(l) != str:
        raise ValueError('cria_posicao: argumentos invalidos')
    if c != 'a' and c != 'b' and c != 'c':
        raise ValueError('cria_posicao: argumentos invalidos')
    if l != '1' and l != '2' and l != '3':
        raise ValueError('cria_posicao: argumentos invalidos')
    p = []
    return p + [c] + [l]
    
def cria_copia_posicao(p):
    '''cria_copioa_posicao(p) recebe uma posicao e devolve uma copia nova da 
    posicao.'''
    copia = [p[0], p[1]]
    return copia

def obter_pos_c(p):
    '''obter_pos_c(p) devolve a componente coluna c da posicao p '''
    return p[0]

def obter_pos_l(p):
    '''obter_pos_l(p) devolve a componente linha l da posicao p'''
    return p[1]
    
def eh_posicao(arg):
    '''eh_posicao(arg) devolve True caso o argumento seja uma posicao com o 
    formato ['c', 'l'] e False caso contrario'''
    if type(arg) != list:
        return False
    if arg[0] != 'a' and arg[0] != 'b' and arg[0] != 'c':
        return False
    if arg[1] != '1' and arg[1] != '2' and arg[1] != '3':
        return False
    return True

def posicoes_iguais(p1, p2):
    '''posicoes_igauis(p1, p2) devolve True se e so se p1 e p2 sao posicoes e 
    sao iguais'''
    if not eh_posicao(p1) or not eh_posicao(p2):
        return False
    return p1 == p2

def posicao_para_str(p):
    '''posicao_para_str(p) devolve a cadeia de caracteres 'cl' que representa 
    o seu argumento, sendo c a coluna de p e l a linha de p.'''
    return p[0] + p[1]

def obter_posicoes_adjacentes(p):
    '''obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes
    a posicao p de acordo com a ordem de leitura do tabuleiro'''
    if p == cria_posicao('a', '1'):
        return (cria_posicao('b', '1'), cria_posicao('a', '2'),\
                cria_posicao('b', '2'))
    if p == cria_posicao('b', '1'):
        return (cria_posicao('a', '1'), cria_posicao('c', '1'), \
                cria_posicao('b', '2'))
    if p == cria_posicao('c', '1'):
        return (cria_posicao('b', '1'), cria_posicao('b', '2'), \
                cria_posicao('c', '2'))
    if p == cria_posicao('a', '2'):
        return (cria_posicao('a', '1'), cria_posicao('b', '2'), \
                cria_posicao('a', '3'))
    if p == cria_posicao('b', '2'):
        return (cria_posicao('a', '1'), cria_posicao('b', '1'), \
                cria_posicao('c', '1'), cria_posicao('a', '2'), \
                cria_posicao('c', '2'), cria_posicao('a', '3'), \
                cria_posicao('b', '3'), cria_posicao('c', '3'))
    if p == cria_posicao('c', '2'):
        return (cria_posicao('c', '1'), cria_posicao('b', '2'), \
                cria_posicao('c', '3'))
    if p == cria_posicao('a', '3'):
        return (cria_posicao('a', '2'), cria_posicao('b', '2'), \
                cria_posicao('b', '3'))
    if p == cria_posicao('b', '3'):
        return (cria_posicao('b', '2'), cria_posicao('a', '3'), \
                cria_posicao('c', '3'))
    if p == cria_posicao('c', '3'):
        return (cria_posicao('b', '2'), cria_posicao('c', '2'), \
                cria_posicao('b', '3'))

#TAD peca
#Representacao interna: lista de um elemento (['X'], ['O'] ou [' '])
#cria_peca: string -> peca
#cria_copia_peca: peca -> peca
#eh_peca: universal -> booleano
#peca_para_str: peca-> str
#peca_para_inteiro: peca -> Z

def cria_peca(s):
    '''cria_peca(s) recebe uma cadeia de caracteres que corresponde ao
    identificador de um dos dois jogadores ('X' ou 'O') ou a peca livre (' ') e 
    devolve a peca correspondente no formato de uma lista de um elemento. Caso
    o argumento introduzido seja invalido, e gerado um ValueError com a seguinte
    mensagem 'cria_peca: argumento invalido'.'''
    if type(s) != str:
        raise ValueError('cria_peca: argumento invalido')
    if s != ' ' and s != 'X' and s != 'O':
        raise ValueError('cria_peca: argumento invalido')
    res = []
    res += s
    return res

def cria_copia_peca(s):
    '''cria_copia_peca(s) recebe uma peca e devolve uma copia nova da peca'''
    return s.copy()

def eh_peca(arg):
    '''eh_peca(arg) devolve True caso o argumento introduzido seja uma peca e 
    False em caso contrario'''
    if type(arg) != list:
        return False
    if len(arg) != 1:
        return False
    if arg[0] != 'X' and arg[0] != ' ' and arg[0] != 'O':
        return False
    return True

def pecas_iguais(j1, j2):
    '''pecas_iguais(j1, j2) devolve True se e so se j1 e j2 sao pecas e sao 
    iguais'''
    if not eh_peca(j1) or not eh_peca(j2):
        return False
    return j1 == j2

def peca_para_str(s):
    '''peca_para_str(s) devolve a cadeia de caracteres que reprensenta o 
    jogador dono da peca, isto e, '[X]', '[O]' ou '[ ]'.'''
    if s == cria_peca(' '):
        return '[ ]'
    if s == cria_peca('X'):
        return '[X]'
    if s == cria_peca('O'):
        return '[O]'

def peca_para_inteiro(s):
    '''peca_para_inteiro(s) devolve um inteiro valor 1, -1, 0 dependendo se a
    peca e do jogador 'X', 'O' ou ' ' respetivamente.'''
    if s == cria_peca(' '):
        return 0
    if s == cria_peca('X'):
        return 1
    if s == cria_peca('O'):
        return -1

#TAD tabuleiro
#Representacao interna: Lista de listas de pecas
#cria_tabuleiro: {} -> tabuleiro
#cria_copia_tabuleiro: tabuleiro -> tabuleiro
#obter_peca: tabuleiro x posicao -> peca
#obter_vetor: tabuleiro x str -> tuplo de pecas
#coloca_peca: tabuleiro x peca x posicao -> tabuleiro
#remove_peca: tabuleiro x posicao -> tabuleiro
#move_peca: tabuleiro x posicao x posicao -> tabuleiro
#eh_tabuleiro: universal -> booleano
#eh_posicao_livre: tabuleiro x posicao -> booleano
#tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
#tabuleiro_para_str: tabuleiro -> str
#tuplo_para_tabuleiro: tuplo -> tabuleiro
#obter_ganhador: tabuleiro -> peca
#obter_posicoes_livres: tabuleiro -> tuplo de posicoes
#obter_posicoes_jogador: tabuleiro -> tuplode posicoes

def cria_tabuleiro():
    '''cria_tabuleiro() devolve um tabuleiro de jogo do moinho de 3x3 sem 
    posicoes ocupadas por pecas de jogador'''
    return [[cria_peca(' '), cria_peca(' '), cria_peca(' ')], \
           [cria_peca(' '), cria_peca(' '), cria_peca(' ')], \
           [cria_peca(' '), cria_peca(' '), cria_peca(' ')]]


def cria_copia_tabuleiro(t):
    '''cria_copia_tabuleiro(t) recebe um tabuleiro e devolve uma copia nova do 
    tabuleiro'''
    return [[cria_copia_peca(t[0][0]), cria_copia_peca(t[0][1]), \
            cria_copia_peca(t[0][2])], [cria_copia_peca(t[1][0]), \
            cria_copia_peca(t[1][1]), cria_copia_peca(t[1][2])], \
            [cria_copia_peca(t[2][0]), cria_copia_peca(t[2][1]), \
             cria_copia_peca(t[2][2])]]

def obter_peca(t, p):
    '''obter_peca(t, p) devolve a peca na posicao p do tabuleiro t'''
    #p = [coluna, linha]
    if p[0] == 'a':
        n = 0
    elif p[0] == 'b':
        n = 1
    elif p[0] == 'c':
        n = 2
        
    if p[1] == '1':
        m = 0
    elif p[1] == '2':
        m = 1
    elif p[1] == '3':
        m = 2
    return cria_peca(t[m][n][0])

def obter_vetor(t, s):
    '''obter_vetor(t, s) devolve todas as pecas da linha ou coluna especificada
    pelo argumento s'''
    if s == 'a': #primeira coluna:
        return (cria_peca(t[0][0][0]), cria_peca(t[1][0][0]), \
                          cria_peca(t[2][0][0]))
    elif s == 'b': #segunda coluna
        return (cria_peca(t[0][1][0]), cria_peca(t[1][1][0]), \
                 cria_peca(t[2][1][0]))
    elif s == 'c': #terceira coluna
        return (cria_peca(t[0][2][0]), cria_peca(t[1][2][0]), \
                                                 cria_peca(t[2][2][0]))
    elif s == '1': #primeira linha
        return (cria_peca(t[0][0][0]), cria_peca(t[0][1][0]), \
                                             cria_peca(t[0][2][0]))
    elif s == '2': #segunda linha
        return (cria_peca(t[1][0][0]), cria_peca(t[1][1][0]), \
                                             cria_peca(t[1][2][0]))
    elif s == '3': #terceira linha
        return (cria_peca(t[2][0][0]), cria_peca(t[2][1][0]), \
                                             cria_peca(t[2][2][0]))
    
def coloca_peca(tab, peca, pos):
    '''coloca_peca(tab, peca, pos) modifica destrutivamente o tabuleiro t 
    colocando a peca j na posicao p e devolve o proprio tabuleiro'''
    #pos = [coluna, linha]
    n = pos[0]
    m = pos[1]
    if n == 'a':
        n = 0
    elif n == 'b':
        n = 1
    elif n == 'c':
        n = 2
    
    if m == '1':
        m = 0
    elif m == '2':
        m = 1
    elif m == '3':
        m = 2
        
    tab[m][n] = cria_peca(peca[0])
    return tab

def remove_peca(tab, pos):
    '''remove_peca(tab, pos) modifica destrutivamente o tabuleiro tab removendo
    a peca da posicao p e devolve o proprio tabuleiro'''
    #pos = [coluna, linha]
    n = pos[0]
    m = pos[1]
    if n == 'a':
        n = 0
    elif n == 'b':
        n = 1
    elif n == 'c':
        n = 2
    
    if m == '1':
        m = 0
    elif m == '2':
        m = 1
    elif m == '3':
        m = 2
        
    tab[m][n] = cria_peca(' ')
    return tab

def move_peca(tab, pos1, pos2):
    '''move_peca(tab, pos1, pos2) modifica destrutivamente o tabuleiro tab 
    movendo a peca que se encontra na posicao pos1 para a posicao pos2 e devolve
    o proprio tabuleiro'''
    peca = cria_peca(obter_peca(tab, pos1)[0])
    remove_peca(tab, pos1)
    return coloca_peca(tab, peca, pos2)

def eh_tabuleiro(t):
    '''eh_tabuleiro(t) devolve True caso o seu argumento seja um tabuleiro 
    representado por uma lista de listas de pecas. Um tabuleiro valido pode ter
    um maximo de 3 pecas de cada jogador, nao pode conter mais de 1 peca a mais
    de um jogador em relacao ao adversario e apenas pode ter 1 jogador ganhador.
    Se alguma destas condicoes nao se verificar a funcao devolve False.'''
    if type(t) != list:
        return False
    contadorX = 0
    contadorO = 0
    i = 0
    while i < 3:
        if type(t[i]) != list:
            return False
        if len(t[i]) != 3:
            return False
        n = 0
        while n < 3:
            if type(t[i][n]) != list:
                return False
            if t[i][n] != cria_peca(' ') and t[i][n] != cria_peca('X')\
               and t[i][n] != cria_peca('O'):
                return False
            if t[i][n] == cria_peca('X'):
                contadorX += 1
            elif t[i][n] == cria_peca('O'):
                contadorO += 1
            if contadorX > 3 or contadorO > 3: #max de 3 pecas por jogador
                return False
            n += 1
        i += 1
    #verificar se um jogador tem mais duas pecas que o adversario
    if contadorX > (contadorO + 1) or contadorO > (contadorX + 1):
        return False
    jgX = 0
    jgO = 0
    for i in ['a', 'b', 'c', '1', '2', '3']:
        if obter_vetor(t, i)[0] == obter_vetor(t, i)[1] == obter_vetor(t, i)[2]\
           == cria_peca('X'):
            jgX = 1
        if obter_vetor(t, i)[0] == obter_vetor(t, i)[1] == obter_vetor(t, i)[2]\
           == cria_peca('O'):
            jgO = 1
    if jgX == jgO == 1: # mais que um jogador ganhador
        return False
    return True

def eh_posicao_livre(t, pos):
    '''eh_posicao_livre(t, pos) devolve true apenas se a posicao pos do
    tabuleiro t corresponder a uma posicao livre.'''
    #pos = [coluna, linha]
    n = pos[0]
    m = pos[1]
    if n == 'a':
        n = 0
    elif n == 'b':
        n = 1
    elif n == 'c':
        n = 2
    if m == '1':
        m = 0
    elif m == '2':
        m = 1
    elif m == '3':
        m = 2
    return t[m][n] == cria_peca(' ')

def tabuleiros_iguais(t1, t2):
    '''tabuleiros_iguais(t1, t2) devolve True apenas se t1 e t2 sao tabuleiros e
    sao iguais'''
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False
    return t1[0][0] == t2[0][0] and t1[0][1] == t2[0][1] and \
           t1[0][2] == t2[0][2] and t1[1][0] == t2[1][0] and \
           t1[1][1] == t2[1][1] and t1[1][2] == t2[1][2] and \
           t1[2][0] == t2[2][0] and t1[2][1] == t2[2][1] and \
           t1[2][2] == t2[2][2]

def tabuleiro_para_str(t):
    '''tabuleiro_para_str(t) devolve a cadeia de caracteres que representa o 
    tabuleiro visualmente'''
    res = ''
    res += '   a   b   c\n' #primeira linha
    res +='1 ' #segunda linha:
    j = 0
    n = 0
    while n < 3:
        if t[j][n] == cria_peca(' '):
            res += '[ ]'
        if t[j][n] == cria_peca('X'):
            res += '[X]'
        if t[j][n] == cria_peca('O'):
            res += '[O]'
        if n < 2:
            res += '-'
        n += 1
    res += '\n   | \ | / |\n' #terceira linha
    res +='2 ' #quarta linha:
    j = 1
    n = 0    
    while n < 3:
        if t[j][n] == cria_peca(' '):
            res += '[ ]'
        if t[j][n] == cria_peca('X'):
            res += '[X]'
        if t[j][n] == cria_peca('O'):
            res += '[O]'
        if n < 2:
            res += '-'
        n += 1
    res += '\n   | / | \ |\n' #quinta linha
    res +='3 '  #sexta linha:
    j = 2
    n = 0
    while n < 3:
        if t[j][n] == cria_peca(' '):
            res += '[ ]'
        if t[j][n] == cria_peca('X'):
            res += '[X]'
        if t[j][n] == cria_peca('O'):
            res += '[O]'
        if n < 2:
            res += '-'
        n += 1
    return res

def tuplo_para_tabuleiro(t):
    '''tuplo_pra_tabuleiro(t) devolve o tabuleiro que e representado pelo tuplo
    t com 3 tuplos, cada um deles com 3 valores inteiros iguais a 1, -1 ou 0'''
    tabuleiro = []
    for l in t:
        linha = []
        for posicao in l:
            if posicao == 0:
                linha = linha + [cria_peca(' ')]
            elif posicao == 1:
                linha = linha + [cria_peca('X')]
            elif posicao == -1:
                linha = linha + [cria_peca('O')]
        tabuleiro = tabuleiro + [linha,]
    return tabuleiro

def obter_ganhador(t):
    '''obter_ganhador(t) devolve uma peca do jogador que tenha as suas 3 pecas 
    em linha na vertical ou na horizontal do tabuleiro. Se nao existir nenhum 
    ganhador devolve uma peca livre''' 
    for i in ['a', 'b', 'c', '1', '2', '3']:
        if obter_vetor(t, i)[0] == obter_vetor(t, i)[1] == obter_vetor(t, i)[2]\
           == cria_peca('X'):
            return cria_peca('X')
        if obter_vetor(t, i)[0] == obter_vetor(t, i)[1] == obter_vetor(t, i)[2]\
           == cria_peca('O'):
            return cria_peca('O')
    return cria_peca(' ')

def obter_posicoes_livres(t):
    '''obter_posicoes_livres(t) devolve um tuplo com as posicoes nao ocupadas
    pelas pecas de qualquer um dos dois jogadores na ordem de leitura do 
    tabuleiro'''
    res = ()
    for i in [cria_posicao('a', '1'), cria_posicao('b', '1'), \
          cria_posicao('c', '1'), cria_posicao('a', '2'), \
          cria_posicao('b', '2'), cria_posicao('c', '2'), \
          cria_posicao('a', '3'), cria_posicao('b', '3'), \
          cria_posicao('c', '3')]:
        if eh_posicao_livre(t, i):
            res += (i,)
    return res

def obter_posicoes_jogador(t, p):
    '''obter_posicoes_jogador(t, p) devolve um tuplo com as posicoes ocupadas 
    pelas pecas p de um dos dois jogadores na ordem de leitura do tabuleiro'''
    res = ()
    for i in [cria_posicao('a', '1'), cria_posicao('b', '1'), \
          cria_posicao('c', '1'), cria_posicao('a', '2'), \
          cria_posicao('b', '2'), cria_posicao('c', '2'), \
          cria_posicao('a', '3'), cria_posicao('b', '3'), \
          cria_posicao('c', '3')]:
        n = i[0]
        m = i[1]
        if n == 'a':
            n = 0
        elif n == 'b':
            n = 1
        elif n == 'c':
            n = 2
        if m == '1':
            m = 0
        elif m == '2':
            m = 1
        elif m == '3':
            m = 2        
        if t[m][n] == p:
            res += (i,)
    return res

def mv(t, pos1, pos2): #movimento valido
    '''tabuleiro x posicao x posicao -> booleano. Esta funcao auxiliar serve 
    para verificar se o movimento do jogador e valido ou nao, isto e, se o 
    jogador move a sua peca para uma posicao adjacente livre. Caso todas as 
    posicoes adjacentes das suas pecas estejam ocupadas a movimentacao da peca 
    para a mesma posicao e considerado um movimento valido'''
    if pos1 == pos2:
        pj = obter_posicoes_jogador(t, obter_peca(t, pos1)) #pecas jogador = pj
        a = pj[0]
        b = pj[1]
        c = pj[2]
        a1 = obter_posicoes_adjacentes(a)
        b1 = obter_posicoes_adjacentes(b)
        c1 = obter_posicoes_adjacentes(c)
        #verificar se todas as pecas do jogador estao bloqueadas
        if obter_peca(t, a1[0]) != cria_peca(' ') and \
           obter_peca(t, a1[1]) != cria_peca(' ') and \
           obter_peca(t, a1[2]) != cria_peca(' ') and \
           obter_peca(t, b1[0]) != cria_peca(' ') and \
           obter_peca(t, b1[1]) != cria_peca(' ') and \
           obter_peca(t, b1[2]) != cria_peca(' ') and \
           obter_peca(t, c1[0]) != cria_peca(' ') and \
           obter_peca(t, c1[1]) != cria_peca(' ') and \
           obter_peca(t, c1[2]) != cria_peca(' '):
            return True
        else:
            return False
    else:
        return False
        
def obter_movimento_manual(t, peca):
    '''tabuleiro x peca -> tuplo de posicoes. Funcao auxiliar que recebe um 
    tabuleiro e a peca de um jogador e dveolve um tuplo com uma ou duas posicoes
    que representam uma posicao ou um movimento introduzido pelo jogador. 
    Na fase de colocacao , o tuplo contem apenas a posicao introduzaida pelo 
    utilizador onde colcoar uma nova peca. Na fase de movimento, o tuplo contem
    a posicao de origem e a posicao de destino da peca a movimentar. Se nao 
    for possivel movimentar nenhuma peca por estarem todas bloqueadas, o jogador
    pode movimentar uma peca para a mesma posicao. Se o valor introduzido pelo 
    jogador nao corresponder a uma posicao ou a um movimento valido e a funcao 
    deve gerar um erro com a mensagem 'obter_movimento_manual: escolha invalida'
    A funcao apresenta a mensagem 'Turno do jogador. escolha uma posicao: ' ou 
    'Turno do jogador. Escolha um movimento: ' para pedir ao utilizador para 
    introduzir uma posicao ou um movimento. '''
    contador_peca = 0 #fase de colocacao
    i = 0
    res = ()
    while i < 3:
        n = 0
        while n < 3:
            if cria_peca(t[i][n][0]) == peca:
                contador_peca += 1
            n += 1
        i += 1
    if contador_peca < 3:
        m = input('Turno do jogador. Escolha uma posicao: ')
        if m != 'a1' and m != 'b1' and m != 'c1' and m != 'a2' and \
            m != 'b2' and m != 'c2' and m != 'a3' and m != 'b3' and \
            m != 'c3':
            raise ValueError('obter_movimento_manual: escolha invalida')
        if cria_posicao(m[0], m[1]) not in obter_posicoes_livres(t):
            raise ValueError('obter_movimento_manual: escolha invalida')        
        return res + (cria_posicao(m[0], m[1]),)
    else: #fase movimento - ja ha 3 pecas do jogador    
        m = input('Turno do jogador. Escolha um movimento: ')
        if len(m) != 4 or m[0] + m[1] not in ('a1', 'b1', 'c1', 'a2', 'b2', \
            'c2', 'a3', 'b3', 'c3') or m[2] + m[3] not in ('a1', 'b1', 'c1', \
            'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
            raise ValueError('obter_movimento_manual: escolha invalida')
        n = cria_posicao(m[0], m[1]) #posicao de partida
        p = cria_posicao(m[2], m[3]) #posicao de chegada        
        if n not in obter_posicoes_jogador(t, peca):
            raise ValueError('obter_movimento_manual: escolha invalida')
        if posicoes_iguais(n, p):
            if not mv(t, n, p):
                raise ValueError('obter_movimento_manual: ' + \
                        'escolha invalida')
            return res + (n,) + (p,)
        if not posicoes_iguais(n, p):
            if p not in obter_posicoes_adjacentes(n):
                raise ValueError('obter_movimento_manual: escolha invalida')
            if p not in obter_posicoes_livres(t):
                raise ValueError('obter_movimento_manual: escolha invalida')
            return res + (n,) + (p,)
        
def obter_movimento_auto(t, peca, string):
    '''tabuleiro x peca x str -> tuplo de posicoes. Funcao auxiliar que recebe 
    um tabuleiro, uma peca de um jogador e uma cadeia de caracteres que 
    representa o nivel de dificuldade do jogo e dolve um tuplo com uma ou 
    duas posicoes que representam uma posicao ou um movimento escolhido 
    automaticamente. Para qualquer nivel, a fase de colocao segue as regras da 
    seccao 1.3.1 do enunciado. Na fase de movimento existem diferencas consoante 
    o nivel do jogo. Caso seja facil, e movida a primeira peca na ordem de
    leitura do tabuleiro da maquina que contenha alguma posicao adjacente livre 
    para a primeira posicao ajdacente livre. Caso o nivel seja normal e 
    utilizado o algoritmo minimax com nivel de recursao igual a 1. Caso o nivel
    seja dificil o nivel de recursao e igual a 5.'''
    if string == 'facil':
        return oma_facil(t, peca)
    elif string == 'normal':
        return oma_normal(t, peca)
    elif string == 'dificil':
        return oma_dificil(t, peca)

def cantos(t):
    '''tabuleiro -> posicao. Devolve a posicao correspondente ao primeiro
    canto livre na ordem de leitura do tabuleiro'''
    if t[0][0] == cria_peca(' '):
        return (['a', '1'],)
    elif t[0][2] == cria_peca(' '):
        return (['c', '1'],)
    elif t[2][0] == cria_peca(' '):
        return (['a', '3'],)
    elif t[2][2] == cria_peca(' '):
        return (['c', '3'],)
    
def cantos_possivel(t):
    '''tabuleiro -> booleano. Devolve True caso seja possivel jogar num canto e 
    False caso contrario'''
    if cantos(t) == None:
        return False
    return True

def laterais(t):
    '''tabuleiro -> posicao. Devolve a posicao correspondente a primeira 
    lateral livre na ordem de leitura do tabuleiro'''    
    if t[0][1] == cria_peca(' '):
        return (['b', '1'],)
    elif t[1][0] == cria_peca(' '):
        return (['a', '2'],)
    elif t[1][2] == cria_peca(' '):
        return (['c', '2'],)
    elif t[2][1] == cria_peca(' '):
        return (['b', '3'],)

def laterais_possivel(t):
    '''tabuleiro -> booleano. Devolve True caso seja possivel jogar numa lateral 
    e False caso contrario'''    
    if laterais(t) == None:
        return False
    return True
        
def vitoria(t, peca):
    '''tabuleiro x peca -> posicao. Devolve a posicao na qual se obtem 3 pecas 
    em linha do jogador'''
    for i in [cria_posicao('a', '1'), cria_posicao('b', '1'), \
          cria_posicao('c', '1'), cria_posicao('a', '2'), \
          cria_posicao('b', '2'), cria_posicao('c', '2'), \
          cria_posicao('a', '3'), cria_posicao('b', '3'), \
          cria_posicao('c', '3')]:
        if eh_posicao_livre(t, i):
            t1 = cria_copia_tabuleiro(t)
            if obter_ganhador(coloca_peca(t1, peca, i)) == peca:
                return (i,)        
            
def vitoria_possivel(t, peca):
    '''tabuleiro x peca -> booleano. Devolve True caso seja possivel obter a
    vitoria num determinado tabuleiro t e False caso contrario'''
    if vitoria(t, peca) == None:
        return False
    return True

def bloqueio(t, peca):
    '''tabuleiro x peca -> posicao. Devolve a posicao na qual se impede o 
    adversario de ter 3 pecas em linha'''
    if peca == cria_peca('X'):
        for i in [cria_posicao('a', '1'), cria_posicao('b', '1'), \
          cria_posicao('c', '1'), cria_posicao('a', '2'), \
          cria_posicao('b', '2'), cria_posicao('c', '2'), \
          cria_posicao('a', '3'), cria_posicao('b', '3'), \
          cria_posicao('c', '3')]:
            if eh_posicao_livre(t, i):
                t1 = cria_copia_tabuleiro(t)
                if obter_ganhador(coloca_peca(t1, ['O'], i)) == ['O']:
                    return (i,)
    if peca == cria_peca('O'):
        for i in [cria_posicao('a', '1'), cria_posicao('b', '1'), \
          cria_posicao('c', '1'), cria_posicao('a', '2'), \
          cria_posicao('b', '2'), cria_posicao('c', '2'), \
          cria_posicao('a', '3'), cria_posicao('b', '3'), \
          cria_posicao('c', '3')]:
            if eh_posicao_livre(t, i):
                t1 = cria_copia_tabuleiro(t)
                if obter_ganhador(coloca_peca(t1, ['X'], i)) == ['X']:
                    return (i,)
                
def bloqueio_possivel(t, peca):
    '''tabuleiro x peca -> booleano. Devolve True caso seja possivel bloquear a 
    vitoria do adversario num determinado tabuleiro t e False caso contrario'''    
    if bloqueio(t, peca) == None:
        return False
    return True

def oma_facil(t, peca): #oma = obter movimento auto
    '''tabuleiro x peca -> tuplo de posicoes. Funcao auxiliar para o nivel
    facil. '''
    #fase colocacao
    contador_peca = 0 #fase de colocacao
    i = 0
    res = ()
    while i < 3:
        n = 0
        while n < 3:
            if cria_peca(t[i][n][0]) == peca:
                contador_peca += 1
            n += 1
        i += 1
    if contador_peca < 3:    
        if vitoria_possivel(t, peca):
            return vitoria(t, peca)
        elif bloqueio_possivel(t, peca):
            return bloqueio(t, peca)
        elif t[1][1] == cria_peca(' '): # centro livre
            return (cria_posicao('b', '2'),)
        elif cantos_possivel(t):
            return cantos(t)
        elif laterais_possivel(t):
            return laterais(t)
    else: #fase de movimentacao = ja ha 3 pecas do jogador
        p3 = ()
        p1 = obter_posicoes_jogador(t, peca)
        p11 = p1[0]
        p2 = obter_posicoes_adjacentes(p11)
        if obter_peca(t, p2[0]) == cria_peca(' '):
            p3 = p2[0]
        elif obter_peca(t, p2[1]) == cria_peca(' '):
            p3 = p2[1]
        elif obter_peca(t, p2[2]) == cria_peca(' '):
            p3 = p2[2]
        if p3 != ():
            return (p11, p3)
        p11 = p1[1]
        p2 = obter_posicoes_adjacentes(p11)
        if obter_peca(t, p2[0]) == cria_peca(' '):
            p3 = p2[0]
        elif obter_peca(t, p2[1]) == cria_peca(' '):
            p3 = p2[1]
        elif obter_peca(t, p2[2]) == cria_peca(' '):
            p3 = p2[2]
        if p3 != ():
            return (p11, p3)
        p11 = p1[2]
        p2 = obter_posicoes_adjacentes(p11)
        if obter_peca(t, p2[0]) == cria_peca(' '):
            p3 = p2[0]
        elif obter_peca(t, p2[1]) == cria_peca(' '):
            p3 = p2[1]
        elif obter_peca(t, p2[2]) == cria_peca(' '):
            p3 = p2[2]
        if p3 != ():
            return (p11, p3)
        else:
            return(p1[0], p1[0])

def oma_normal(t, peca): #oma = obter movimento auto
    '''tabuleiro x peca -> tuplo de posicoes. Funcao auxiliar para o nivel
    normal. '''    
    #fase colocacao
    contador_peca = 0
    i = 0
    res = ()
    while i < 3:
        n = 0
        while n < 3:
            if cria_peca(t[i][n][0]) == peca:
                contador_peca += 1
            n += 1
        i += 1
    if contador_peca < 3:    
        if vitoria_possivel(t, peca):
            return vitoria(t, peca)
        elif bloqueio_possivel(t, peca):
            return bloqueio(t, peca)
        elif t[1][1] == cria_peca(' '):
            return (cria_posicao('b', '2'),)
        elif cantos_possivel(t):
            return cantos(t)
        elif laterais_possivel(t):
            return laterais(t)
    else: #fase de movimentacao
        m = minimax(t, peca, 1, ())
        return (m[1][0][0], m[1][0][1])
    
def oma_dificil(t, peca): #oma = obter movimento auto
    '''tabuleiro x peca -> tuplo de posicoes. Funcao auxiliar para o nivel
    dificil. '''    
    #fase colocacao
    contador_peca = 0 #fase de colocacao
    i = 0
    res = ()
    while i < 3:
        n = 0
        while n < 3:
            if cria_peca(t[i][n][0]) == peca:
                contador_peca += 1
            n += 1
        i += 1
    if contador_peca < 3:    
        if vitoria_possivel(t, peca):
            return vitoria(t, peca)
        elif bloqueio_possivel(t, peca):
            return bloqueio(t, peca)
        elif t[1][1] == cria_peca(' '):
            return (cria_posicao('b', '2'),)
        elif cantos_possivel(t):
            return cantos(t)
        elif laterais_possivel(t):
            return laterais(t)
    else: #fase de movimentacao
        m = minimax(t, peca, 5, ())
        return (m[1][0][0], m[1][0][1])

def minimax(t, peca, np, sm): #np = nivel profundidade, sm = seq movimentos
    '''Funcao recursiva auxiliar para obter o melhor movimento para os niveis
    de dificuldade normal e dificil.'''
    if obter_ganhador(t) != cria_peca(' ') or np == 0:
        return (peca_para_inteiro(obter_ganhador(t)), sm)
    else:
        melhor_seq_movimentos = ()
        if peca == cria_peca('X'):
            outra_peca = cria_peca('O')
        if peca == cria_peca('O'):
            outra_peca = cria_peca('X')        
        melhor_resultado = -peca_para_inteiro(outra_peca)
        for i in obter_posicoes_jogador(t, peca):
            for n in obter_posicoes_adjacentes(i):
                if eh_posicao_livre(t, n):
                    copia = cria_copia_tabuleiro(t)
                    novo_mov = (i, n)
                    novo_t = move_peca(copia, i, n)
                    novo_resultado, nova_seq_mov = minimax(novo_t, outra_peca, \
                                                    np-1, sm + (novo_mov,))
                    if melhor_seq_movimentos == () or (peca == cria_peca('X')\
                        and novo_resultado > melhor_resultado) or \
                       (peca == cria_peca('O') and \
                        novo_resultado < melhor_resultado):
                        melhor_resultado, melhor_seq_movimentos = \
                            novo_resultado, nova_seq_mov
        
        return (melhor_resultado, melhor_seq_movimentos)
    
def moinho(peca, modo):
    '''str x str -> str. Funcao principal que permite jogar um jogo completo do
    jogo do moinho de um jogador contra o computador. A funcao recebe duas 
    cadeias de caracteres e devolve a representacao externa da peca ganhadora. 
    O primeiro argumento corresponde a representacao externa da peca com que 
    deseja jogar o humano e o segundo argumento corresponde ao nivel de 
    dificuldade. Se algum dos argumentos introduzidos for invalido, a funcao 
    deve gerar um erro com a mensagem 'moinho: argumentos invalidos'. A funcao 
    deve aprensentar a mensagem 'Turno do computador (<nivel>): ' em que 
    <nivel> corresponde a cadeia de caracteres passada como argumento, quando 
    for o turno do computrador,'''
    if peca != '[X]' and peca != '[O]':
        raise ValueError('moinho: argumentos invalidos')
    if modo != 'facil' and modo != 'normal' and modo != 'dificil':
        raise ValueError('moinho: argumentos invalidos')
    
    if peca == '[X]':
        jogador = cria_peca('X')
    if peca == '[O]':
        jogador = cria_peca('O')
        
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade {}.'.format(modo))
    
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    
    while obter_ganhador(t) == cria_peca(' '):
        if jogador == cria_peca('X'):
            pc = cria_peca('O')
            
            pos = obter_movimento_manual(t, jogador)
            if len(pos) == 1:
                a = pos[0]
                print(tabuleiro_para_str(coloca_peca(t, jogador, \
                                                 cria_posicao(a[0], a[1]))))
            elif len(pos) == 2:
                a = pos[0]
                b = pos[1]
                print(tabuleiro_para_str(move_peca(t, cria_posicao(a[0], a[1]),\
                                                cria_posicao(b[0], b[1]))))
            if obter_ganhador(t) != cria_peca(' '):
                return peca_para_str(obter_ganhador(t))
            
            print('Turno do computador ({}):'.format(modo))
            pos2 = obter_movimento_auto(t, pc, modo)
            if len(pos2) == 1:
                a = pos2[0]
                print(tabuleiro_para_str(coloca_peca(t, pc, \
                                        cria_posicao(a[0], a[1]))))
            elif len(pos2) == 2:
                a = pos2[0]
                b = pos2[1]
                print(tabuleiro_para_str(move_peca(t, \
                    cria_posicao(a[0], a[1]), cria_posicao(b[0], b[1]))))
                
            if obter_ganhador(t) != cria_peca(' '):
                return peca_para_str(obter_ganhador(t))
        
        elif jogador == cria_peca('O'):
            pc = cria_peca('X')
            print('Turno do computador ({}):'.format(modo))
            pos2 = obter_movimento_auto(t, pc, modo)
            if len(pos2) == 1:
                a = pos2[0]
                print(tabuleiro_para_str(coloca_peca(t, pc, \
                                                     cria_posicao(a[0], a[1]))))
            elif len(pos2) == 2:
                a = pos2[0]
                b = pos2[1]
                print(tabuleiro_para_str(move_peca(t, cria_posicao(a[0], a[1]),\
                                                cria_posicao(b[0], b[1]))))
            if obter_ganhador(t) != cria_peca(' '):
                return peca_para_str(obter_ganhador(t))
            
            pos = obter_movimento_manual(t, jogador)
            if len(pos) == 1:
                a = pos[0]
                print(tabuleiro_para_str(coloca_peca(t, jogador, \
                                                 cria_posicao(a[0], a[1]))))
            elif len(pos) == 2:
                a = pos[0]
                b = pos[1]
                print(tabuleiro_para_str(move_peca(t, cria_posicao(a[0], a[1]),\
                                                cria_posicao(b[0], b[1]))))
            if obter_ganhador(t) != cria_peca(' '):
                return peca_para_str(obter_ganhador(t))