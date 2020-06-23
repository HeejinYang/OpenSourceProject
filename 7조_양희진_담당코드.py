# class Boss 작성자: 양희진
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.y = 100
        self.speed = 7
        self.Ydirection = 0
        self.Xdirection = 0
        self.HP = 100
        self.last_shot = pygame.time.get_ticks()
        self.shot_delay = 2000

    def update(self):
        if self.Xdirection == 0:
            self.rect.x += self.speed
            if self.rect.right >= WIDTH:
                self.Xdirection = 1
        if self.Xdirection == 1:
            self.rect.left -= self.speed
            if self.rect.x < 0:
                self.Xdirection = 0
        if self.HP < 0:
            self.kill()

        if now - self.last_shot > self.shot_delay:
            self.last_shot = now
            boss_bullet = Boss_Bullet(self.rect.x, self.rect.bottom)
            all_sprites.add(boss_bullet)
            boss_bullets.add(boss_bullet)

# class Boss_Bullet 작성자: 양희진
class Boss_Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_shot
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.top = y + 5

    def update(self):
        self.rect.y += 7
        if self.rect.y < 0:
            self.kill()

# def draw_HP 작성자: 양희진
def draw_HP(surf, x, y, HP, color):
    HP = max(HP, 0)
    fill = (HP / 100) * shieldWIDHT
    outline_rect = pygame.Rect(x, y, shieldWIDHT, shieldHEIGHT)
    fill_rect = pygame.Rect(x, y, fill, shieldHEIGHT)
    pygame.draw.rect(surf, color, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 2)

# def draw_text 작성자: 양희진
def draw_text(surf, text, size, x, y, color):
    if color == BLACK:
        font = pygame.font.Font(font_name, size)
    if color == WHITE:
        font = pygame.font.Font(font_name, size + 2)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# def manual 작성자: 양희진
def manual():
    global screen
    manual_img = manual_img1
    page = 1
    screen.blit(manual_img, (0, 0))
    draw_button(b_main, 0, 600)
    b_main_rect = b_main.get_rect()

    draw_button(b_Rarrow, WIDTH - 100, 600)
    b_Rarrow_rect = b_Rarrow.get_rect()
    draw_button(b_Larrow, 50, 600)
    b_Larrow_rect = b_Larrow.get_rect()

    pygame.display.update()

    while True:
        if page == 1: manual_img = manual_img1
        elif page == 2: manual_img = manual_img2
        elif page == 3: manual_img = manual_img3

        screen.blit(manual_img, (0, 0))
        draw_button(b_main, 0, 600)
        draw_button(b_Rarrow, WIDTH - 100, 600)
        draw_button(b_Larrow, 50, 600)

        if pygame.mouse.get_pressed()[0]: #마우스 왼쪽 버튼 클릭
            mouse_pos = pygame.mouse.get_pos()
            if collide(mouse_pos[0], mouse_pos[1], b_main_rect, 600) == True:
                return 1
            if collideXY(mouse_pos[0], mouse_pos[1], b_Rarrow_rect, WIDTH - 100, 600) == True:
                page += 1
                if page >= 3:
                    page = 3
            if collideXY(mouse_pos[0], mouse_pos[1], b_Larrow_rect, 50, 600) == True:
                page -= 1
                if page <= 1:
                    page = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()
        clock.tick(10)

# def nextlevel 작성자: 양희진
def nextlevel(time, level):
    global screen

    screen.blit(nextlevel_img, (0, 0))
    draw_text(screen, str(level + 1), 70, WIDTH / 2, 200, BLACK)
    pygame.display.update()

    while True:
        now = pygame.time.get_ticks()
        if time + 2000 <= now:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
