import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船发射子弹的类"""

    def __init__(self, ai_game):
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0,0)的位置创建一个子弹的矩形，并设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_width)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 使用浮点数存储子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新表示子弹的小数值
        self.y -= self.settings.bullet_speed
        # 更新子弹矩形位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上位置子弹矩形"""
        pygame.draw.rect(self.screen, self.color, self.rect)
