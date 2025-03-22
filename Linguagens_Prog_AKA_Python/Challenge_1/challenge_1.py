def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# labirinto estatico 10x10
maze = [
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'H', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', 'D', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'E'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', ' ', 'X', 'X', ' ', 'X', ' ', 'X', ' ', 'X'],
    ['X', 'K', 'X', 'X', ' ', ' ', ' ', 'X', ' ', 'X'],
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
]

print_maze(maze)


hero_x = 1
hero_y = 1
has_key = False

# Funcao para verificar proximidade do dragao
def check_dragon(position: list):
    if maze[position[0] + 1][position[1]] == 'D' or maze[position[0] - 1][position[1]] == 'D' :
        print("* * * * * * * YOU DIED! * * * * * * *")
        print("     (Don't touch the dragon! He bites!)")
        exit(1)

# verificar se heroi tem a chave
def check_key(position: list):
    global has_key
    if maze[position[0]][position[1]] == 'K':
        print("You found the key!")
        has_key = True
        maze[position[0]][position[1]] = ' '  # tirar a chave da maze

# verificar se o heroi conseguiu sair e tem a chave para o mesmo
def check_exit(position: list):
    if maze[position[0]][position[1]] == 'E':
        if has_key:
            print("* * * * * * * YOU ESCAPED! * * * * * * *")
            exit(0)
        else:
            print("You forgot the Key! You have now fallen into a trap!")
            print("* * * * * * * YOU DIED! * * * * * * *")
            exit(0) 
            


def mover_hero(direction: str):
    global hero_x, hero_y

    # calcular a nova posicao tendo em conta a direcao que o utilizador inserir
    new_x, new_y = hero_x, hero_y
    if direction == 'w':  # Move para cima
        new_x -= 1
    elif direction == 's':  # Move para baixo
        new_x += 1
    elif direction == 'a':  # Move para a esquerda
        new_y -= 1
    elif direction == 'd':  # Move para a direita
        new_y += 1

    # verificar se bate contra um X
    if maze[new_x][new_y] == 'X':
        print("You can't go through walls!")
        return

   

    



    # verificar se o heroi tem a chave e ou ta no exit ou nao
    check_key([new_x, new_y])
    check_exit([new_x, new_y])

    # verificar proximaded do dragao
    check_dragon([new_x, new_y])
    
     # Mover o heroi -> atualizar a maze
    maze[hero_x][hero_y] = ' '  # Limpar posicao atual do heroi
    hero_x, hero_y = new_x, new_y
    maze[hero_x][hero_y] = 'H'  # Atualizar posicao nova do heroi
    
    # Dar print à maze para o utilizador observar a nova posição do herói
    print_maze(maze)
# Loop do jogo
while True:
    direction = input("Mova o heroi com WASD: ").strip().lower()  # lower para o utilizador nao inserir uppercase versions do WASD e strip para limpar "white space" à volta do char inserido
    mover_hero(direction)