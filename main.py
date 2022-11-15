"""
Joao Ferreira - ist1103680
"""

# TAD Posicao - (Coordenada x, Coordenada y)

# Construtores
def cria_posicao(x, y):
    """
    cria_posicao: inteiro x inteiro --> posicao
    Recebe as coordenadas de uma funcao e devolve uma posicao
    """
    if type(x) is not int or type(y) is not int or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")
    return x, y


def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posicao x posicao --> posicao
    Recebe uma posicao e devolve uma copia da posicao
    """
    if type(pos) is not tuple or len(pos) != 2:
        raise ValueError("cria_copia_posicao: argumentos invalidos")
    return cria_posicao(pos[0], pos[1])


# Seletores
def obter_pos_x(pos):
    """
    obter_pos_x: posicao --> inteiro
    Recebe uma posicao e devolve a coordenada de eixo x
    """
    return pos[0]


def obter_pos_y(pos):
    """
    obter_pos_y: posicao --> inteiro
    Recebe uma posicao e devolve a coordenada de eixo y
    """
    return pos[1]


# Reconhecedor
def eh_posicao(arg):
    """
    eh_posicao: universal --> booleano
    Recebe um  argumento e verifica se este e uma argicao
    """
    return type(arg) is tuple and len(arg) == 2\
           and type(obter_pos_x(arg)) is int and type(
        obter_pos_y(arg)) is int and obter_pos_x(
        arg) >= 0 and obter_pos_y(arg) >= 0


# Teste
def posicoes_iguais(p1, p2):
    """
    posicoes_iguais: posicao x posicao --> booleano
    Recebe duas posicoes e verifica se sao iguais
    """
    return cria_posicao(obter_pos_x(p1), obter_pos_y(p1))\
           == cria_posicao(obter_pos_x(p2), obter_pos_y(p2))


# Transformador
def posicao_para_str(pos):
    """
    posicao_para_str: posicao --> string
    Recebe uma posicao e torna-a em string
    """
    return str(pos)


# Alto nivel
def obter_posicoes_adjacentes(p):
    """
    obter_posicoes_adjacentes: posicao --> tuplo
    Recebe uma posicao e devolve um tuplo contendo as posicoes adjacentes
    """
    return tuple(cria_posicao(possivel_pos[0], possivel_pos[1]) for possivel_pos in
                 ((obter_pos_x(p), obter_pos_y(p) - 1),
                  (obter_pos_x(p) + 1, obter_pos_y(p)),
                  (obter_pos_x(p), obter_pos_y(p) + 1),
                  (obter_pos_x(p) - 1, obter_pos_y(p)))
                 if (possivel_pos[0] >= 0 and possivel_pos[1] >= 0))


def ordenar_posicoes(posicoes):
    """
    ordenar_posicoes: tuplo --> tuplo
    Recebe um tuplo de posicoes e ordena-as
    """
    return tuple(sorted(posicoes, key=lambda pos: (obter_pos_y(pos), obter_pos_x(pos))))
    # ordena as posicoes priorizando o eixo y e depois o x


# TAD Animal -  [Especie, Frequencia de Reproducao, Frequencia de Alimentacao, Idade, Fome]


# Construtores
def cria_animal(s, r, a):
    """
    cria_animal: string x inteiro x inteiro --> animal
    Recebe a especie,frequencia de reproducao e frequencia de alimentacao de um animal e devolve um TAD do animal
    """
    if type(s) is not str or not s or\
            not isinstance(r, int) or\
            not isinstance(a, int) or r <= 0 or a < 0:
        raise ValueError("cria_animal: argumentos invalidos")
    return [s, r, a, 0, 0]


def cria_copia_animal(a):
    """
    cria_copia_animal: animal --> animal
    Recebe um animal e devolve uma copia do mesmo
    """
    if type(a) is not list or len(a) != 5 or type(a[0]) is not str or not a[0] \
            or not (int == type(a[1]) == type(a[2]) == type(a[3]) == type(a[4])) \
            or a[1] <= 0 or a[2] < 0 or a[3] < 0 or a[4] < 0:
        raise ValueError("cria_copia_animal: argumentos invalidos")
    return [arg for arg in a]


# Seletores
def obter_especie(a):
    """
    obter_especie: animal --> string
    Recebe um animal e devolve a especie do mesmo
    """
    return a[0]


def obter_freq_reproducao(a):
    """
    obter_freq_reproducao: animal --> inteiro
    Recebe um animal e devolve a sua frequencia de reproducao
    """
    return a[1]


def obter_freq_alimentacao(a):
    """
    obter_freq_alimentacao: animal --> inteiro
    Recebe um animal e devolve a sua frequencia de reproducao
    """
    return a[2]


def obter_idade(a):
    """
    obter_idade: animal --> inteiro
    Recebe um animal e devolve a sua idade
    """
    return a[3]


def obter_fome(a):
    """
    obter_fome: animal --> inteiro
    Recebe um animal e devolve a sua fome
    """
    return a[4]


# Modificadores
def aumenta_idade(a):
    """
    aumenta_idade: animal --> animal
    Recebe um animal e muda destrutivavemente o animal adicionando um valor de idade
    """
    a[3] += 1
    return a


def reset_idade(a):
    """
        reset_idade: animal --> animal
        Recebe um animal e muda destrutivavemente o animal definindo-lhe a idade para 0
    """
    a[3] = 0
    return a


def aumenta_fome(a):
    """
        aumenta_fome: animal --> animal
        Recebe um animal e muda destrutivavemente o animal adicionando um valor de fome
    """
    if eh_predador(a):
        a[4] = obter_fome(a) + 1
    return a


def reset_fome(a):
    """
            reset_fome: animal --> animal
            Recebe um animal e muda destrutivavemente o animal definindo-lhe a fome para 0
    """
    a[4] = 0
    return a


# Reconhecedor
def eh_animal(arg):
    """
    eh_animal: universal --> booleano
    Recebe um argumento e verifica se este e um animal segundo o TAD
    """
    return type(arg) is list and len(arg) == 5 and\
           type(arg[0]) is str and len(arg[0]) > 0 \
           and (int == type(arg[1]) == type(arg[2]) == type(arg[3]) == type(arg[4])) \
           and arg[1] > 0 and arg[2] >= 0 and arg[3] >= 0 and arg[4] >= 0


def eh_predador(arg):
    """
    eh_predador: universal --> booleano
    Recebe um argumento e verifica se este e um predador
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    """
    eh_presa: universal --> booleano
    Recebe um argumento e verifica se este e um predador
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


# Teste
def animais_iguais(a1, a2):
    """
    animais_iguais: animal x animal --> booleano
    Recebe dois animais e verifica se estes sao iguais
    """
    return eh_animal(a1) and eh_animal(a2) \
        and obter_especie(a1) == obter_especie(a2) \
        and obter_freq_reproducao(a1) == obter_freq_reproducao(a2) \
        and obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2)\
        and obter_idade(a1) == obter_idade(a2) \
        and obter_fome(a1) == obter_fome(a2)


# Transformador
def animal_para_char(a):
    """
    animal_para_char: animal --> string
    Recebe um animal e devolve o primeiro carater da especie em maiuscula se for predador e minuscula se for presa
    """
    if eh_predador(a):
        return obter_especie(a)[0].upper()
    return obter_especie(a)[0].casefold()


def animal_para_str(a):
    """
    animal_para_str: animal --> string
    Recebe um animal e devolve a cadeia de carateres que representa o animal
    """
    if eh_predador(a):
        return str(obter_especie(a)) + " [" + str(obter_idade(a)) +\
               "/" + str(obter_freq_reproducao(a)) + ";" + str(
            obter_fome(a)) + "/" + str(obter_freq_alimentacao(a)) + "]"
    return str(obter_especie(a)) + " [" +\
           str(obter_idade(a)) + "/" + str(obter_freq_reproducao(a)) + "]"


# Alto nivel
def eh_animal_fertil(a):
    """
    eh_animal_fertil: animal --> booleano
    Recebe um animal e verifica se este e fertil
    """
    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """
       eh_animal_faminto: animal --> booleano
       Recebe um animal e verifica se este vai morrer de fome
    """
    return obter_fome(a) >= obter_freq_alimentacao(a) and eh_predador(a)


def reproduz_animal(a):
    """
    reproduz_animal: animal --> animal
    Recebe um animal e devolve um novo animal da mesma especie com fome e idade igual a 0
    """
    reset_idade(a)
    return reset_fome(cria_copia_animal(a))


#TAD Prado - [Dimensao, Obstaculos, Animais, Posicoes dos Animais]


# Construtores
def cria_prado(d, r, a, p):
    """
    cria_prado: posicao x tuplo x tuplo x tuplo --> prado
    Recebe a posicao do canto inferior direito , um tuplo com rochedos, um tuplo com animais
     e um tuplo com as posicoes dos animais e devolve a TAD do prado
     """
    if eh_posicao(d) and tuple == type(r) == type(a) == type(p) \
            and all(eh_posicao(pos)
                    and 0 < obter_pos_x(pos) < obter_pos_x(d)
                    and 0 < obter_pos_y(pos) < obter_pos_y(d) for pos in r) \
            and (obter_pos_x(pos) not in (0, obter_pos_x(d))
                 and obter_pos_y(pos) not in (0, obter_pos_y(d)) for pos in r) \
            and a and all(eh_animal(anim) for anim in a) and len(p) == len(a) \
            and all(eh_posicao(pos)
                    and 0 < obter_pos_x(pos) < obter_pos_x(d)
                    and 0 < obter_pos_y(pos) < obter_pos_y(d) for pos in p):
        return [d, r, a, p]
    raise ValueError("cria_prado: argumentos invalidos")


def cria_copia_prado(prado):
    """
    cria_copia_prado: prado --> prado
    Recebe um prado e devolve uma copia do mesmo
    """
    if type(prado) is list and len(prado) == 4:
        return cria_prado(prado[0], prado[1], prado[2], prado[3])
    raise ValueError("cria_copia_prado:argumentos invalidos")


# Seletores
def obter_tamanho_x(prado):
    """
    obter_tamanho_x: prado --> int
    Recebe um prado e devolve o valor correspondente a dimensao x do prado
    """
    return obter_pos_x(prado[0]) + 1


def obter_tamanho_y(prado):
    """
    obter_tamanho_y: prado --> int
    Recebe um prado e devolve o valor correspondente a dimensao y do prado
    """
    return obter_pos_y(prado[0]) + 1


def obter_numero_predadores(prado):
    """
    obter_numero_predadores: prado --> int
    Recebe um prado e devolve o numero de predadores
    """
    return len(list(filter(lambda animal: eh_predador(animal), prado[2])))


def obter_numero_presas(prado):
    """
    obter_numero_presa: prado --> int
    Recebe um prado e devolve o numero de presa
    """
    return len(list(filter(lambda animal: eh_presa(animal), prado[2])))


def obter_posicao_animais(prado):
    """
    obter_posicao_animais: prado --> tuplo de posicoes
    Recebe um prado e devolve um tuplo contendo as posicoes do prado ocupadas por animais
    """
    return ordenar_posicoes(prado[3])


def obter_animal(prado, pos):
    """
    obter_animal: prado x posicao --> animal
    Recebe um prado e uma posicao e devolve o animal que esta nessa posicao
    """
    i = 0
    for ipos in range(len(prado[3])):
        if posicoes_iguais(pos, prado[3][ipos]):
            i = ipos  # obter index da pos
            break
    return prado[2][i]


# Modificadores
def eliminar_animal(prado, pos):
    """
    eliminar_animal: prado x posicao --> animal
    Recebe um prado e uma posicao e elimina o animal presente nessa posicao
    """
    i = 0
    for ipos in range(len(prado[3])):
        if posicoes_iguais(pos, prado[3][ipos]):
            i = ipos  # obter index da pos
            break
    prado[2] = prado[2][:i] + prado[2][i + 1:]
    prado[3] = prado[3][:i] + prado[3][i + 1:]
    return prado


def mover_animal(prado, pos1, pos2):
    """
      mover_animal: prado x posicao x posicao --> prado
      Recebe um prado e duas posicoes e
       modifica o prado mudando o animal que estava na primeira posicao para a segunda
    """
    i = 0
    for ipos in range(len(prado[3])):
        if posicoes_iguais(pos1, prado[3][ipos]):
            i = ipos  # obter index da pos
            break
    prado[3] = prado[3][:i] + (pos2,) + prado[3][i + 1:]
    return prado


def inserir_animal(prado, a, pos):
    """
    inserir_animal: prado x animal x posicao --> prado
    Recebe um prado, um animal e uma posicao e
     devolve o prado modificado inserindo o animal na posicao
    """
    prado[2] = prado[2] + (a,)
    prado[3] = prado[3] + (pos,)
    return prado


# Reconhecedores
def eh_prado(arg):
    """
    eh_prado: universal --> booleano
    Recebe um argumento e verifica se este e um prado
    """
    return type(arg) is list and len(arg) == 4 and eh_posicao(arg[0]) \
        and tuple == type(arg[1]) == type(arg[2]) == type(arg[3]) \
        and all(eh_posicao(pos) and 0 < obter_pos_x(pos) < obter_pos_x(arg[0])
                and 0 < obter_pos_y(pos) < obter_pos_y(arg[0])
                for pos in arg[1]) and len(arg[2]) != 0 \
        and all(eh_animal(anim) for anim in arg[2]) and len(arg[3]) == len(arg[2]) \
        and all(eh_posicao(pos) for pos in arg[3]) \
        and all(obter_pos_x(pos) not in (0, obter_tamanho_x(arg) - 1) and
                obter_pos_y(pos) not in (0, obter_tamanho_y(arg) - 1) for pos in arg[1])


def eh_posicao_animal(prado, pos1):
    """
    eh_posicao_animal: prado x posicao --> booleano
    Recebe um prado e uma posicao e verifica se esta um animal na posicao dada
    """
    return any(posicoes_iguais(pos1, pos2) for pos2 in obter_posicao_animais(prado))


def eh_posicao_obstaculo(prado, pos1):
    """
    eh_posicao_obstaculo: prado x posicao --> booleano
    Recebe um prado e uma posicao e
     verifica se esta um obstaculo na posicao dada
    """

    def eh_posicao_montanha(prado1, pos):
        """
        eh_posicao_montanha: prado x posicao --> booleano
        Recebe um prado e uma posicao e
         verifica se esta uma montanha na posicao dada
        """
        return any(obter_pos_x(pos) == x for x in [0, obter_tamanho_x(prado1) - 1]) \
            or any(obter_pos_y(pos) == y for y in [0, obter_tamanho_y(prado1) - 1])

    return any(posicoes_iguais(pos1, pos2) for pos2 in prado[1]) or eh_posicao_montanha(prado, pos1)


def eh_posicao_livre(prado, pos):
    """
    eh_posicao_livre: prado x posicao --> booleano
    Recebe um prado e uma posicao e verifica se a posicao esta livre
    """
    return not (eh_posicao_animal(prado, pos) or eh_posicao_obstaculo(prado, pos))


# Teste
def prados_iguais(p1, p2):
    """
    prados_iguais: prado x prado --> booleano
    Recebe dois prados e verifica se estes prados sao iguais
    """
    return eh_prado(p1) and eh_prado(p2) \
        and posicoes_iguais(cria_posicao(obter_tamanho_x(p1) - 1, obter_tamanho_y(p1) - 1),
                            cria_posicao(obter_tamanho_x(p2) - 1, obter_tamanho_y(p2) - 1)) \
        and ordenar_posicoes(p1[1]) == ordenar_posicoes(p2[1]) \
        and obter_posicao_animais(p1) == obter_posicao_animais(p2) \
        and all(animais_iguais(obter_animal(p1, i), obter_animal(p2, i))
                for i in obter_posicao_animais(p1))


# Transformadores
def prado_para_str(prado):
    """
    prado_para_str: prado --> string
    Recebe um prado e devolve a sua representacao numa cadeia de carateres
    """
    x_sem_pontas, y_sem_pontas = obter_tamanho_x(prado) - 2, obter_tamanho_y(prado) - 2
    linhas = "|" + "." * x_sem_pontas + "|\n"
    base = "+" + "-" * x_sem_pontas + "+\n" +\
           y_sem_pontas * linhas + "+" + "-" * x_sem_pontas + "+"

    for rocha in prado[1]:
        valor = obter_valor_numerico(prado, rocha)
        base = base[:valor + obter_pos_y(rocha)] +\
            "@" + base[valor + 1 + obter_pos_y(rocha):]
    for a in obter_posicao_animais(prado):
        valor = obter_valor_numerico(prado, a)
        base = base[:valor + obter_pos_y(a)] + \
            animal_para_char(obter_animal(prado, a)) + base[valor + 1 + obter_pos_y(a):]
    return base


# Alto nivel
def obter_valor_numerico(prado, pos):
    """
    obter_valor_numerico: prado x pos --> inteiro
    Recebe um prado e uma posicao e devolve o valor numerico da posicao pela ordem de leitura do prado
    """
    return (obter_tamanho_x(prado) * obter_pos_y(pos)) + obter_pos_x(pos)


def obter_movimento(prado, pos_i):
    """
    obter_movimento: prado x posicao --> posicao
    Recebe um prado e devolve a posicao seguinte do animal de acordo com as regras e posicoes disponiveis
    """
    if eh_predador(obter_animal(prado, pos_i)):  # como e predador prioriza as posicoes de presas
        posicoes_possiveis = [newpos for newpos in
                              obter_posicoes_adjacentes(pos_i)
                              if (eh_posicao_animal(prado, newpos)
                                  and eh_presa(obter_animal(prado, newpos)))]
        if posicoes_possiveis:
            return posicoes_possiveis[obter_valor_numerico(prado, pos_i)
                                      % len(posicoes_possiveis)]

    posicoes_possiveis = [newpos for newpos in
                          obter_posicoes_adjacentes(pos_i) if eh_posicao_livre(prado, newpos)]
    if posicoes_possiveis:  # se a lista tiver elementos
        return posicoes_possiveis[obter_valor_numerico(prado, pos_i)
                                  % len(posicoes_possiveis)]
    return pos_i  # nao ha movimentos possiveis entao fica na mesma posicao


# Adicionais
def geracao(prado):
    """
      geracao: prado --> prado
      Recebe um prado e modifica o prado de acordo com uma evolucao de uma geracao completa
      """
    pos_comidos = []
    for pos in obter_posicao_animais(prado):
        a = obter_animal(prado, pos)
        if not any(posicoes_iguais(pos, posicao_comida) for
                   posicao_comida in pos_comidos):  # se a posicao estiver
            # na lista quer dizer que o animal é um predador
            # e vai repetir o movimento portanto salta-se para o proximo animal
            aumenta_fome(a)
            aumenta_idade(a)
            new_pos = obter_movimento(prado, pos)
            if new_pos != pos:  # se o animal nao se mover tambem nao pode reproduzir se nem comer outros
                if eh_posicao_animal(prado, new_pos):
                    eliminar_animal(prado, new_pos)
                    reset_fome(a)
                    pos_comidos += [new_pos]  # guarda a posicao nova do predador
                mover_animal(prado, pos, new_pos)
                if eh_animal_fertil(a):
                    inserir_animal(prado, reproduz_animal(a), pos)
            if eh_animal_faminto(a):
                eliminar_animal(prado, new_pos)
    return prado


def config_para_prado(file1):
    """
    config_para_prado: string --> prado
    Recebe uma cadeia de carateres correspondente ao nome do ficheiro de configuracao da simulacao
    e devolve um prado
    """
    with open(file1, "r") as f:
        args = f.readlines()
    pi = cria_posicao(eval(args[0])[0], eval(args[0])[1])
    rochas = tuple(cria_posicao(pos[0], pos[1])
                   for pos in eval(args[1]))  # cria uma posicao para cada rocha
    animais, pos = (), ()
    for animal in args[2:]:
        animal = eval(animal)
        pos += (cria_posicao(animal[3][0], animal[3][1]),)  # obtem as posicoes dos animais
        animais += (cria_animal(animal[0], animal[1], animal[2]),)  # obtem os animais
    return cria_prado(pi, rochas, animais, pos)


def simula_ecossistema(f, g, v):
    """
    simula_ecossistema: string x inteiro x booleano --> tuplo
    Recebe uma cadeia de carateres correspondente ao nome do ficheiro de configuracao da simulacao, um
    inteiro correspondente as geracoes da simulacao
    e um booleano correspondente ou a um modo verboso ou quiet True ou False,respetivamente.
    Esta representa os prados de cada geracao e as suas presas e predadores
    e devolve um tuplo de presas e predadores da ultima geracao
    """

    def representa_simulacao(prado1, gen, index):
        """
        representa_simulacao  inteiro --> string
        Recebe o numero da geracao e devolve a representacao do prado,presas e predadores de acordo com a geracao
        """
        return "Predadores: " + str(gen[0]) + " vs " \
               + "Presas: " + str(gen[1]) +\
               " (Gen. " + str(index) + ")\n" + prado_para_str(prado1)

    prado = config_para_prado(f)
    ult_gen = (obter_numero_predadores(prado), obter_numero_presas(prado))
    if v:
        for i in range(g + 1):
            if i != 0:  # primeira geracao e igual ao prado
                geracao(prado)
                nova_gen = (obter_numero_predadores(prado), obter_numero_presas(prado))
                if ult_gen != nova_gen:  # se os predadores ou presas mudarem da-se a representacao da nova geracao
                    ult_gen = nova_gen
                    print(representa_simulacao(prado, ult_gen, i))

            else:
                print(representa_simulacao(prado, ult_gen, i))
    else:
        for i in range(g + 1):
            if i != 0:
                geracao(prado)

            else:
                print(representa_simulacao(prado, ult_gen, i))
        ult_gen = (obter_numero_predadores(prado), obter_numero_presas(prado))
        print(representa_simulacao(prado, ult_gen, g))

    return ult_gen
