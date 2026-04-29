import pygame, sys, random, time
from racer import Player, Enemy, Collectible
from persistence import save_score, get_leaderboard, get_settings, save_settings
from ui import Button, draw_text

# Инициализация
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SIS 3: Advanced Racer")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 40)

# Загрузка ресурсов
bg = pygame.image.load("assets/street.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

def get_user_name():
    name = ""
    entering = True
    while entering:
        screen.fill((50, 50, 50))
        draw_text(screen, "Enter Your Name:", font, (255,255,255), 100, 250)
        draw_text(screen, name + "_", big_font, (255, 255, 0), 100, 300)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name != "":
                    entering = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 10:
                        name += event.unicode
        pygame.display.update()
    return name

def game_loop(user_name):
    settings = get_settings()
    # Настройка сложности
    base_speed = 5 if settings['difficulty'] == "Easy" else 8
    
    player = Player(settings['car_color'])
    enemies = pygame.sprite.Group()
    enemies.add(Enemy(base_speed))
    
    items = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    score = 0
    distance = 0
    coins_count = 0
    active_powerup = None
    powerup_timer = 0
    bg_y = 0

    running = True
    while running:
        # 1. Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2. Логика сложности и движения фона
        distance += 0.1
        bg_y += base_speed
        if bg_y >= HEIGHT: bg_y = 0
        
        # 3. Спавн предметов (монеты и бонусы)
        if random.randint(1, 100) < 3:
            p_type = random.choice(["coin", "nitro", "shield", "repair"])
            img = f"assets/{p_type.capitalize()}.png"
            items.add(Collectible(img, value=10 if p_type=="coin" else 0, type=p_type))

        # 4. Обновление позиций
        player.move()
        for enemy in enemies:
            enemy.move()
        items.update(base_speed)

        # 5. Коллизии
        # С врагами
        if pygame.sprite.spritecollideany(player, enemies):
            if player.shielded:
                player.shielded = False
                active_powerup = None
                # Убираем врага, чтобы не застрять в нем
                for e in enemies: e.rect.top = -100 
            else:
                save_score(user_name, score, distance)
                return "GAME_OVER", score, int(distance)

        # С бонусами
        hit_item = pygame.sprite.spritecollideany(player, items)
        if hit_item:
            if hit_item.type == "coin":
                score += 10
                coins_count += 1
                if coins_count % 5 == 0: # Ускорение каждые 5 монет
                    for e in enemies: e.speed += 1
            elif hit_item.type == "nitro":
                active_powerup = "Nitro"
                powerup_timer = time.time() + 5
                player.speed = 10
            elif hit_item.type == "shield":
                active_powerup = "Shield"
                player.shielded = True
                powerup_timer = time.time() + 10
            elif hit_item.type == "repair":
                score += 50 # Repair просто дает очки в этой версии
            hit_item.kill()

        # Проверка таймеров бонусов
        if active_powerup and time.time() > powerup_timer:
            if active_powerup == "Nitro": player.speed = 5
            if active_powerup == "Shield": player.shielded = False
            active_powerup = None

        # 6. Отрисовка
        screen.blit(bg, (0, bg_y))
        screen.blit(bg, (0, bg_y - HEIGHT))
        
        for entity in all_sprites: screen.blit(entity.image, entity.rect)
        for enemy in enemies: screen.blit(enemy.image, enemy.rect)
        for item in items: screen.blit(item.image, item.rect)

        # UI внутри игры
        draw_text(screen, f"Score: {score}", font, (0,0,0), 10, 10)
        draw_text(screen, f"Dist: {int(distance)}m", font, (0,0,0), 10, 35)
        if active_powerup:
            draw_text(screen, f"Buff: {active_powerup}", font, (255,0,0), 250, 10)

        pygame.display.update()
        clock.tick(60)

def main_menu():
    user_name = get_user_name()
    while True:
        screen.fill((100, 100, 100))
        btn_play = Button("PLAY", 100, 150, 200, 50)
        btn_leader = Button("LEADERBOARD", 100, 220, 200, 50)
        btn_settings = Button("SETTINGS", 100, 290, 200, 50)
        btn_quit = Button("QUIT", 100, 360, 200, 50)

        for btn in [btn_play, btn_leader, btn_settings, btn_quit]:
            btn.draw(screen, font)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn_play.is_clicked(pos):
                    res, s, d = game_loop(user_name)
                    # После игры можно показать Game Over (упрощено)
                if btn_leader.is_clicked(pos): show_leaderboard()
                if btn_settings.is_clicked(pos): show_settings()
                if btn_quit.is_clicked(pos): pygame.quit(); sys.exit()
        
        pygame.display.update()

def show_leaderboard():
    waiting = True
    while waiting:
        screen.fill((30, 30, 30))
        draw_text(screen, "TOP 10 RACERS", big_font, (255, 215, 0), 50, 30)
        scores = get_leaderboard()
        for i, entry in enumerate(scores):
            txt = f"{i+1}. {entry['name']} - {entry['score']} pts"
            draw_text(screen, txt, font, (255,255,255), 50, 100 + i*30)
        
        btn_back = Button("BACK", 150, 500, 100, 40)
        btn_back.draw(screen, font)
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and btn_back.is_clicked(event.pos):
                waiting = False
        pygame.display.update()

def show_settings():
    s = get_settings()
    waiting = True
    while waiting:
        screen.fill((50, 50, 50))
        btn_diff = Button(f"Diff: {s['difficulty']}", 100, 150, 200, 50)
        btn_back = Button("SAVE & BACK", 100, 400, 200, 50)
        
        btn_diff.draw(screen, font)
        btn_back.draw(screen, font)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_diff.is_clicked(event.pos):
                    s['difficulty'] = "Hard" if s['difficulty'] == "Medium" else "Medium"
                if btn_back.is_clicked(event.pos):
                    save_settings(s)
                    waiting = False
        pygame.display.update()

if __name__ == "__main__":
    main_menu()