from string import ascii_letters, digits
from random import choice, randrange, shuffle

# Coletando os caracteres
characters_special = '!@%$#'
alphanumeric = digits
alphabet = ascii_letters

def forming(Finishing):
    # Finalizando a senha
    
    generated = ''
    for i in Finishing:
        generated += i  # Adicionando cada caractere à senha gerada
    return generated

def shuffling(pure):
    # Misturando os caracteres para uma dificuldade maior
    listing = []
    for character in pure:
        listing.append(character)  # Adicionando cada caractere à lista
    shuffle(listing)  # Embaralhando a lista de caracteres
    return listing

def building():  
    # Construindo a base da senha
    senha = ''
    for i in range(randrange(8, 12)):
        senha += choice(alphanumeric)  # Adicionando caracteres alfanuméricos à senha
    for i in range(randrange(2, 3)):
        senha += choice(alphabet)  # Adicionando letras à senha
    for i in range(randrange(1, 2)):
        senha += choice(characters_special)  # Adicionando caracteres especiais à senha
    return senha