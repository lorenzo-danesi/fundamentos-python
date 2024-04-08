texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
# exibe os valores entre 0 e 51 em intervalos de 5 (múltiplos)
for numero in range(0, 51, 5):
    print(numero, end=" ")