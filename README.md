# Grammar Simplifier

Este projeto implementa um algoritmo para simplificar gramáticas formais, removendo produções indesejáveis de acordo com os seguintes passos:

1. **Remover as produções-vazias**  
   Produções que geram a palavra vazia são eliminadas.

2. **Remover as produções-unidade**  
   Produções que ligam uma variável diretamente a outra variável são eliminadas.

3. **Remover as produções inúteis**  
   Produções que não contribuem para a geração de palavras da linguagem são eliminadas.

---

## 📂 Formato dos Arquivos

### Arquivo de Entrada
O arquivo de entrada deve seguir o seguinte formato:

1. **Linha 1:** Variáveis separadas por espaço  
    Exemplo: `S A B C D`
2. **Linha 2:** Símbolo inicial  
    Exemplo: `S`
3. **Linhas 3 em diante:** Regras de produção no formato `variável -> símbolos`  
    - Símbolos são variáveis ou terminais.  
    - `h` representa a palavra vazia.  
    Exemplo:  
    ```text
    S -> a
    S -> Aa
    A -> a
    A -> Aa
    A -> B
    B -> h
    ```
### Arquivo de Saída
O arquivo de saída deve manter o mesmo formato do arquivo de entrada, mas com a gramática já simplificada. Exemplo:

**Entrada:**
```text
S A B C D
S
S -> a
S -> Aa
A -> a
A -> Aa
A -> B
B -> h
```

**Saída (Gramática Limpa):**
```text
S A
S
S -> a
S -> Aa
A -> a
```

## 🚀 Como Usar
1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/Grammar-Simplifier.git
    cd Grammar-Simplifier
    ```
2. Certifique-se de que tem o Python instalado em sua máquina.
3. Execute o programa passando o arquivo de entrada e o nome para o arquivo de saída quando necessário (opte sempre por inseri-los nas pastas input e output):
