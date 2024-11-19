import os

def save_matrix_to_txt(matrix, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w') as file:
        for row in matrix:
            line = ' '.join(map(str, row))
            file.write(line + '\n')

# Função para ler o arquivo e transformar em uma matriz
def capture_matrix():
    path = input(f"Insira o caminho do arquivo de texto contendo a gramatica a ser simplificada: \n")
    text_matrix = []

    try:
        # Ler e transformar o arquivo de texto em uma matriz com tratamento de erros
        with open(path, 'r') as file:
            for linha in file:
                text_matrix.append(linha.strip().split(" "))
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho especificado: {path}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

    return text_matrix

# Função para salvar o arquivo
def save_file(type, matrix):
    name = input("Insira o nome do arquivo txt que será retornado: ")
    file_path = f"./output/{type}/{name}.txt"
    save_matrix_to_txt(matrix, file_path)
    print(f"Seu arquivo foi salvo em: {file_path}")
    return