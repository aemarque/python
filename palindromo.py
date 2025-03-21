#Palindromo
def ehpalindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    invertido = palavra[::-1]
     # Remove espaços em branco e converte para minúsculas
    palavra = palavra.lower().replace(" ", "")
    # Compara a palavra original com a palavra invertida
    if palavra == invertido:
        return True
    else:
        return False

palavra = input("Digite uma palavra ou frase: ")
if ehpalindromo(palavra):
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo!")