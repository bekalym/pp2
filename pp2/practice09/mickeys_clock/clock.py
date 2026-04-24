import pygame
import datetime
import sys

def run_clock():
    pygame.init()

    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mickey Clock")

    clock = pygame.time.Clock()

    # загрузка изображений
    bg = pygame.image.load("images/mickey_no_arms.png")
    right_hand = pygame.image.load("images/mickey_right-hand.png")
    left_hand = pygame.image.load("images/mickey_left-hand.png")

    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

    center = (WIDTH // 2, HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg, (0, 0))

        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        # углы
        sec_angle = -seconds * 6
        min_angle = -minutes * 6

        # вращение
        sec_rotated = pygame.transform.rotate(left_hand, sec_angle)
        min_rotated = pygame.transform.rotate(right_hand, min_angle)

        # центрируем
        sec_rect = sec_rotated.get_rect(center=center)
        min_rect = min_rotated.get_rect(center=center)

        # рисуем
        screen.blit(min_rotated, min_rect)
        screen.blit(sec_rotated, sec_rect)

        pygame.display.flip()
        clock.tick(60)