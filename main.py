import pygame
import math
import Moto_class
import parametros
import Fontes
from pygame.locals import *
from sys import exit
import os

pygame.init()

# Tudo sobre .a tela
tela = pygame.display.set_mode((parametros.largura, parametros.altura), pygame.RESIZABLE)
pygame.display.set_caption('movimento obliquo')
fps = pygame.time.Clock()
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
# Tela acaba aqui


angulo_temp = 30
user_text_ang = 30
velocidade_temp = 0
user_text_vel = 0
distancia_temp = 10
user_text_dist = 10
color_angulo = (120, 0, 0)
color_velocidade = (0, 120, 0)
color_distancia = (0, 0, 120)
angulo = 30
velocidade = 0
distancia = 10

active_angulo = False
active_velocidade = False
active_distancia = False
entrada = False

sprites = pygame.sprite.Group()
Moto = Moto_class.Moto()
sprites.add(Moto)


def Tela():
    tela.fill((0, 0, 0))
    fps.tick(30)
    # pygame.draw.circle(tela, (255, 0, 0), (Moto.rect.x, Moto.rect.y), 0.5)


def Rampa(angulo):
    pygame.draw.line(tela, (255, 0, 0), (0, parametros.altura-70), (parametros.largura, parametros.altura-70), 5)
    angulo = math.radians(angulo)
    parametros.base_rampa = 100 * math.cos(angulo)
    parametros.altura_rampa = 100 * math.sin(angulo)
    pygame.draw.line(tela, (200, 200, 200), (0, parametros.altura-70), (parametros.dist_rampa + parametros.base_rampa, parametros.altura-70), 20)
    pygame.draw.line(tela, (200, 200, 200), (parametros.dist_rampa, parametros.altura-70),(parametros.dist_rampa + parametros.base_rampa, parametros.altura-70 - parametros.altura_rampa),
                     20)
    pygame.draw.line(tela, (200, 200, 200), (distancia_user, parametros.altura-70), (parametros.largura, parametros.altura-70), 20)


def Entrada_angulo():
    title = Fontes.tiny_font.render(str("Ângulo da rampa (graus)"), True, (255, 255, 255))
    tela.blit(title, (Fontes.input_rect_angulo.x - 12, Fontes.input_rect_angulo.y - 20))

    pygame.draw.rect(tela, color_angulo, Fontes.input_rect_angulo)
    angulo_temp = Fontes.base_font.render(str(user_text_ang), True, (255, 255, 255))

    tela.blit(angulo_temp, (Fontes.input_rect_angulo.x + 10, Fontes.input_rect_angulo.y + 5))
    Fontes.input_rect_angulo.w = max(100, angulo_temp.get_width() + 10)

    if user_text_ang != '':

        return int(user_text_ang)
    else:
        return 0


def Entrada_velocidade():
    title = Fontes.tiny_font.render(str("Velocidade (m/s)"), True, (255, 255, 255))
    tela.blit(title, (Fontes.input_rect_velocidade.x + 5, Fontes.input_rect_velocidade.y - 20))

    pygame.draw.rect(tela, color_velocidade, Fontes.input_rect_velocidade)
    velocidade_temp = Fontes.base_font.render(str(user_text_vel), True, (255, 255, 255))
    tela.blit(velocidade_temp, (Fontes.input_rect_velocidade.x + 10, Fontes.input_rect_velocidade.y + 5))
    Fontes.input_rect_velocidade.w = max(100, velocidade_temp.get_width() + 10)

    if user_text_vel != '':

        return int(user_text_vel)
    else:
        return 0


def Entrada_distancia():
    title = Fontes.tiny_font.render(str("Distância (m)"), True, (255, 255, 255))
    tela.blit(title, (Fontes.input_rect_distancia.x + 15, Fontes.input_rect_distancia.y - 20))

    pygame.draw.rect(tela, color_distancia, Fontes.input_rect_distancia)
    distancia_temp = Fontes.base_font.render(str(user_text_dist), True, (255, 255, 255))
    tela.blit(distancia_temp, (Fontes.input_rect_distancia.x + 10, Fontes.input_rect_distancia.y + 5))
    Fontes.input_rect_distancia.w = max(100, distancia_temp.get_width() + 10)

    if user_text_dist != '':

        return float(user_text_dist)
    else:
        return 0


