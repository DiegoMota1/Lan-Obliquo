import math
import pygame
import parametros

class Moto(pygame.sprite.Sprite):
    t = 0
    pulo = False
    movimento = False
    rampa = False
    posx = 0
    posy = 0
    ang = 0
    i = 0
    j = 0
    teste = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load('motinho.png'))

        self.current_sprite = 0
        self.og_image = self.sprites[self.current_sprite]
        self.image = self.og_image

        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.bottomleft = [0, parametros.altura-70]

    def update(self, nom, vel):

        if parametros.dist_rampa - 30 <= self.rect.x < parametros.dist_rampa + parametros.base_rampa:
            self.rampa = True

        if self.rect.x + 35 >= (parametros.dist_rampa + parametros.base_rampa):
            self.pulo = True
            self.rampa = False
            self.rect.y = self.posy - ((vel * (5 / 3)) * (math.sin(math.radians(nom)) * self.t) - ((5 / 90) * 4.9) * (
                    self.t * self.t))
            self.rect.x = self.posx + ((5 / 3) * vel * math.cos(math.radians(nom))) * self.t
        
        if self.rect.x >= parametros.largura:

            self.ang = 0            
            self.image = self.og_image
            self.pulo = False
            self.rampa = False
            self.rect.bottomleft = [0, parametros.altura-70]
            self.movimento = False

        if self.pulo:
            self.t += 1

        elif self.rampa:

            # rotacao
            self.ang = nom            
            self.image = pygame.transform.rotate(self.og_image, self.ang)

            self.rect.x += (5 / 3) * vel * math.cos(math.radians(nom))
            self.rect.y -= (5 / 3) * vel * math.sin(math.radians(nom))

            self.posx = self.rect.x
            self.posy = self.rect.y


        else:
            self.rect.x += (5 / 3) * vel
            self.t = 0
