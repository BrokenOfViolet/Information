import pygame
import sys

class Rocket():
    def __init__(self):
        self.screen = pygame.display.set_mode((1000,600))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        
        self.rocket = pygame.image.load("/Users/mac/vscode/Python/Alien_Invasion/images/ship(1).png")
        self.rocket_rect = self.rocket.get_rect()
        
        self.rocket_rect.midleft = self.screen_rect.midleft
        
        self.rocket_down_moving = False
        self.rocket_up_moving = False
        self.rocket_left_moving = False
        self.rocket_right_moving = False
        
        self.rocket_speed = 3.0
        
        pygame.display.set_caption("Rocket Adventure")
        
    def run_game(self):       
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_keydown(event)
                if event.type == pygame.KEYUP:
                    self._check_keyup(event)
            
            self._check_collision()
            self._screen_update()
        
            self.clock.tick(60)
    
    def rocket_move(self):
        if self.rocket_up_moving:
            self.rocket_rect.y -= self.rocket_speed
        if self.rocket_down_moving:
            self.rocket_rect.y += self.rocket_speed
        if self.rocket_left_moving:
            self.rocket_rect.x -= self.rocket_speed
        if self.rocket_right_moving:
            self.rocket_rect.x += self.rocket_speed
        
    def _check_keydown(self, event):
        if event.type == pygame.K_UP:
            self.rocket_up_moving = True
        if event.type == pygame.K_DOWN:
            self.rocket_down_moving = True
        if event.type == pygame.K_LEFT:
            self.rocket_left_moving = True
        if event.type == pygame.K_RIGHT:
            self.rocket_right_moving = True

    def _check_keyup(self, event):
        if event.type == pygame.K_UP:
            self.rocket_up_moving = False
        if event.type == pygame.K_DOWN:
            self.rocket_down_moving = False
        if event.type == pygame.K_LEFT:
            self.rocket_left_moving = False
        if event.type == pygame.K_RIGHT:
            self.rocket_right_moving = False           
    
    def _check_collision(self):
        if (0 <= self.rocket_rect.x <= self.screen_rect.width) and (0 <= self.rocket_rect.y <= self.screen_rect.height):
            self.rocket_move()
        
        
    def _screen_update(self):
        self.screen.fill((255,255,255))        
        self.screen.blit(self.rocket, self.rocket_rect)
        pygame.display.flip()


    
    

if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()
