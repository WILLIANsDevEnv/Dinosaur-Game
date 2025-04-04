import pygame

class Cloud(pygame.sprite.Sprite):
    """Classe que representa a Nuvem."""
    
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self):
        """Move a nuvem para a esquerda."""
        self.rect.x -= 1
