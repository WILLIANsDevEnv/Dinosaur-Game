import pygame
import random
from code.Const import game_speed

class Ptero(pygame.sprite.Sprite):
    """Classe que representa o Ptero."""
    
    def __init__(self):
        super().__init__()
        self.x_pos = 1300
        self.y_pos = random.choice([280, 295, 350])
        self.sprites = []
        try:
            self.sprites.append(
                pygame.transform.scale(
                    pygame.image.load("assets/Ptero1.png"), (84, 62)))
            self.sprites.append(
                pygame.transform.scale(
                    pygame.image.load("assets/Ptero2.png"), (84, 62)))
        except pygame.error:
            print("Erro ao carregar imagens do Ptero")
        
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        """Atualiza a posição do Ptero"""
        self.animate()
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        if self.rect.right < 0:
            self.kill()

    def animate(self):
        """Atualiza animação do Ptero"""
        self.current_image += 0.025
        if self.current_image >= 2:
            self.current_image = 0
        self.image = self.sprites[int(self.current_image)]
