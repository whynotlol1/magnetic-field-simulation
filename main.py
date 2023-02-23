import time
import pygame
import scipy.integrate as integrate

pygame.init()
standart = height = width = 800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("magnetic field simulation")
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

magnet_standart = 25
magnet1 = pygame.Surface((magnet_standart, magnet_standart))
magnet1_data = {
    "coords": [375, 375],
    "moving_speed": 0.3,
    "strength": 0.42,  # strength parameter must be greater or equal to 0.35
    "magnetic_lines_direction": "up-down"
}

magnet2 = pygame.Surface((magnet_standart, magnet_standart))
magnet2_data = {
    "coords": [375, 375],
    "moving_speed": 0.3,
    "strength": 0.44,  # strength parameter must be greater or equal to 0.35
    "magnetic_lines_direction": "up-down"
}

if __name__ == '__main__':
    running = True
    while running:
        screen.fill((255, 255, 255))
        text_surface = my_font.render(f'1st magnet strength (induction): {round(magnet1_data["strength"], 2)}', False, (0, 0, 0))
        screen.blit(text_surface, (0, 0))
        text_surface = my_font.render(f'2nd magnet strength (induction): {round(magnet2_data["strength"], 2)}', False, (0, 0, 0))
        screen.blit(text_surface, (0, 40))
        screen.blit(magnet1, (magnet1_data["coords"][0] - magnet_standart, magnet1_data["coords"][1] - magnet_standart))
        screen.blit(magnet2, (magnet2_data["coords"][0] - magnet_standart, magnet2_data["coords"][1] - magnet_standart))
        param = integrate.quad(lambda x: magnet1_data["strength"] * standart, 0, magnet1_data["strength"])[0]
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) - param + 2), magnet1_data["coords"][1] - magnet_standart / 2), param, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) + param - 2), magnet1_data["coords"][1] - magnet_standart / 2), param, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) - (param / 1.5) + 2), magnet1_data["coords"][1] - magnet_standart / 2), param / 1.5, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) + (param / 1.5) - 2), magnet1_data["coords"][1] - magnet_standart / 2), param / 1.5, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) - (param / 2) + 2), magnet1_data["coords"][1] - magnet_standart / 2), param / 2, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) + (param / 2) - 2), magnet1_data["coords"][1] - magnet_standart / 2), param / 2, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) - (param / 3) + 2), magnet1_data["coords"][1] - magnet_standart / 2), param / 3, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet1_data["coords"][0] - magnet_standart / 2) + (param / 3) - 2), magnet1_data["coords"][1] - magnet_standart / 2), param / 3, 2)
        param = integrate.quad(lambda x: magnet2_data["strength"] * standart, 0, magnet2_data["strength"])[0]
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) - param + 2), magnet2_data["coords"][1] - magnet_standart / 2), param, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) + param - 2), magnet2_data["coords"][1] - magnet_standart / 2), param, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) - (param / 1.5) + 2), magnet2_data["coords"][1] - magnet_standart / 2), param / 1.5, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) + (param / 1.5) - 2), magnet2_data["coords"][1] - magnet_standart / 2), param / 1.5, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) - (param / 2) + 2), magnet2_data["coords"][1] - magnet_standart / 2), param / 2, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) + (param / 2) - 2), magnet2_data["coords"][1] - magnet_standart / 2), param / 2, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) - (param / 3) + 2), magnet2_data["coords"][1] - magnet_standart / 2), param / 3, 2)
        pygame.draw.circle(screen, (0, 0, 0), (int((magnet2_data["coords"][0] - magnet_standart / 2) + (param / 3) - 2), magnet2_data["coords"][1] - magnet_standart / 2), param / 3, 2)

        # controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and magnet1_data["coords"][1] > 0 + magnet_standart:
            magnet1_data["coords"][1] -= magnet1_data["moving_speed"]
        if keys[pygame.K_DOWN] and magnet1_data["coords"][1] < height:
            magnet1_data["coords"][1] += magnet1_data["moving_speed"]
        if keys[pygame.K_RIGHT] and magnet1_data["coords"][0] < width:
            magnet1_data["coords"][0] += magnet1_data["moving_speed"]
        if keys[pygame.K_LEFT] and magnet1_data["coords"][0] > 0 + magnet_standart:
            magnet1_data["coords"][0] -= magnet1_data["moving_speed"]

        if keys[pygame.K_w] and magnet2_data["coords"][1] > 0 + magnet_standart:
            magnet2_data["coords"][1] -= magnet2_data["moving_speed"]
        if keys[pygame.K_s] and magnet2_data["coords"][1] < height:
            magnet2_data["coords"][1] += magnet2_data["moving_speed"]
        if keys[pygame.K_d] and magnet2_data["coords"][0] < width:
            magnet2_data["coords"][0] += magnet2_data["moving_speed"]
        if keys[pygame.K_a] and magnet2_data["coords"][0] > 0 + magnet_standart:
            magnet2_data["coords"][0] -= magnet2_data["moving_speed"]

        if keys[pygame.K_1]:
            magnet1_data["strength"] += 0.01
            time.sleep(0.1)
        if keys[pygame.K_2]:
            magnet1_data["strength"] = magnet1_data["strength"] - 0.01 if magnet1_data["strength"] > 0.35 else magnet1_data["strength"]
            time.sleep(0.1)

        if keys[pygame.K_4]:
            magnet2_data["strength"] += 0.01
            time.sleep(0.1)
        if keys[pygame.K_5]:
            magnet2_data["strength"] = magnet2_data["strength"] - 0.01 if magnet2_data["strength"] > 0.35 else magnet2_data["strength"]
            time.sleep(0.1)

        if keys[pygame.K_3]:
            magnet1_data["magnetic_lines_direction"] = "up-down" if magnet1_data["magnetic_lines_direction"] == "down-up" else "down-up"
        if keys[pygame.K_6]:
            magnet2_data["magnetic_lines_direction"] = "up-down" if magnet2_data["magnetic_lines_direction"] == "down-up" else "down-up"

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit(0)
