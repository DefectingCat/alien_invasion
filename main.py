import sys
import pygame


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """ 初始化游戏并创建游戏资源 """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ 开始游戏的主循环 """
        while True:
            # 监听鼠标键盘事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            # 渲染屏幕
            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()