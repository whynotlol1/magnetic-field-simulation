import time
import math
import pygame
import scipy.integrate as integrate


pygame.init()
standart = height = width = 800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("magnetic field simulation")
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

magnet_standart = 25
magnet_data = {
    "coords": [375, 375],
    "moving_speed": 0.3,
    "strength": 0.44,  # strength parameter must be greater or equal to 0.35
    "magnetic_lines_direction": "up-down"
}

if __name__ == '__main__':
    try:
        running = True
        while running:

            # drawing the magnet and the magnetic field
            screen.fill((255, 255, 255))
            text_surface = my_font.render(f'magnet strength (induction): {round(magnet_data["strength"], 2)}', False, (0, 0, 0))
            screen.blit(text_surface, (0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (magnet_data["coords"][0] - magnet_standart / 2, magnet_data["coords"][1] - magnet_standart / 2, magnet_standart, magnet_standart))
            param = integrate.quad(lambda x: magnet_data["strength"] * standart, 0, magnet_data["strength"])[0]
            for i in range(0, width, 5):
                for j in range(0, height, 5):
                    if math.sqrt((i - magnet_data["coords"][0]) ** 2 + (j - magnet_data["coords"][1]) ** 2) < param:
                        pygame.draw.circle(screen, (0, 255, 0), (i, j), 1)

            # controls
            keys = pygame.key.get_pressed()

            if keys[pygame.K_w] and magnet_data["coords"][1] > 0:
                magnet_data["coords"][1] -= magnet_data["moving_speed"]
            if keys[pygame.K_s] and magnet_data["coords"][1] < height - magnet_standart:
                magnet_data["coords"][1] += magnet_data["moving_speed"]
            if keys[pygame.K_d] and magnet_data["coords"][0] < width - magnet_standart:
                magnet_data["coords"][0] += magnet_data["moving_speed"]
            if keys[pygame.K_a] and magnet_data["coords"][0] > 0:
                magnet_data["coords"][0] -= magnet_data["moving_speed"]

            if keys[pygame.K_1]:
                magnet_data["strength"] += 0.01
                time.sleep(0.1)
            if keys[pygame.K_2]:
                magnet_data["strength"] = magnet_data["strength"] - 0.01 if magnet_data["strength"] > 0.35 else magnet_data["strength"]
                time.sleep(0.1)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit(0)

    except Exception as e:
        print(f"unknown error occurred: {e}")
        exit(0)
