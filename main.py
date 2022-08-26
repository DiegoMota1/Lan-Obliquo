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
tela = pygame.display.set_mode((parametros.largura, parametros.altura))
pygame.display.set_caption('movimento obliquo')
fps = pygame.time.Clock()
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)
# Tela acaba aqui


angulo_temp = 0
user_text_ang = 0
velocidade_temp = 0
user_text_vel = 0
distancia_temp = 0
user_text_dist = 0
color = (255, 0, 0)
angulo = 0
velocidade = 0
distancia = 0

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
    pygame.draw.line(tela, (255, 0, 0), (0, 950), (1920, 950), 5)
    angulo = math.radians(angulo)
    parametros.base_rampa = 100 * math.cos(angulo)
    parametros.altura_rampa = 100 * math.sin(angulo)
    pygame.draw.line(tela, (255, 255, 255), (0, 950), (parametros.dist_rampa + parametros.base_rampa, 950), 20)
    pygame.draw.line(tela, (255, 255, 255), (parametros.dist_rampa, 950),
                     (parametros.dist_rampa + parametros.base_rampa, 950 - parametros.altura_rampa),
                     20)
    pygame.draw.line(tela, (255, 255, 255), (distancia_user, 950), (1920, 950), 20)


def Entrada_angulo():
    pygame.draw.rect(tela, color, Fontes.input_rect_angulo)
    angulo_temp = Fontes.base_font.render(str(user_text_ang), True, (255, 255, 255))
    tela.blit(angulo_temp, (Fontes.input_rect_angulo.x + 10, Fontes.input_rect_angulo.y + 5))
    Fontes.input_rect_angulo.w = max(100, angulo_temp.get_width() + 10)
    if user_text_ang != '':

        return int(user_text_ang)
    else:
        return 0


def Entrada_velocidade():
    pygame.draw.rect(tela, color, Fontes.input_rect_velocidade)
    velocidade_temp = Fontes.base_font.render(str(user_text_vel), True, (255, 255, 255))
    tela.blit(velocidade_temp, (Fontes.input_rect_velocidade.x + 10, Fontes.input_rect_velocidade.y + 5))
    Fontes.input_rect_velocidade.w = max(100, velocidade_temp.get_width() + 10)
    if user_text_vel != '':

        return int(user_text_vel)
    else:
        return 0


def Entrada_distancia():
    pygame.draw.rect(tela, color, Fontes.input_rect_distancia)
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
    i = 950
    while i >= 0:
        pygame.draw.line(tela, (255, 255, 255), (0, i), (1920, i))
        i = i - 50
    j = 0
    while j <= 1920:
        pygame.draw.line(tela, (255, 255, 255), (j, 0), (j, 1020))
        j = j + 50

    x = 0
    y = 0
    t = 0

    while t < Moto.t:
        y = (Moto.posy - ((velocidade * (5 / 3)) * (math.sin(math.radians(angulo)) * t) - ((5 / 90) * 4.9) * (
            t * t))) + 50
        x = (Moto.posx + ((5 / 3) * velocidade * math.cos(math.radians(angulo))) * t) + 25
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
    distancia_user = (Entrada_distancia() * 50) + 400
    Rampa(angulo)

    Entrada_angulo()

    sprites.draw(tela)
    sprites.update(angulo, velocidade)

    # print (Moto.rect.x)

    for event in pygame.event.get():

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

            color = Fontes.color_active
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

                    if 80 >= angulo_user >= 0:
                        angulo = angulo_user

                if 48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741922:
                    user_text_ang += event.unicode


        else:
            color = Fontes.color_passive
            if angulo_user > 80 or angulo_user < 0:
                user_text_ang = '0'

        # draw rectangle and argument passed which should
        # be on screen

        if active_velocidade:
            color = Fontes.color_active
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text_vel = user_text_vel[:-1]

                # Unicode standard is used for string
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    active_velocidade = False
                    if 50 >= velocidade_user >= 0:
                        velocidade = velocidade_user

                if 48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741922:
                    user_text_vel += event.unicode

        if active_distancia:
            color = Fontes.color_active
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text_dist = user_text_dist[:-1]

                # Unicode standard is used for string
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    active_distancia = False
                    if 30 >= distancia_user >= 0:
                        distancia = distancia_user

                if 48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741922 or event.key == pygame.K_PERIOD:
                    user_text_dist += event.unicode

        else:
            color = Fontes.color_passive
            if distancia_user > 1700 or distancia_user < 00:
                user_text_dist = '0'

    pygame.display.update()
