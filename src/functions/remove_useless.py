import re

def remove_useless(matrix):
    variables = matrix[0]  # Variáveis
    start_symbol = matrix[1][0]  # Símbolo inicial
    productions = matrix[2:]  # Produções

    
    """
        1. Verificar produções alcançaveis a partir da variável de inicio 'start_symbol'
    """

    reached_variables = set(start_symbol[0]) # por padrão a variável inicial deve permanecer
    for variable in variables:
        for prod in productions:
            if variable in prod[1]:
                reached_variables.add(variable)
                continue
            
    print("Variáveis alcançáveis: `{reached_variables}")

    """
        2. Verificar se existem produções com cadeias terminais que geram loops A->aA e não inseri-las nas novas produções  
    """
    new_productions = []
    useless = set()
    for prod in productions:
        # Remover recursões diretas A->aA
        if prod[0] in prod[1] or prod[0] not in reached_variables:
            useless.add(tuple(prod))
            continue

        new_productions.append(prod)
    
    print(f"Produções Removidas: {useless}")
    """
        3. Retornar nova matriz 
    """

    return [variables, [start_symbol]] + new_productions