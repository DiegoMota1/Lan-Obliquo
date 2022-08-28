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
        self.sprites.append(pygame.image.load('motinho-alt.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.bottomleft = [0, parametros.altura-70]

    def update(self, nom, vel, dis):

        #animacao
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        if vel > 0 and self.pulo == False:
            self.image = self.sprites[self.current_sprite]
            self.image = pygame.transform.rotate(self.image, self.ang)

        #ramp
        if parametros.dist_rampa - 30 <= self.rect.x < parametros.dist_rampa + parametros.base_rampa:
            self.rampa = True

        #pos
        if self.rect.x + 35 >= (parametros.dist_rampa + parametros.base_rampa):
            self.pulo = True
            self.rampa = False

            self.rect.y = self.posy - ((vel * (5 / 3)) * (math.sin(math.radians(nom)) * self.t) - ((5 / 90) * 4.9) * (
                    self.t * self.t))

            self.rect.x = self.posx + ((5 / 3) * vel * math.cos(math.radians(nom))) * self.t

            #colisao com o "chao"
            if self.rect.y > parametros.altura-135:
                if self.rect.x > dis:
                    self.rect.y = parametros.altura-135
                    self.ang = 0
                    self.image = self.sprites[self.current_sprite]
                    self.image = pygame.transform.rotate(self.image, self.ang)


        #fim da tela
        if self.rect.x >= parametros.largura or self.rect.y >= parametros.altura-50:
            self.ang = 0            
            self.pulo = False
            self.rampa = False
            self.rect.bottomleft = [0, parametros.altura-70]
            self.movimento = False

        #estado
        if self.pulo:
            self.t += 1

        elif self.rampa:
            self.ang = nom            

            self.rect.x += (5 / 3) * vel * math.cos(math.radians(nom))
            self.rect.y -= (5 / 3) * vel * math.sin(math.radians(nom))

            self.posx = self.rect.x
            self.posy = self.rect.y

        else:
            self.rect.x += (5 / 3) * vel
            self.t = 0



