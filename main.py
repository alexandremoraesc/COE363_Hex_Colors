import pygame as p
import sys
import record as mic
import SpeechRecognition as SR
import os
import RGB
import random
import time 

HEIGHT, WIDTH = 512,512
recognizer = SR.SpeechReconizer("labels.txt", 1.5, 5)

def notRecognized():
    print("Not recognized")
    pass

def recognizeCallBack2(label, currentMinDist):
    print(label, currentMinDist)
    if label in ["Vermelho", "Azul", "Verde"]:
        if len(RGB.listened) == 0:
            RGB.listened.append(label)
        else:
            RGB.listened = [label]
    elif label == "Troca":
        if len(RGB.listened) != 1:
            RGB.data['Azul'] = random.randint(0,255)
            RGB.data['Vermelho'] = random.randint(0,255)
            RGB.data['Verde'] = random.randint(0,255)
        else:
            RGB.data[RGB.listened[0]] = random.randint(0,255)
    elif label == "Mais":
        if len(RGB.listened) > 0:
            if RGB.data[RGB.listened[0]]+25 > 255:
                RGB.data[RGB.listened[0]] = 255
            else:
                RGB.data[RGB.listened[0]]+=25
            RGB.listened = []
    else:
        if len(RGB.listened) > 0:
            RGB.listened.append(label)

recognizer.attachDefaultCallback(recognizeCallBack2)
recognizer.attachFailedCallback(notRecognized)

def main():
    p.init()
    running = True
    clock = p.time.Clock()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    smallfont = p.font.SysFont('Corbel',28)
    gravar = smallfont.render('Gravando...' , True , (170,0,0))

    while running:
        clock.tick(30)
        p.display.flip()
        if len(RGB.listened) == 4:
            if(int(RGB.listened[1]+RGB.listened[2]+RGB.listened[3]) <= 255):
                RGB.data[RGB.listened[0]] = int(RGB.listened[1]+RGB.listened[2]+RGB.listened[3])
            else:
                RGB.data[RGB.listened[0]] = 255
            RGB.listened = []
        screen.fill(p.Color(RGB.data['Vermelho'],RGB.data['Verde'],RGB.data['Azul']))
        listened = smallfont.render(str(RGB.listened) , True ,  (255,255,255))
        screen.blit(listened , (WIDTH/2-60,31*HEIGHT/100))
        vermelho = smallfont.render(str(RGB.data['Vermelho']) , True , (255,255,255))
        azul = smallfont.render(str(RGB.data['Azul']) , True ,  (255,255,255))
        verde = smallfont.render(str(RGB.data['Verde']) , True ,  (255,255,255))
        mouse = p.mouse.get_pos()
        p.draw.circle(screen, (0,0,0), (WIDTH/2, 4*HEIGHT/5), 40, 0)
        p.draw.rect(screen,(100,0,0),[WIDTH/4-55,HEIGHT/2,110,30])
        p.draw.rect(screen,(0,100,0),[2*WIDTH/4-55,HEIGHT/2,110,30])
        p.draw.rect(screen,(0,0,100),[3*WIDTH/4-55,HEIGHT/2,110,30])
        if WIDTH/2-25 <= mouse[0] <= WIDTH/2+25 and 4*HEIGHT/5-25 <= mouse[1] <= 4*HEIGHT/5+25:
            p.draw.circle(screen, (170,0,0), (WIDTH/2, 4*HEIGHT/5), 25, 0)
        else:
            p.draw.circle(screen, (255,0,0), (WIDTH/2, 4*HEIGHT/5), 25, 0)
        screen.blit(vermelho , (WIDTH/4-20,HEIGHT/2+5))
        screen.blit(verde , (2*WIDTH/4-20,HEIGHT/2+5))
        screen.blit(azul , (3*WIDTH/4-20,HEIGHT/2+5))

        p.display.update()

        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    pass
            elif event.type == p.QUIT:
                p.quit()
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN:
                if WIDTH/2-25 <= mouse[0] <= WIDTH/2+25 and 4*HEIGHT/5-25 <= mouse[1] <= 4*HEIGHT/5+25:
                    screen.blit(gravar , (WIDTH/2-60,63*HEIGHT/100))
                    p.display.update()
                    time.sleep(1)
                    mic.recordToFile("output.wav")
                    recognizer.recognizeFile("output.wav", True)
                    try:
                        os.remove("output.wav")
                    except OSError:
                        pass


main()
