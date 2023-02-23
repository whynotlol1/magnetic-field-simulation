import time
import pygame
import scipy.integrate as integrate

pygame.init()
height = width = 800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("magnetic field simulation")
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

magnet_standart = 25
magnet1 = pygame.Surface((magnet_standart, magnet_standart))
magnet1_data = {
    "coords": [375, 375],
    "moving_speed": 0.3,
    "strength": 0.53 # strength parameter must be greater or equal to 0.35
}

magnet2 = pygame.Surface((magnet_standart, magnet_standart))
magnet2_data = {
    "coords": [375, 375],
    "moving_speed": 0.3,
    "strength": 0.53 # strength parameter must be greater or equal to 0.35
}

if __name__ == '__main__':
    running = True
    while running:
        screen.fill((255, 255, 255))
        text_surface = my_font.render(f'1st magnet strength (induction): {round(magnet1_data["strength"], 2)}', False, (0, 0, 0))
        screen.blit(text_surface, (0, 0))
        text_surface = my_font.render(f'2nd magnet strength (induction): {round(magnet2_data["strength"], 2)}', False, (0, 0, 0))
        screen.blit(text_surface, (0, 40))
        screen.blit(magnet1, (magnet1_data["coords"][0] - magnet_standart / 2, magnet1_data["coords"][1] - magnet_standart / 2))
        screen.blit(magnet2, (magnet2_data["coords"][0] - magnet_standart / 2, magnet2_data["coords"][1] - magnet_standart / 2))
        magnetic_field_line_radius = integrate.quad(lambda x: magnet1_data["strength"] * standart, 0, magnet1_data["strength"])[0]
        pygame.draw.circle(screen, (255, 0, 255), (magnet1_data["coords"][0], magnet1_data["coords"][1]), magnetic_field_line_radius / 4, 2)
        pygame.draw.circle(screen, (255, 0, 255), (magnet1_data["coords"][0], magnet1_data["coords"][1]), magnetic_field_line_radius / 2, 2)
        pygame.draw.circle(screen, (255, 0, 255), (magnet1_data["coords"][0], magnet1_data["coords"][1]), magnetic_field_line_radius / 1.5, 2)
        pygame.draw.circle(screen, (255, 0, 255), (magnet1_data["coords"][0], magnet1_data["coords"][1]), magnetic_field_line_radius, 2)
        magnetic_field_line_radius = integrate.quad(lambda x: magnet2_data["strength"] * standart, 0, magnet2_data["strength"])[0]
        pygame.draw.circle(screen, (255, 0, 255), (magnet2_data["coords"][0], magnet2_data["coords"][1]), magnetic_field_line_radius / 4, 2)
        pygame.draw.circle(screen, (255, 0, 255), (magnet2_data["coords"][0], magnet2_data["coords"][1]), magnetic_field_line_radius / 2, 2)
        pygame.draw.circle(screen, (255, 0, 255), (magnet2_data["coords"][0], magnet2_data["coords"][1]), magnetic_field_line_radius / 1.5, 2)
        pygame.draw.circle(screen, (255, 0, 255), (magnet2_data["coords"][0], magnet2_data["coords"][1]), magnetic_field_line_radius, 2)



        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and magnet1_data["coords"][1] > 0 + magnet_standart / 2:
            magnet1_data["coords"][1] -= magnet1_data["moving_speed"]
        if keys[pygame.K_DOWN] and magnet1_data["coords"][1] < height - magnet_standart / 2:
            magnet1_data["coords"][1] += magnet1_data["moving_speed"]
        if keys[pygame.K_RIGHT] and magnet1_data["coords"][0] < width - magnet_standart / 2:
            magnet1_data["coords"][0] += magnet1_data["moving_speed"]
        if keys[pygame.K_LEFT] and magnet1_data["coords"][0] > 0 + magnet_standart / 2:
            magnet1_data["coords"][0] -= magnet1_data["moving_speed"]

        if keys[pygame.K_w] and magnet2_data["coords"][1] > 0 + magnet_standart / 2:
            magnet2_data["coords"][1] -= magnet2_data["moving_speed"]
        if keys[pygame.K_s] and magnet2_data["coords"][1] < height - magnet_standart / 2:
            magnet2_data["coords"][1] += magnet2_data["moving_speed"]
        if keys[pygame.K_d] and magnet2_data["coords"][0] < width - magnet_standart / 2:
            magnet2_data["coords"][0] += magnet2_data["moving_speed"]
        if keys[pygame.K_a] and magnet2_data["coords"][0] > 0 + magnet_standart / 2:
            magnet2_data["coords"][0] -= magnet2_data["moving_speed"]

        if keys[pygame.K_1]:
            magnet1_data["strength"] += 0.01
            time.sleep(0.1)
        if keys[pygame.K_2]:
            magnet1_data["strength"] = magnet1_data["strength"] - 0.01 if magnet1_data["strength"] > 0.35 else magnet1_data["strength"]
            time.sleep(0.1)

        if keys[pygame.K_3]:
            magnet2_data["strength"] += 0.01
            time.sleep(0.1)
        if keys[pygame.K_4]:
            magnet2_data["strength"] = magnet2_data["strength"] - 0.01 if magnet2_data["strength"] > 0.35 else magnet2_data["strength"]
            time.sleep(0.1)


        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit(0)
