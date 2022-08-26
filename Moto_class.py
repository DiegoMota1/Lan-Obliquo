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
        # self.image = pygame.transform.scale(self.image, (300, 150))  # 50 px = 1m
        self.rect.bottomleft = [0, parametros.altura-70]

    def update(self, nom, vel):

        if parametros.dist_rampa - 30 <= self.rect.x < parametros.dist_rampa + parametros.base_rampa:
            self.rampa = True
            # self.image = pygame.transform.rotate(self.image, nom)

        if self.rect.x + 35 >= (parametros.dist_rampa + parametros.base_rampa):
            self.pulo = True
            self.rampa = False
            self.rect.y = self.posy - ((vel * (5 / 3)) * (math.sin(math.radians(nom)) * self.t) - ((5 / 90) * 4.9) * (
                    self.t * self.t))
            self.rect.x = self.posx + ((5 / 3) * vel * math.cos(math.radians(nom))) * self.t
        # - 100 * math.sin(nom)   + 100 * math.cos(nom)

        if self.rect.x >= parametros.largura or self.rect.y >= parametros.altura-70:

            self.ang = 0            
            self.image = self.og_image

            self.pulo = False
            self.rampa = False
            self.rect.bottomleft = [0, parametros.altura-70]
            self.movimento = False

            # self.image = pygame.transform.rotate(self.image, 0)

        if self.pulo:
            self.t += 1



            # rotacao
            self.ang += -2
            self.image = pygame.transform.rotate(self.og_image, self.ang)
            self.rect = self.image.get_rect(center=self.rect.center)

            self.teste = True



        elif self.rampa:

            # rotacao
            self.ang = nom            
            self.image = pygame.transform.rotate(self.og_image, self.ang)
            self.rect = self.image.get_rect(center=self.rect.center)

            self.rect.x += (5 / 3) * vel * math.cos(math.radians(nom))
            self.rect.y -= (5 / 3) * vel * math.sin(math.radians(nom))
            self.posx = self.rect.x
            self.posy = self.rect.y




        else:
            self.rect.x += (5 / 3) * vel
            self.t = 0
            self.teste = False