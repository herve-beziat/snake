# build-game.py

import random
import time
import keyboard  # Pour détecter les touches du clavier

# Dimensions de la grille
GRID_SIZE = 20  # Taille 10x10 (modifiable)

# Directions possibles (x, y)
DIRECTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

def create_grid():
    """Crée une grille vide avec des bords optionnels."""
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    # Optionnel : Ajouter des murs (bordure de la grille)
    for i in range(GRID_SIZE):
        grid[0][i] = -1  # Mur haut
        grid[GRID_SIZE - 1][i] = -1  # Mur bas
        grid[i][0] = -1  # Mur gauche
        grid[i][GRID_SIZE - 1] = -1  # Mur droit

    return grid

def place_snake(grid):
    """Place le serpent au centre de la grille."""
    x, y = GRID_SIZE // 2, GRID_SIZE // 2
    grid[x][y] = 1  # Tête du serpent
    return [(x, y)]  # Liste des positions du serpent (tête + corps)

def place_food(grid):
    """Ajoute une pomme à un emplacement aléatoire."""
    while True:
        x, y = random.randint(1, GRID_SIZE - 2), random.randint(1, GRID_SIZE - 2)
        if grid[x][y] == 0:  # Vérifie que la case est vide
            grid[x][y] = 3  # Place une pomme
            break
    return (x, y)

def move_snake(grid, snake, direction):
    """Déplace le serpent dans la direction donnée."""
    head_x, head_y = snake[0]  # Position actuelle de la tête
    dx, dy = DIRECTIONS[direction]  # Déplacement en x et y
    new_x, new_y = head_x + dx, head_y + dy  # Nouvelle position

    # Vérifier si le serpent se cogne contre un mur ou lui-même
    if grid[new_x][new_y] == -1 or (new_x, new_y) in snake:
        print("💀 GAME OVER !")
        return False  # Fin du jeu

    # Vérifier si on mange une pomme
    if grid[new_x][new_y] == 3:
        print("🍏 Miam ! Le serpent grandit !")
        snake.insert(0, (new_x, new_y))  # Ajouter la nouvelle tête (grandit)
        place_food(grid)  # Ajouter une nouvelle pomme
    else:
        snake.insert(0, (new_x, new_y))  # Ajouter la nouvelle tête
        tail_x, tail_y = snake.pop()  # Retirer l'ancienne queue
        grid[tail_x][tail_y] = 0  # Libérer l'ancienne position

    # Mettre à jour la grille
    grid[new_x][new_y] = 1  # Nouvelle tête
    return True  # Continue le jeu

def print_grid(grid):
    """Affiche la grille dans la console."""
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()

# --- Boucle du jeu ---
if __name__ == "__main__":
    grid = create_grid()
    snake = place_snake(grid)
    food = place_food(grid)
    direction = "RIGHT"  # Direction initiale

    running = True
    while running:
        print_grid(grid)  # Afficher la grille
        time.sleep(0.5)  # Pause pour voir le déplacement

        # Détection des touches directionnelles
        if keyboard.is_pressed("up"):
            direction = "UP"
        elif keyboard.is_pressed("down"):
            direction = "DOWN"
        elif keyboard.is_pressed("left"):
            direction = "LEFT"
        elif keyboard.is_pressed("right"):
            direction = "RIGHT"

        # Déplacement du serpent
        running = move_snake(grid, snake, direction)

    print("Fin du jeu !")