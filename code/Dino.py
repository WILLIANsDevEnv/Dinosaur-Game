import pygame

class Dino(pygame.sprite.Sprite):
    """Classe que representa o dinossauro no jogo."""
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.running_sprites = []
        self.ducking_sprites = []

        # Carregando imagens do dinossauro
        try:
            self.running_sprites.append(pygame.transform.scale(
                pygame.image.load("assets/Dino1.png"), (80, 100)))
            self.running_sprites.append(pygame.transform.scale(
                pygame.image.load("assets/Dino2.png"), (80, 100)))
            self.ducking_sprites.append(pygame.transform.scale(
                pygame.image.load("assets/DinoDucking1.png"), (110, 60)))
            self.ducking_sprites.append(pygame.transform.scale(
                pygame.image.load("assets/DinoDucking2.png"), (110, 60)))
        except pygame.error:
            print("Erro ao carregar imagens do Dino")
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.velocity = 0.02
        self.gravity = 3.3
        self.ducking = False

    def jump(self):
        """Faz o dinossauro pular."""
        try:
            jump_sfx = pygame.mixer.Sound("assets/sfx/jump.mp3")
            jump_sfx.play()
        except pygame.error:
            print("Erro ao carregar som de pulo")
        
        if self.rect.centery >= 360:
            while self.rect.centery - self.velocity > 40:
                self.rect.centery -= 1

    def duck(self):
        self.ducking = True
        self.rect.centery = 380

    def unduck(self):
        self.ducking = False
        self.rect.centery = 360

    def apply_gravity(self):
        """Aplica a gravidade ao dinossauro."""
        if self.rect.centery < 360:
            self.rect.centery += self.gravity

    def update(self):
        """Atualiza o estado do dinossauro."""
        self.animate()
        self.apply_gravity()

    def animate(self):
        """Troca entre frames de animação."""
        self.current_image += 0.05
        if self.current_image >= 2:
            self.current_image = 0

        if self.ducking:
            self.image = self.ducking_sprites[int(self.current_image)]
        else:
            self.image = self.running_sprites[int(self.current_image)]
