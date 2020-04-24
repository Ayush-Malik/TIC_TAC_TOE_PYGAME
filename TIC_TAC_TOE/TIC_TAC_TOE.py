import pygame
import time
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((600 , 600))

LIGHT_BLUE = (105 , 105 , 105)
pattern_img = pygame.image.load('TTT.png')

game_over_entry = False
current_CHARACTER = 'o'

counter = 0

x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')


listt = []
for i in range(3):
    listt.append([ '' , '' , '' ])






SCREEN_elements = []


def screen_data_print():
    
    SCREEN.blit(pattern_img , (0 , 0))
    
    for X in range( len(SCREEN_elements)):
        img , x , y = SCREEN_elements[X]
        SCREEN.blit(img , (x , y))

   
   
        
     



    


def INPUT():
    global game_over_entry
    global entry
    global counter
    global tie_entry
    global current_CHARACTER

    
    

    x , y = pygame.mouse.get_pos()



    if x >= 0 and x <= 190 : # x to j
        j = 0
    elif x >= 225 and x<= 380:
        j = 1
    elif x >= 415 and x <= 600:
        j = 2

    if y >= 0 and y <= 190: # y to i
        i = 0
    elif y >= 225 and y <= 380:
        i = 1
    elif y >= 415 and  y <= 600:
        i = 2



    if listt[i][j] != '':
        return

    counter += 1

    # if listt[i][j] != '': # TO avoid overlapping of X AND O
    #     return

    


    listt[i][j] = current_CHARACTER

    

    if current_CHARACTER == 'x':
        current_CHARACTER = 'o'
    else:
        current_CHARACTER = 'x'
  
    # APPENDING IMAGES TO MAIN_PRINTIND_DISPLAY
    if current_CHARACTER == 'x':
        APPEND_CHARACTER = x_img
    else:
        APPEND_CHARACTER = o_img

    SCREEN_elements.append( (APPEND_CHARACTER ,  40 + j * 190 , 40 + i * 190 ) )





    game_over_entry = check_game_over(i , j)

    if counter == 9 and game_over_entry == False:
        entry = False
        tie_entry = True
        screen_data_print()
 

        




    if game_over_entry:
        screen_data_print()
        entry = False



def GAME_OVER_TEXT():



    SCREEN.fill(LIGHT_BLUE)
   
    
    
    


    font = pygame.font.SysFont('comicsansms' , 30)
    over_font = pygame.font.SysFont("comicsansms", 80)
    # over_font = pygame.font.Font('freesansbold.ttf' , 80 )
    over_text_1 = over_font.render("GAME OVER" , True , (0 , 0 , 0))
    over_text_2 = font.render("DEVELOPED BY : AYUSH MALIK" , True  , (0 , 0 , 0))
    SCREEN.blit(over_text_1 , (45 , 250))
    SCREEN.blit(over_text_2 , (80 , 500))
    


def TIE_TEXT():
    SCREEN.fill(LIGHT_BLUE)
    font = pygame.font.SysFont('comicsansms' , 30)
    over_font = pygame.font.SysFont("comicsansms", 80)

    tie_text = over_font.render("GAME TIED" , True , (0 , 0 , 0))
    over_text_2 = font.render("DEVELOPED BY : AYUSH MALIK" , True  , (0 , 0 , 0))
    
    SCREEN.blit(tie_text , (45 , 250))
    SCREEN.blit(over_text_2 , (80 , 500))

    


def check_game_over( i , j):
    if listt[i][0] == listt[i][1] and listt[i][1] == listt[i][2]:
        return True
    elif listt[0][j] == listt[1][j] and listt[1][j] == listt[2][j]:
        return True


    if i == j:
        if listt[0][0] == listt[1][1] and listt[1][1] == listt[2][2]:
            return True
    if i + j == 2:
        if listt[0][2] == listt[1][1] and listt[1][1] == listt[2][0]:
            return True
    
    return False

        

    
    
        


    










exitt = 0
entry = True
CLOSE = False
tie_entry = False
w = False
while True:
 








    if CLOSE:
        break

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            CLOSE = True
        elif event.type == pygame.MOUSEBUTTONUP and entry:
            input_sound = mixer.Sound('input_sound.wav')
            input_sound.play()
            INPUT()
    if tie_entry or game_over_entry:
        for i in range(1000):
            screen_data_print()
        exitt += 1


    if exitt == 2 or w :
        if tie_entry:
            end_sound = mixer.Sound('GAME_OVER.wav')
            end_sound.play()
            TIE_TEXT()
        else:
            end_sound = mixer.Sound('GAME_OVER.wav')
            end_sound.play()
            GAME_OVER_TEXT()
        w = True
        
    if w == False:
        SCREEN.fill(LIGHT_BLUE)
        screen_data_print()
    



   
    pygame.display.update()

