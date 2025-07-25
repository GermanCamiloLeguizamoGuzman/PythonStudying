# juego_de_dados.py - Acá empieza mi proyecto del 25 de julio de 2025
import random

# Loop
choice = input('¿Lanzamos el dado? (y/n): ').lower()

if choice == 'y':
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f'Has obtenido {dado1} y {dado2}')
elif choice == 'n':
    print('¡Gracias por jugar!')
else:
    print('¡Elección inválida!')
