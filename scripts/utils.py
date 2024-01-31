import pygame

BASE_IMAGE_PATH = 'Assets/img/'

def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path)
    """ img.set_colorkey((0,0,0)) """
    return img