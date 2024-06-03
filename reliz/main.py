import pygame
import random

pygame.init()

class Card:
    def __init__(self, x, y, width, height, back_color, pered_color, text):
        self.back_rect = pygame.Rect(x, y, width, height)
        self.back_color = back_color
        self.pered_rect = pygame.Rect(x + width * 0.1, y + height * 0.1, width * 0.8, height * 0.8)
        self.pered_color = pered_color
        self.font = pygame.font.SysFont(None, 24)
        self.change_text(text)

    def draw(self, window):
        pygame.draw.rect(window, self.back_color, self.back_rect)
        pygame.draw.rect(window, self.pered_color, self.pered_rect)
        text_rect = self.text.get_rect(center=self.pered_rect.center)
        window.blit(self.text, text_rect)

    def change_text(self, text):
        self.t = text
        self.text = self.font.render(text, True, (0, 0, 0))

countries = [
    "Який популярний спорт в Україні?", 
    "Вид спорту в якому потрібно закидувати мяч в кільце?",
    "Вид спорту в якому на полі можуть перебувати одночасно 6 гравців ?", 
    "Який популярний вид спорту в США?",
    "Вид спорту в якому потрібно забивати мяч в лунку?", 
    "Вид спорту в якому гравці грають через сітку? ",
    "Який вид спорту відноситься до бойових мистецтв?", 
    "Який популярний вид спорту в Канаді?",
    "У якому виді спорту Україна здобула першу золоту медаль?", 
    "В якому виді спорту на полі грають 12 гравців?",
    "Яким видом спорту займається спортсмен Роман Романчук?", 
    "Який популярний вид спорту в Японії?"
]

capitals = [
    "футбол", 
    "баскетбол", 
    "волейбол", 
    "американський футбол", 
    "гольф", "волейбол", 
    "бокс", 
    "хокей", 
    "фігурне катання", 
    "футбол", 
    "плавання", 
    "бейсбол"
]

window = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()
pygame.font.init()

card1 = Card(25, 200, 450, 50, (255, 0, 0), (255, 255, 255), "клікай")
card2 = Card(25, 270, 450, 50, (255, 0, 0), (255, 255, 255), "клікай")
card3 = Card(25, 340, 450, 50, (255, 0, 0), (255, 255, 255), "клікай")
card4 = Card(25, 410, 450, 50, (255, 0, 0), (255, 255, 255), "клікай")
cards = [card1, card2, card3, card4]

scoro = 0
scoro_text = pygame.font.SysFont(None, 49).render("Rahunok :" + str(scoro), True, (255, 255, 255))
loose_text = pygame.font.SysFont(None, 40).render("Ти програв", True, (0, 0, 0))
win_text = pygame.font.SysFont(None, 40).render("Ти виграв і набрав потрібну кількість балів", True, (0, 0, 0))

a = 0
unique_numbers = set()
unique_numbers.add(a)
while len(unique_numbers) < 4:
    unique_numbers.add(random.randint(0, len(capitals) - 1))

num1, num2, num3, num4 = unique_numbers
cards[0].change_text(capitals[num1])
cards[1].change_text(capitals[num2])
cards[2].change_text(capitals[num3])
cards[3].change_text(capitals[num4])

game = True
while game:
    if scoro <= -1:
        window.fill((0, 0, 255))
        window.blit(loose_text, ([200, 200]))
        pygame.display.flip()
        break
    if scoro >= 23:
        window.fill([0, 0, 255])
        window.blit(win_text, (200, 200))
        pygame.display.flip()
        break

    window.fill((0, 255, 0))
    scoro_text = pygame.font.SysFont(None, 49).render("Rahunok: " + str(scoro), True, (255, 255, 255))
    window.blit(scoro_text, (150, 100))
    if a < len(countries):
        window.blit(pygame.font.SysFont(None, 24).render(countries[a], True, (0, 0, 0)), (20, 50))
    for card in cards:
        card.draw(window)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(len(cards)):
                if cards[i].pered_rect.collidepoint(x, y):
                    if a < len(capitals) and cards[i].t == capitals[a]:
                        scoro += 1
                    else:
                        scoro -= 1
                    a += 1
                    if a == len(capitals):
                        if scoro > 20:
                            print("Ти виграв")
                            game = False
                            break
                    if a < len(countries):
                        unique_numbers = set()
                        unique_numbers.add(a)
                        while len(unique_numbers) < 4:
                            unique_numbers.add(random.randint(0, len(capitals) - 1))

                        num1, num2, num3, num4 = unique_numbers
                        cards[0].change_text(capitals[num1])
                        cards[1].change_text(capitals[num2])
                        cards[2].change_text(capitals[num3])
                        cards[3].change_text(capitals[num4])
                        random.shuffle(cards)
                    break

    fps.tick(60)
pygame.quit()
