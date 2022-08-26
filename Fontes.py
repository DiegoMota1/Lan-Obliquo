import pygame
pygame.init()

font = pygame.font.Font('freesansbold.ttf', 32)
pygame.font.SysFont('fonte', 24, 1)
base_font = pygame.font.Font(None, 32)
tiny_font = pygame.font.Font(None, 16)

input_rect_angulo = pygame.Rect(200, 200, 140, 32)
input_rect_velocidade = pygame.Rect(200, 300, 140, 32)
input_rect_distancia = pygame.Rect(200, 400, 140, 32)

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
