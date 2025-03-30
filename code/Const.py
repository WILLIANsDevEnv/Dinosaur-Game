import pygame
from code.Dino import Dino

pygame.init()

# Configurações do jogo
game_speed = 5
jump_count = 10
player_score = 0
game_over = False
obstacle_timer = 0
obstacle_spawn = False
obstacle_cooldown = 1000

# Carregando imagens
try:
    ground = pygame.image.load("assets/ground.png")
    ground = pygame.transform.scale(ground, (1280, 20))
except pygame.error:
    print("Erro ao carregar imagem do chão")

ground_x = 0
ground_rect = ground.get_rect(center=(640, 400))

try:
    cloud = pygame.image.load("assets/cloud.png")
    cloud = pygame.transform.scale(cloud, (200, 80))
except pygame.error:
    print("Erro ao carregar imagem da nuvem")

# Grupos de sprites
cloud_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()
dino_group = pygame.sprite.GroupSingle()
ptero_group = pygame.sprite.Group()

# Criando o objeto dinossauro
dinosaur = Dino(50, 360)
dino_group.add(dinosaur)

# Eventos personalizados
CLOUD_EVENT = pygame.USEREVENT
pygame.time.set_timer(CLOUD_EVENT, 3000)