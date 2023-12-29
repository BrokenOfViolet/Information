import pygame
import sys

class Rocket():
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,600))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        
        self.rocket = pygame.image.load("/Users/mac/vscode/Python/Alien_Invasion/images/ship(1).png")
        self.rocket_rect = self.rocket.get_rect()
        
        pygame.display.set_caption("Rocket Adventure")
        
    def run_game(self):       
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._screen_update()
            self.rocket_position()
        
            self.clock.tick(60)
    
    def rocket_position(self):
        self.rocket_rect.midleft = self.screen_rect.midleft
        
    def _check_keydown(self, event):
        if event.type == pygame.K_UP:
            self.rocket_up_moving = True
        if event.type == pygame.K_DOWN:
            self.rocket_down_moving = True
        if event.type == pygame.K_left:
            self.rocket_ 

    def _check_keyup(self, event):
        if event.type == pygame.K_UP():
            pass
    
    def _screen_update(self):
        self.screen.fill((255,255,255))        
        self.screen.blit(self.rocket, self.rocket_rect)
        pygame.display.flip()


    
    

if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()
