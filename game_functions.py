import pygame
import sys
import random


def update_ball(ball, stats):
    ball.update()
    
    if stats.lifes_left >= 0:
        if ball.rect.bottom >= ball.screen_rect.bottom:
            ball.reset()
            stats.lifes_left -= 1
            print(stats.lifes_left)
    else:
        stats.game_active = False


def check_bottom(screen, ball, stats):
    screen_rect = screen.get_rect()

    if stats.lifes_left > 0:

        if ball.rect.bottom >= screen_rect.bottom:
            ball.reset()
            stats.lifes_left -= 1 
            print(stats.lifes_left)
    else:
        stats.game_active = False


def check_collide(screen, ball, kratos, stats, sb):
    if ball.rect.colliderect(kratos):
        stats.score += 1
        sb.prep_score()
        print(stats.score)
        ball.reset()

    # check_bottom(screen, ball, stats)


def check_keydown(event, settings, kratos):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_a:
        kratos.moving_left = True
        if kratos.direction == 1:
            kratos.flip()
            kratos.direction *= -1

    elif event.key == pygame.K_d:
        kratos.moving_right = True
        if kratos.direction == -1:
            kratos.flip()
            kratos.direction *= -1

    elif event.key == pygame.K_PLUS:
        if not settings.volume >= 1:
            settings.volume += 0.1

    elif event.key == pygame.K_MINUS:
        if not settings.volume <= 0:
            settings.volume -= 0.1

def check_keyup(event, kratos):
    if event.key == pygame.K_a:
        kratos.moving_left = False
    elif event.key == pygame.K_d:
        kratos.moving_right = False

def check_events(settings, kratos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown(event, settings, kratos)
        elif event.type == pygame.KEYUP:
            check_keyup(event, kratos)

def update_screen(settings, screen, kratos, ball, stats, sb, vidas):
    # screen.fill(settings.bg_color)
    screen.blit(settings.bg_image, (0, 0))
    sb.show_score()
    kratos.blitme()
    vidas.blitme()
    ball.blitme()

    check_collide(screen, ball, kratos, stats, sb)

    pygame.display.flip()
