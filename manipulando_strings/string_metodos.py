# Criar o arquivo string_metodos.py

nome = "GUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = " Olá mundo!   "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

menu = "Java"
print("###" + menu + "###")
# Passamos o número de caracteres para centralizar
print(menu.center(14))
print(menu.center(14, "#"))
print("J-a-v-a")
print("-".join(menu))

# Faz a mesma coisa do .join()
for letra in menu:
    print(letra, end="-")
print()
