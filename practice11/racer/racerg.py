import pygame
import random
import os

pygame.init()

# размеры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# путь к файлам
base_path = os.path.dirname(os.path.abspath(__file__))

# загрузка картинок
player_img = pygame.image.load(os.path.join(base_path, "space_racer.png")).convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 70))

coin_img = pygame.image.load(os.path.join(base_path, "coin.png")).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (30, 30))

enemy_img = pygame.image.load(os.path.join(base_path, "enemy.png")).convert_alpha()
enemy_img = pygame.transform.scale(enemy_img, (50, 70))

WHITE = (255, 255, 255)

# игрок
player = pygame.Rect(180, 500, 50, 70)

# враг
enemy = pygame.Rect(random.randint(0, WIDTH - 50), -100, 50, 70)
enemy_speed = 5

# список монет (x, y, weight)
coins = []

score = 0
font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill((0, 0, 0))

    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # ограничение
    player.x = max(0, min(player.x, WIDTH - player.width))

    # =========================
    # генерация монет
    # =========================
    if random.randint(1, 40) == 1:
        x = random.randint(0, WIDTH - 30)

        # случайный "вес" монеты (1, 2 или 3 очка)
        weight = random.choice([1, 2, 3])

        coins.append({"rect": pygame.Rect(x, 0, 30, 30), "weight": weight})

    # =========================
    # движение монет
    # =========================
    for coin in coins[:]:
        coin["rect"].y += 5

        # если поймал монету
        if player.colliderect(coin["rect"]):
            score += coin["weight"]   # добавляем вес
            coins.remove(coin)

        elif coin["rect"].y > HEIGHT:
            coins.remove(coin)

    # =========================
    # движение врага
    # =========================
    enemy.y += enemy_speed

    # если враг вышел за экран → сверху снова
    if enemy.y > HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(0, WIDTH - 50)

    # столкновение = GAME OVER
    if player.colliderect(enemy):
        print("GAME OVER")
        running = False

    # =========================
    # ⚡ увеличение скорости
    # =========================
    if score % 5 == 0 and score != 0:
        enemy_speed = 5 + score // 5   # каждые 5 монет быстрее

    # =========================
    # отрисовка
    # =========================
    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)

    for coin in coins:
        screen.blit(coin_img, coin["rect"])

        # показываем вес монеты
        weight_text = font.render(str(coin["weight"]), True, WHITE)
        screen.blit(weight_text, (coin["rect"].x + 10, coin["rect"].y))

    # счет
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()