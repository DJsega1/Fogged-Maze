import pygame
from sprites import *


# Класс эффектов
class Buff(Sprite):
    def __init__(self, x, y, SPRITES_WIDTH, SPRITES_HEIGHT, player, pic):
        super().__init__(buffs)
        self.image = pygame.transform.scale(pygame.image.load(f"assets\\{pic}.png"),
                                            (SPRITES_WIDTH, SPRITES_HEIGHT))
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH // 2 - self.rect.width // 2 + (x * SPRITES_WIDTH - player.x),
                             HEIGHT // 2 - self.rect.height // 2 + (y * SPRITES_HEIGHT - player.y))

    def update(self):
        pass


# Яркая лампа
class LanternBuff(Buff):
    def update(self):
        if pygame.sprite.spritecollideany(self, user):
            pygame.mixer.Sound("assets\\buff.ogg").play()
            self.player.mp += 2
            self.kill()


# Удобные сапоги
class BootsBuff(Buff):
    def update(self):
        if pygame.sprite.spritecollideany(self, user):
            pygame.mixer.Sound("assets\\buff.ogg").play()
            self.player.speed += 5
            self.kill()


class Exit(Buff):
    def update(self):
        if pygame.sprite.spritecollideany(self, user):
            self.player.escaped = True


buffs = SpriteGroup()
