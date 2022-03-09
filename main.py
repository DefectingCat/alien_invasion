import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """ 开始游戏的主循环 """
        while True:
            self._check_event()
            # 更新飞船
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 渲染屏幕
        pygame.display.flip()

    def _check_event(self):
        """响应按键和鼠标事件"""
        # 监听鼠标键盘事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入到编组 bullets 中"""
        if len(self.bullets) < self.settings.bullet_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


if __name__ == '__main__':
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
