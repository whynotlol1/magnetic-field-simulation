import time
import math
import pygame
import scipy.integrate as integrate


def calculate_l(x1, y1, x2, y2) -> list[float, float, float]:
    return [math.sqrt((x1-x2)**2+(y1-y2)**2), (x1-x2), (y1-y2)]


pygame.init()
standart = height = width = 800
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("magnetic field simulation")
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

magnet_standart = 25
magnet_gravity_speed_standart = 0.4
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
    try:
        running = True
        while running:
    
            # drawing the magnets
            screen.fill((255, 255, 255))
            text_surface = my_font.render(f'1st magnet strength (induction): {round(magnet1_data["strength"], 2)}', False, (0, 0, 0))
            screen.blit(text_surface, (0, 0))
            text_surface = my_font.render(f'2nd magnet strength (induction): {round(magnet2_data["strength"], 2)}', False, (0, 0, 0))
            screen.blit(text_surface, (0, 40))
            screen.blit(magnet1, (magnet1_data["coords"][0] - magnet_standart, magnet1_data["coords"][1] - magnet_standart))
            screen.blit(magnet2, (magnet2_data["coords"][0] - magnet_standart, magnet2_data["coords"][1] - magnet_standart))
            param1 = integrate.quad(lambda x: magnet1_data["strength"] * standart, 0, magnet1_data["strength"])[0]
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) - param1 + 2), magnet1_data["coords"][1] - magnet_standart / 2), param1, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) + param1 - 2), magnet1_data["coords"][1] - magnet_standart / 2), param1, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) - (param1 / 1.5) + 2), magnet1_data["coords"][1] - magnet_standart / 2), param1 / 1.5, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) + (param1 / 1.5) - 2), magnet1_data["coords"][1] - magnet_standart / 2), param1 / 1.5, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) - (param1 / 2) + 2), magnet1_data["coords"][1] - magnet_standart / 2), param1 / 2, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) + (param1 / 2) - 2), magnet1_data["coords"][1] - magnet_standart / 2), param1 / 2, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) - (param1 / 3) + 2), magnet1_data["coords"][1] - magnet_standart / 2), param1 / 3, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet1_data["coords"][0] - magnet_standart / 2) + (param1 / 3) - 2), magnet1_data["coords"][1] - magnet_standart / 2), param1 / 3, 2)
            param2 = integrate.quad(lambda x: magnet2_data["strength"] * standart, 0, magnet2_data["strength"])[0]
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) - param2 + 2), magnet2_data["coords"][1] - magnet_standart / 2), param2, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) + param2 - 2), magnet2_data["coords"][1] - magnet_standart / 2), param2, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) - (param2 / 1.5) + 2), magnet2_data["coords"][1] - magnet_standart / 2), param2 / 1.5, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) + (param2 / 1.5) - 2), magnet2_data["coords"][1] - magnet_standart / 2), param2 / 1.5, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) - (param2 / 2) + 2), magnet2_data["coords"][1] - magnet_standart / 2), param2 / 2, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) + (param2 / 2) - 2), magnet2_data["coords"][1] - magnet_standart / 2), param2 / 2, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) - (param2 / 3) + 2), magnet2_data["coords"][1] - magnet_standart / 2), param2 / 3, 2)
            pygame.draw.circle(screen, (255, 0, 255), (int((magnet2_data["coords"][0] - magnet_standart / 2) + (param2 / 3) - 2), magnet2_data["coords"][1] - magnet_standart / 2), param2 / 3, 2)
    
            distance = calculate_l(magnet1_data["coords"][0], magnet1_data["coords"][1], magnet2_data["coords"][0], magnet2_data["coords"][1])
    
            # gravitation 'physics'
            if param1 + param2 > distance[0]:
                if distance[1] == distance[2] == 0:
                    pass
                else:
                    if distance[1] == 0:
                        if distance[2] > 0:
                            pass
                        elif distance[2] < 0:
                            pass
                    elif distance[2] == 0:
                        if distance[1] > 0:
                            pass
                        elif distance[1] < 0:
                            pass
                    else:
                        if distance[1] > 0:
                            if distance[2] > 0:
                                pass
                            elif distance[2] < 0:
                                pass
                        elif distance[1] < 0:
                            if distance[2] > 0:
                                pass
                            elif distance[2] < 0:
                                pass
    
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
    except Exception as e:
        print(f"unknown error occurred: {e}")
        exit(0)
