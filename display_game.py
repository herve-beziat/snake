import pygame
import time
import random
from build_game import create_grid, place_snake, place_food, move_snake, DIRECTIONS  # On importe les fonctions du jeu

# Dimensions de la grille et fenêtre
GRID_SIZE = 20  
CELL_SIZE = 40  # Chaque case fait 40 pixels
WINDOW_SIZE = GRID_SIZE * CELL_SIZE  # Taille de la fenêtre

# Couleurs
WHITE = (255, 255, 255)  # Fond
BLACK = (0, 0, 0)        # Bordures de grille
GREEN = (0, 200, 0)      # Serpent
RED = (200, 0, 0)        # Pomme
GRAY = (100, 100, 100)   # Murs

# Initialisation de Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Snake Game")

# Fonction pour dessiner la grille
def draw_grid(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            x, y = col * CELL_SIZE, row * CELL_SIZE

            if grid[row][col] == -1:  # Murs
                pygame.draw.rect(screen, GRAY, (x, y, CELL_SIZE, CELL_SIZE))
            elif grid[row][col] == 1:  # Tête du serpent
                pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
            elif grid[row][col] == 2:  # Corps du serpent
                pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))
            elif grid[row][col] == 3:  # Pomme
                pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))
            else:  # Cases vides
                pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))

            # Dessiner les contours de la grille
            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

# Fonction principale du jeu
def main():
    grid = create_grid()
    snake = place_snake(grid)
    food = place_food(grid)
    direction = "RIGHT"

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)  # Efface l'écran
        draw_grid(grid)  # Affiche la grille
        pygame.display.flip()  # Met à jour l'affichage

        # Détection des événements clavier
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "UP"
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    direction = "RIGHT"

        # Déplacement du serpent
        running = move_snake(grid, snake, direction)

        # Vitesse du jeu
        clock.tick(5)  # 5 FPS (modifiable pour accélérer le serpent)

    pygame.quit()

# Lancer le jeu si ce fichier est exécuté
if __name__ == "__main__":
    main()