def Saida(msg):
    mensagem = f'{msg}'
    txt_formatado = Fontes.font.render(mensagem, True, (255, 255, 255))
    return txt_formatado


def Grade():
    i = parametros.altura-70
    while i >= 0:
        pygame.draw.line(tela, (100, 100, 100), (0, i), (parametros.largura, i))
        i = i - 50
    j = 0
    while j <= parametros.largura:
        pygame.draw.line(tela, (100, 100, 100), (j, 0), (j, parametros.altura))
        j = j + 50

    x = 0
    y = 0
    t = 0

    while t < Moto.t:
        y = (Moto.posy - ((velocidade * (5 / 3)) * (math.sin(math.radians(angulo)) * t) - ((5 / 90) * 4.9) * (
            t * t))) + 50
        x = (Moto.posx + ((5 / 3) * velocidade * math.cos(math.radians(angulo))) * t) + 25

        if y < parametros.altura-100 or x < (Entrada_distancia() * 50) + parametros.dist_rampa:
            pygame.draw.circle(tela, (255, 0, 0), (x, y), 3)
      
        t = t+1

while True:

    Tela()
    # print(fps)
    if Moto.teste:
        pygame.draw.circle(tela, (0, 255, 0), (500, 500), 50)

    Grade()

    angulo_user = Entrada_angulo()
    velocidade_user = Entrada_velocidade()
    distancia_user = (Entrada_distancia() * 50) + parametros.dist_rampa
 
    Rampa(angulo)

    #colisao com o "chao"
    if Moto.rect.y > parametros.altura-120:
        if Moto.rect.x > distancia_user:
            Moto.rect.y = parametros.altura-120
            Moto.ang = 0
            Moto.image = pygame.transform.rotate(Moto.og_image, Moto.ang)
            Moto.pulo = False
            Moto.rampa = False

    sprites.draw(tela)
    sprites.update(angulo, velocidade)

    for event in pygame.event.get():

        # readequar conteudo ao redimensionar a tela
        if event.type == pygame.VIDEORESIZE:
            parametros.largura=event.w
            parametros.altura=event.h

            Moto.rect.bottomleft = [0, parametros.altura-70]

            tela = pygame.display.set_mode((parametros.largura, parametros.altura), pygame.RESIZABLE)


        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Fontes.input_rect_angulo.collidepoint(event.pos):
                user_text_ang = ''
                active_angulo = True

            elif Fontes.input_rect_velocidade.collidepoint(event.pos):
                user_text_vel = ''
                active_velocidade = True

            elif Fontes.input_rect_distancia.collidepoint(event.pos):
                user_text_dist = ''
                active_distancia = True

            else:
                active_angulo = False
                active_velocidade = False
                active_distancia = False

        if active_angulo:
            color_angulo = (180, 0, 0)
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text_ang = user_text_ang[:-1]
                    # if user_text_ang == '':
                    #    user_text_ang = '0'

                # Unicode standard is used for string
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    active_angulo = False
                    color_angulo = (120, 0, 0)

                    if 80 >= angulo_user >= 0:
                        angulo = angulo_user

                if 48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741922:
                    user_text_ang += event.unicode


        else:
            color = Fontes.color_passive
            if angulo_user > 80:
                user_text_ang = '80'

            if angulo_user < 0:
                user_text_ang = '0'

        # draw rectangle and argument passed which should
        # be on screen

        if active_velocidade:
            color_velocidade = (0, 180, 0)

            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text_vel = user_text_vel[:-1]

                # Unicode standard is used for string
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    active_velocidade = False
                    color_velocidade = (0, 120, 0)

                    if 50 >= velocidade_user >= 0:
                        velocidade = velocidade_user

                if 48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741922:
                    user_text_vel += event.unicode

        if active_distancia:
            color_distancia = (0, 0, 180)
            
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text_dist = user_text_dist[:-1]

                # Unicode standard is used for string
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    active_distancia = False
                    color_distancia = (0, 0, 120)

                    if 30 >= distancia_user >= 0:
                        distancia = distancia_user

                if 48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741922 or event.key == pygame.K_PERIOD:
                    user_text_dist += event.unicode

        else:
            if distancia_user > 1700 or distancia_user < 00:
                user_text_dist = '0'

    pygame.display.update()
