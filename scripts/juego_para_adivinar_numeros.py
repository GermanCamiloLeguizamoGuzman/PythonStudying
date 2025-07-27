import random

# Configuración del juego
numero_de_digitos = 3
maximo_numero_de_intentos = 10

def main():
    print(f'''Este programa fue desarrollado por Camilo para practicar Python.
Es el segundo reto subido a GitHub.

He pensado un número de {numero_de_digitos} dígitos sin dígitos repetidos.
Intenta adivinar qué número es. Debes seguir mis pistas:

1. Cuando diga "Conito" significa que un dígito es correcto, pero está en la posición errónea.
2. Cuando diga "Yodita" significa que un dígito es correcto y está en la posición correcta.
3. Cuando diga "Cornelito" significa que ningún dígito es correcto.

Por ejemplo, si el número secreto es 346 y tú escribes 243, te diré "Conito" y "Yodita".
''')

    while True:
        numero_secreto = generar_numero_secreto()
        print('He pensado un número.')
        print(f'Tienes {maximo_numero_de_intentos} intentos para adivinarlo.')

        intento_num = 1
        while intento_num <= maximo_numero_de_intentos:
            guess = ''
            while len(guess) != numero_de_digitos or not guess.isdecimal():
                print(f'Intento #{intento_num}:')
                guess = input('> ')

            pistas = obtener_pistas(guess, numero_secreto)
            print(pistas)
            intento_num += 1

            if guess == numero_secreto:
                break

            if intento_num > maximo_numero_de_intentos:
                print('Has agotado todos tus intentos.')
                print(f'El número secreto era: {numero_secreto}')

        print('¿Quieres jugar de nuevo? (sí o no)')
        if not input('> ').lower().startswith('s'):
            break

    print('¡Gracias por jugar!')

def generar_numero_secreto() -> str:
    """Genera un número aleatorio sin dígitos repetidos."""
    digitos = list('0123456789')
    random.shuffle(digitos)
    secreto = ''.join(digitos[:numero_de_digitos])
    return secreto

def obtener_pistas(conjetura: str, secreto: str) -> str:
    """Genera las pistas que se dan al jugador."""
    if conjetura == secreto:
        return '¡Lo adivinaste!'

    pistas = []

    for i in range(len(conjetura)):
        if conjetura[i] == secreto[i]:
            pistas.append('Yodita')  # Dígito correcto y en la posición correcta
        elif conjetura[i] in secreto:
            pistas.append('Conito')  # Dígito correcto pero en posición incorrecta

    if not pistas:
        return 'Cornelito'  # Ningún dígito es correcto
    else:
        pistas.sort()
        return ' '.join(pistas)

# Llamada principal al juego
if __name__ == '__main__':
    main()
