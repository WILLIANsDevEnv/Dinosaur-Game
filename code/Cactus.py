import pygame
import random
from code.Const import game_speed

class Cactus(pygame.sprite.Sprite):
    """Classe que representa o Cacto (obstáculo)."""
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprites = []
        try:
            for i in range(1, 7):
                current_sprite = pygame.transform.scale(
                    pygame.image.load(f"assets/cacti/cactus{i}.png"), (100, 100))
                self.sprites.append(current_sprite)
        except pygame.error:
            print("Erro ao carregar imagem do Cacto")
        
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        """Move o cacto para a esquerda."""
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
