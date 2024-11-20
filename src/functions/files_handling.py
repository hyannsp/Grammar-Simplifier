import os

# Validar se a gramática passada esta no formato correto
def validate_grammar(matrix):
    if not matrix or len(matrix) < 3:
        print("Erro: A gramática fornecida é inválida. Ela deve conter pelo menos variáveis, símbolo inicial e regras.")
        return False
    
    variables = set(matrix[0])
    initial_symbol = matrix[1][0]
    if initial_symbol not in variables:
        print("Erro: O símbolo inicial não está listado entre as variáveis.")
        return False

    return True

def capture_matrix():
    path = input("Insira o caminho do arquivo de texto contendo a gramática a ser simplificada: \n")
    text_matrix = []

    try:
        with open(path, 'r') as file:
            for linha in file:
                stripped_line = linha.strip()
                if stripped_line:  # Ignorar linhas vazias
                    text_matrix.append(stripped_line.split(" "))
        
        if not text_matrix:
            print(f"Erro: O arquivo {path} está vazio.")
            return None

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho especificado: {path}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None
    
    if (error := validate_grammar(text_matrix)) != True:
        print(error)
        return None
    
    return text_matrix

def save_matrix_to_txt(matrix, file_path):
    if not matrix:
        print("Erro: A matriz fornecida está vazia. Nada foi salvo.")
        return
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    try:
        with open(file_path, 'w') as file:
            for row in matrix:
                line = ' '.join(map(str, row))
                file.write(line + '\n')
        print(f"Arquivo salvo com sucesso em: {file_path}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função para salvar o arquivo
def save_file(matrix):
    if not matrix:
        print("Erro: A matriz fornecida está vazia. Nada foi salvo.")
        return
    
    while True:

        name = input("Insira o nome do arquivo txt que será retornado (sem extensão): ").strip()
        if not name or any(char in name for char in r'\/:*?"<>|'):
            print("Erro: Nome inválido. Evite caracteres especiais.")
            continue
        
        break

    file_path = f"./examples/output/{name}.txt"
    save_matrix_to_txt(matrix, file_path)