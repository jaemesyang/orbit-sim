import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

sun = {"x": 400, "y": 400, "mass": 200, "size": 20, "color": (255, 220, 0)}
planet1 = {"x": 400, "y": 200, "mass": 6, "vel_x": 7.07, "vel_y": 0, "ax": 0, "ay": 0,"ax_new": 0, "ay_new": 0, "size": 8, "color": (255, 0, 0), "trail": []}
planet2 = {"x": 300, "y": 300, "mass": 8, "vel_x": -5.95, "vel_y": 5.95, "ax": 0, "ay": 0, "ax_new": 0, "ay_new": 0, "size": 8, "color": (0, 0, 255), "trail": []}
planet3 = {"x": 500, "y": 600, "mass": 5, "vel_x": 5.98, "vel_y": -2.99, "ax": 0, "ay": 0, "ax_new": 0, "ay_new": 0, "size": 8, "color": (0, 255, 0), "trail": []}
bodies = [sun, planet1, planet2, planet3]

gravityvconstant = 50
dt = 0.1
speed = 10

zoom = 0.5
center_x = 400
center_y = 400

trail = [] 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                zoom -= 0.1
            if event.key == pygame.K_UP:
                zoom += 0.1

    screen.fill((0, 0, 0))
    for init in bodies:
        screen_x = int((init["x"] - center_x) * zoom + 400)
        screen_y = int((init["y"] - center_y) * zoom + 400)
        pygame.draw.circle(screen, init["color"], (int(screen_x), int(screen_y)), int(init["size"] * zoom))

    for _ in range(speed):
        for i in bodies:
            i["ax"] = 0
            i["ay"] = 0
            for j in bodies:
                if i != j and i != sun: 
                    distance = math.sqrt((i["y"]-j["y"])**2+(i["x"]-j["x"])**2)
                    direction = math.atan2(j["y"] - i["y"], j["x"] - i["x"])
                    i["ax"] += math.cos(direction) * (gravityvconstant * j["mass"]/(distance**2))
                    i["ay"] += math.sin(direction) * (gravityvconstant * j["mass"]/(distance**2))
        for body in bodies:
            if body != sun:
                body["ax_new"] = 0
                body["ay_new"] = 0
                body["x"] += body["vel_x"] * dt + 0.5 * body["ax"] *(dt**2)
                body["y"] += body["vel_y"] * dt + 0.5 * body["ay"] *(dt**2)
        for i in bodies:
            for j in bodies:
                if i != j and i != sun: 
                    distance = math.sqrt((i["y"]-j["y"])**2+(i["x"]-j["x"])**2)
                    direction = math.atan2(j["y"] - i["y"], j["x"] - i["x"])
                    i["ax_new"] += math.cos(direction) * (gravityvconstant * j["mass"]/(distance**2))
                    i["ay_new"] += math.sin(direction) * (gravityvconstant * j["mass"]/(distance**2))
        for body in bodies:
            if body != sun:
                body["vel_x"] += 0.5 * (body["ax"] + body["ax_new"]) * dt
                body["vel_y"] += 0.5 * (body["ay"] + body["ay_new"]) * dt
                body["ax"] = body["ax_new"]
                body["ay"] = body["ay_new"] 
    for body in bodies:
        if body != sun:
            screen_x = int((body["x"] - center_x) * zoom + 400)
            screen_y = int((body["y"] - center_y) * zoom + 400)
            body["trail"].append((int(screen_x), int(screen_y)))
            if len(body["trail"]) > 200:
                body["trail"].pop(0)
            for point in body["trail"]:
                screen.fill(body["color"], (point[0], point[1], 2, 2))
    pygame.display.flip()
    clock.tick(500)

pygame.quit()