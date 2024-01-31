import pygame
import sys

from scripts.utils import load_image
from scripts.entities import PhysicsEntity 



class Game:
    def __init__(self):
        pygame.init()
        print('Game started...')

        pygame.display.set_caption('BOT game')
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        
        self.movement = [False, False]
        self.assets = {
            'player': load_image('robot.png')
        }
        self.player = PhysicsEntity(self, 'player', (200, 400), (8, 15))
        
        
    def run(self):
        fps = 60

        while True:
            self.screen.fill((14,219,248))

            self.player.update(self.movement[1] - self.movement[0])
            self.player.render(self.screen)
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(fps)
            
            
Game().run()