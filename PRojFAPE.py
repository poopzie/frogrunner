import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT,
    K_SPACE,
    
)


screen_width = 1000
screen_height = 500

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
            
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > screen_width/2 - 100:
            self.rect.right = screen_width/2 - 100
        if self.rect.top <= 200:
            self.rect.top = 200
        if self.rect.bottom >= screen_height-30:
            self.rect.bottom = screen_height-30
        
pygame.init()

screen = pygame.display.set_mode([screen_width,screen_height])

player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
            
    pressed_keys= pygame.key.get_pressed()
    
    player.update(pressed_keys)
    
    screen.fill((0,0,0))
    
    screen.blit(player.surf, player.rect)

    pygame.display.flip()
    

pygame.quit()