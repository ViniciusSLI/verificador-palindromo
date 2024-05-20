def is_palindrome(word):
    # Converte a palavra para minúsculas para ignorar a diferença entre maiúsculas e minúsculas
    word = word.lower()
    
    # Remove espaços em branco da palavra
    word = word.replace(" ", "")
    
    # Verifica se a palavra é igual à sua inversa
    if word == word[::-1]:
        return True
    else:
        return False

def main():
    # Solicita ao usuário que insira uma palavra
    word = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    
    # Limita o número de caracteres permitidos
    if len(word) > 50:
        print("Por favor, digite uma palavra ou frase com menos de 50 caracteres.")
        return
    
    # Verifica se a palavra é um palíndromo
    if is_palindrome(word):
        print("Sim, é um palíndromo!")
    else:
        print("Não é um palíndromo.")

if __name__ == "__main__":
    main()
