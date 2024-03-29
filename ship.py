import pygame


class Ship:
    """ 管理飞船 """

    def __init__(self, ai_game):
        """ 初始化飞船并设置其初始位置 """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('assets/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 每艘新飞船都放在屏幕底部正中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 保存飞船位置属性位小数
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitime(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据自身位置信息更新 rect 对象
        self.rect.x = self.x
