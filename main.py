import pygame as p
import sys
import record as mic
import SpeechRecognition as SR
import os
import RGB
import random
import time 
import LISTENED as LISTENED
HEIGHT, WIDTH = 512,512
recognizer = SR.SpeechReconizer("labels.txt", 1.5, 5)

def notRecognized():
    print("Not recognized")
    pass

def recognized(label, currentMinDist):
    print(label,currentMinDist,LISTENED.listened)
    if label == "Vermelho":
        LISTENED.listened = []
        LISTENED.listened.append(label)
        time.sleep(2)
        mic.recordToFile("output_number0.wav")
        recognizer.recognizeFile("output_number0.wav", True)
        os.remove("output_number0.wav")
    elif label == "Verde":
        LISTENED.listened = []
        LISTENED.listened.append(label)
        time.sleep(2)
        mic.recordToFile("output.wav")
        recognizer.recognizeFile("output.wav", True)
        os.remove("output.wav")
    elif label == "Azul":
        LISTENED.listened = []
        LISTENED.listened.append(label)
        time.sleep(2)
        mic.recordToFile("output.wav")
        recognizer.recognizeFile("output.wav", True)
        os.remove("output.wav")

        if RGB.Azul+25 > 255:
            RGB.Azul = 255
        else:
            RGB.Azul+=25
    elif label == "Troca":
        print(LISTENED.listened)
        RGB.Azul = random.randint(0,255)
        RGB.Vermelho = random.randint(0,255)
        RGB.Verde = random.randint(0,255)
    elif label == "Mais":
        if RGB.Azul+25 > 255:
            RGB.Azul = 255
        else:
            RGB.Azul+=25
    pass

recognizer.attachDefaultCallback(recognized)
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
        screen.fill(p.Color(RGB.Vermelho,RGB.Verde,RGB.Azul))
        vermelho = smallfont.render(str(RGB.Vermelho) , True , (255,255,255))
        azul = smallfont.render(str(RGB.Azul) , True ,  (255,255,255))
        verde = smallfont.render(str(RGB.Verde) , True ,  (255,255,255))
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
                    print("Gravando...")
                    screen.blit(gravar , (WIDTH/2-60,63*HEIGHT/100))
                    p.display.update()
                    time.sleep(2)
                    mic.recordToFile("output.wav")
                    recognizer.recognizeFile("output.wav", True)
                    os.remove("output.wav")

main()
