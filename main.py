import pygame
import game_functions as gf
from settings import Settings
from kratos import Kratos
from ball import Ball
from game_stats import GameStats
from scoreboard import ScoreBoard
from vidas import Vidas

pygame.init()

settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption('Ball game')

stats = GameStats(settings)

clock = pygame.time.Clock()

# Kratos
kratos = Kratos(settings, screen)

vidas = Vidas(settings, screen, stats)

# Ball
ball = Ball(settings, screen)

sb = ScoreBoard(settings, screen, stats)

# Background sound
pygame.mixer.music.load(settings.musica)
pygame.mixer.music.play(-1)

while True:
    gf.check_events(settings, kratos)

    if stats.game_active:
        gf.update_ball(ball, stats)
        kratos.update()

    gf.update_screen(settings, screen, kratos, ball, stats, sb, vidas)
    clock.tick(75)
    pygame.mixer.music.set_volume(settings.volume)
