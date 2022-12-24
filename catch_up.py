from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
window.display.set_capshen('Догонялки')
begraud = transform.scale(image.load("background.png"), (700, 500))

Clock = time.Clock()

sprite1 = transform.scale(image.load("background.png"), (100, 100))
sprite2 = transform.scale(image.load("background.png"), (100,100))

x1 = 100
y1 = 200

x2 = 400
y2 = 400
#задай фон сцены

#создай 2 спрайта и размести их на сцене

#обработай событие «клик по кнопке "Закрыть окно"»
game = True
while game:

    window.blit(begraud(0, 0))
    window.blit(sprite1(x1, y1))
    window.blit(sprite2(x2, y2))

    keys_preeset = key.get_presse()

    if keys_preeset[K_up] and x1 > 0:
        x1 -=5
    if keys_preeset[K_down] and x1 > 0:
        x1 -= 5
    if keys_preeset[K_Left] and x1 > 0:
        x1 -= 5
    if keys_preeset[K_Right] and x1 > 0:
        x1 -= 5
