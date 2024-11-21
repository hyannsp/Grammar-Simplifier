def remove_unitary(matrix):
    variables = matrix[0]  # Variáveis
    start_symbol = matrix[1][0]  # Símbolo inicial
    productions = matrix[2:]  # Produções

    new_productions = []
    """
        1. Encontrar os pares Unidade
    """
    # Adicionando pares unidades comum
    unitary_pairs = set()
    for prod in productions:
        if prod[1] in variables:
            #print(f"Par unidade em: {prod}")
            unitary_pairs.add(tuple(prod))
            continue
        new_productions.append(prod) # Salvar os não pares unitários para o passo 2

    # Adicionando pares unidade por indução
    iterator = unitary_pairs.copy() # necessário para mudar o set original
    for x, y in iterator:
        for a, b in iterator:
            if y == a and x != b:  # Verifica a conexão e evita reflexivos
                new_pair = (x, b)
                #print(f"Indução encontrada: {new_pair}")
                unitary_pairs.add(new_pair)
    print(f"Pares unidades encontrados: {unitary_pairs}")

    """
        2. Adicionar à nova produção os pares não unitários
        ( já feito durante a iteração para encontrar os pares unitários, salvo em new_productions)

        3. Introduzir as derivações que substituem os pares unidade
    """
    iterator = new_productions.copy() # necessário para mudar o set original
    for x, y in unitary_pairs:
        for a, b in iterator:
            # Caso S->A e A->bb , logo S->bb
            if y == a and [x , b] not in new_productions:
                new_productions.append([x, b])

    """
        4: Retornar nova gramática
    """
    return [variables, [start_symbol]] + new_productions