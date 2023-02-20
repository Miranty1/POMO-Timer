import pygame, sys
from button import Button
 
pygame.init()

clock = pygame.time.Clock()
 
WIDTH, HEIGHT = 700, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro Timer")
 
WHITE_BUTTON = pygame.image.load("assets/button.png")
font = pygame.font.Font('assets/pong.ttf',10)
Sfont = pygame.font.Font('assets/pong.ttf',25)
 
FONT = pygame.font.Font("assets/pong.ttf", 120)
timer_text = FONT.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(WIDTH/2, HEIGHT/2-25))

sound_sfx = pygame.mixer.Sound('assets/sound.mp3')
 

START_STOP_BUTTON = Button(image = WHITE_BUTTON, pos = (350, 500), text_input ="START", font = Sfont,   base_color = 'black', hovering_color = 'pink')
POMO_BUTTON = Button(image = WHITE_BUTTON, pos = (WIDTH/2-250, HEIGHT/2-300), text_input ="POMO", font = font,   base_color = 'black', hovering_color = 'pink')
SHORTB_BUTTON = Button(image = WHITE_BUTTON, pos = (WIDTH/2, HEIGHT/2-300), text_input ="SHORT BREAK", font = font,   base_color = 'black', hovering_color = 'pink')
LONGB_BUTTON = Button(image = WHITE_BUTTON, pos = (WIDTH/2+250, HEIGHT/2-300), text_input ="LONG BREAK", font = font,   base_color = 'black', hovering_color = 'pink')

 
POMODORO_LENGTH = 1500# 1500 secs / 25 mins
SHORT_BREAK_LENGTH =300# 300 secs / 5 mins
LONG_BREAK_LENGTH = 900# 900 secs / 15 mins

cycle = 1

current_seconds = POMODORO_LENGTH
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False
 
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.checkForInput(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
            if POMO_BUTTON.checkForInput(pygame.mouse.get_pos()):
                cycle = 0
                print(cycle)
                current_seconds = POMODORO_LENGTH
                started = False
            if SHORTB_BUTTON.checkForInput(pygame.mouse.get_pos()):
                cycle = 1
                print(cycle)
                current_seconds = SHORT_BREAK_LENGTH
                started = False
            if LONGB_BUTTON.checkForInput(pygame.mouse.get_pos()):
                cycle = 4
                print(cycle)
                current_seconds = LONG_BREAK_LENGTH
                started = False
            if started:
                START_STOP_BUTTON.text_input = "STOP"
                START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            else:
                START_STOP_BUTTON.text_input = "START"
                START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1

    
    
    SCREEN.fill('light blue')
    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.changeColor(pygame.mouse.get_pos())
    POMO_BUTTON.update(SCREEN)
    POMO_BUTTON.changeColor(pygame.mouse.get_pos())
    SHORTB_BUTTON.update(SCREEN)
    SHORTB_BUTTON.changeColor(pygame.mouse.get_pos())
    LONGB_BUTTON.update(SCREEN)
    LONGB_BUTTON.changeColor(pygame.mouse.get_pos())


    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    SCREEN.blit(timer_text, timer_text_rect)


    if cycle == 0 and current_seconds <=0:
            sound_sfx.play()
            print(cycle)
            cycle += 1
            started = False
            current_seconds = POMODORO_LENGTH
            START_STOP_BUTTON.text_input = "START"
            START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                                START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
    if cycle == 1 and current_seconds <=0:
        sound_sfx.play()
        print(cycle)
        cycle += 1
        started = False
        current_seconds = SHORT_BREAK_LENGTH
        START_STOP_BUTTON.text_input = "START"
        START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
    if cycle == 2 and current_seconds <= 0:
        sound_sfx.play()
        print(cycle)
        cycle += 1
        started = False
        current_seconds = POMODORO_LENGTH
        START_STOP_BUTTON.text_input = "START"
        START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
    if cycle == 3 and current_seconds <= 0:
        sound_sfx.play()
        print(cycle)
        cycle += 1
        started = False
        current_seconds = SHORT_BREAK_LENGTH
        START_STOP_BUTTON.text_input = "START"
        START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
    if cycle == 4 and current_seconds <= 0:
        sound_sfx.play()
        print(cycle)
        cycle += 1
        started = False
        current_seconds = POMODORO_LENGTH
        START_STOP_BUTTON.text_input = "START"
        START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
    if cycle == 5 and current_seconds <= 0:
        sound_sfx.play()
        print(cycle)
        cycle -= 5
        started = False
        current_seconds = LONG_BREAK_LENGTH
        START_STOP_BUTTON.text_input = "START"
        START_STOP_BUTTON.text = pygame.font.Font("assets/pong.ttf", 20).render(
                                            START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
    

    
        
        
        
    pygame.display.update()
    