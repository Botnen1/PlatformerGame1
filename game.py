import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        print('Game started...')

        pygame.display.set_caption('BOT game')
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        
        self.img = pygame.image.load('assets/img/robot.png')
        """ self.img.set_colorkey((0,0,0)) """ # if you want to remove the black background
        self.img_pos = [200, 400]
        self.movement = [False, False]
        
        self.collision_area = pygame.Rect(50,50,300,50)
        
        
    def run(self):
        fps = 60

        while True:
            self.screen.fill((14,219,248))

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0,100,255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0,50,155), self.collision_area)

            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.screen.blit(self.img, (self.img_pos))
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(fps)
            
            
Game().run()