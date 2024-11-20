"""
Ordem para simplificar a gramática: 
1. Remover Lambda
2. Remover Unitárias
3. Remover inuteis
"""
from functions import files_handling, remove_lambda , remove_unitary, remove_useless

def main():
    print("- Simplificar Gramaticas -")

    # Captura o texto do caminho inserido pelo usuário e o transforma em uma matriz
    matrix = files_handling.capture_matrix()
    if matrix == None:
        pass
    print("Gramática Capturada: ")
    print("\n")
    for i in matrix:
        print(i)
    print("\n")

    # Remover produções vazias
    print("Removendo producoes vazias...")
    without_lambda = remove_lambda.remove_lambda(matrix)
    print("\n")
    for i in without_lambda:
        print(i)
    print("\n")

    # Remover produções Unitárias
    print("Removendo producoes unitarias...")
    without_unitary = remove_unitary.remove_unitary(without_lambda)
    print("\n")
    for i in without_unitary:
        print(i)
    print("\n")
    
    # Remover produções Inúteis
    print("Removendo producoes inuteis...")
    without_useless = remove_useless.remove_useless(without_unitary)

    # Salvar arquivo em formato como de entrada
    #files_handling.save_file(without_useless)
    

    return

if __name__ == "__main__":
    main()