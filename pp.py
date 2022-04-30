from pygame import *
from random import randint
 
#фоновая музыка
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#shot = mixer.Sound('fire.ogg')
 
#шрифты и надписи
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)
 
# нам нужны такие картинки:
#img_back = "galaxy.jpg" # фон игры
#img_hero = "rocket.png" # герой
#img_bullet = "bullet.png" # пуля
#img_enemy = "ufo.png" # враг
 

 
# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
 
# класс спрайта-врага   

 
# класс спрайта-пули   

 
# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('fon.jpg'), (win_width, win_height))
 
# создаем спрайты
rok1 = Player('rok.jpg', 20, 100, 80, 100, 10)
rok2 = Player('rok.jpg', 600, 100, 80, 100, 10) 
ball = GameSprite('mach.png', 250, 350, 30, 30, 10)
 

 
# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия на пробел - спрайт стреляет
        
 
    if not finish:
        # обновляем фон
        window.blit(background,(0,0))
 
        # производим движения спрайтов
        rok1.update_l()
        rok2.update_r()
       
 
        # обновляем их в новом местоположении при каждой итерации цикла
        rok1.reset()
        rok2.reset()
        ball.reset()
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
