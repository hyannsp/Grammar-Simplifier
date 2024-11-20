def remove_lambda(matrix):
    variables = matrix[0]  # Variáveis
    start_symbol = matrix[1][0]  # Símbolo inicial
    productions = matrix[2:]  # Produções
    
    """
        Passo 1: Encontrar variáveis anuláveis
    """
    nullable = set()  # Armazena variáveis anuláveis
    
    # Adicionar variáveis diretamente anuláveis
    for prod in productions:
        if len(prod) == 2 and prod[1] == 'h':  # Forma: A → h
            nullable.add(prod[0])
    
    # Encontrar variáveis indiretamente anuláveis
    changed = True
    while changed:
        changed = False
        for prod in productions:
            if prod[0] not in nullable:
                # Verifica se todos os símbolos do lado direito são anuláveis
                if all(symbol in nullable or symbol == 'h' for symbol in prod[1:]):
                    nullable.add(prod[0])
                    changed = True

    if not nullable:
        print("Não encontradas produções vazias!")
        return matrix
    print("Variáveis anuláveis: ", nullable)

    """
        Passo 2: Substituir variáveis anuláveis nas produções
    """
    new_productions = set()  # Usar conjunto para evitar duplicatas

    for prod in productions:
        # Ignorar produções que são apenas λ
        if prod[1] == 'h':
            continue

        # Adiciona a produção original
        new_productions.add(tuple(prod))

        # Verificar e criar novas produções removendo cada instância de uma variável anulável
        for j in range(1, len(prod)):  # Começar em 1 para ignorar a variável à esquerda
            symbol = prod[j]
            print(f"Symbol: {symbol}")
            
            # Encontrar todas as letras anuláveis dentro do símbolo
            nullable_in_symbol = [letter for letter in symbol if letter in nullable]
            
            # Gerar combinações de remoção de símbolos anuláveis
            for i in range(1 << len(nullable_in_symbol)):  # Para cada combinação possível de letras anuláveis a serem removidas
                new_symbol = symbol  # Começa com o símbolo original
                for bit, letter in enumerate(nullable_in_symbol):
                    if i & (1 << bit):  # Se o bit está "1", remova esse caractere
                        new_symbol = new_symbol.replace(letter, "", 1)
                
                # Se a nova produção não for vazia, adicione ao conjunto de produções
                if len(new_symbol) > 0:
                    new_productions.add(tuple([prod[0], new_symbol]))



    """
        Passo 3: Retornar nova gramática
    """
    return [variables, [start_symbol]] + [list(prod) for prod in new_productions]