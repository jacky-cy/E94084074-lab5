import pygame
import os


class UpgradeMenu:
    def __init__(self, x, y):
        
        #從檔案載入三個圖像(upgrade_menu.png)
        self.upgrade_menu_images = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade_menu.png")), (200, 200))   
        self.sell_images = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")), (40, 40))
        self.upgrade_images = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")), (60, 40))
        #設定(self.upgrade_menu_images)圖像的各個數值
        #然後更改其中心點為(x, y)
        self.rect_upgrade_menu_images= self.upgrade_menu_images.get_rect()
        self.rect_upgrade_menu_images.center = (x, y)
        #設定(self.upgrade_images)圖像的各個數值
        #然後更改其中心點為(x, y)
        self.rect_upgrade_images= self.upgrade_images.get_rect()
        self.rect_upgrade_images.center = (x, y-70)
        #設定(self.sell_images)圖像的各個數值
        #然後更改其中心點為(x, y)
        self.rect_sell_images= self.sell_images.get_rect()
        self.rect_sell_images.center = (x, y+75)
        #將 self.__buttons注入兩個Buttons()的屬性
        self.__buttons = [Button(self.upgrade_images, "upgrade",  self.rect_upgrade_menu_images.centerx,  self.rect_upgrade_menu_images.centery-70),
                         Button(self.sell_images, "sell",  self.rect_upgrade_menu_images.centerx, self.rect_upgrade_menu_images.centery+75)]  # (Q2) Add buttons here
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is called in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.upgrade_menu_images, self.rect_upgrade_menu_images)       #利用 win.blit(images, images_rect)   可以輸出設定好位置的圖片
        # draw button
        win.blit(self.upgrade_images, self.rect_upgrade_images)
        win.blit(self.sell_images, self.rect_sell_images)
        
        # (Q2) Draw buttons here
        return None

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons                                                  #直接回傳self.__buttons出來(各個按鈕屬性)


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)      
        :param x: mouse x
        :param y: mouse y
        :return: bool 
        """                                                                  #利用__init__先設定好其按鈕的圖片中心位置self.rect.center=(x,y)
        return True if self.rect.collidepoint(x, y) else False               #再利用self.rect.collidepoint(x, y)偵測是否在這個圖片中，若是則回傳True，反之則False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name                                                     #回傳botton的名字






