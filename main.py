import pygame as p
import sys
import record as mic
import SpeechRecognition as SR
import os
import RGB


recognizer = SR.SpeechReconizer("labels.txt", 1.5, 5, 5)

def notRecognized():
    print("Not recognized")
    pass

def recognized(label, currentMinDist):
    if label == "Vermelho":
        RGB.red += 10
        print(RGB.red)
    print(currentMinDist)
    pass

recognizer.attachDefaultCallback(recognized)
recognizer.attachFailedCallback(notRecognized)

def main():
    p.init()
    running = True
    clock = p.time.Clock()
    screen = p.display.set_mode((512,512))
    screen.fill(p.Color(RGB.red,RGB.green,RGB.blue))
    width = screen.get_width()
    height = screen.get_height()
    smallfont = p.font.SysFont('Corbel',28)
    gravar = smallfont.render('Gravar' , True , (255,255,255))
    vermelho = smallfont.render(str(RGB.red) , True , (255,255,255))
    azul = smallfont.render(str(RGB.blue) , True ,  (255,255,255))
    verde = smallfont.render(str(RGB.green) , True ,  (255,255,255))


    while running:
        screen.fill(p.Color(RGB.red,RGB.green,RGB.blue))
        clock.tick(30)
        p.display.flip()
        mouse = p.mouse.get_pos()
        if width/2-100 <= mouse[0] <= width/2+40 and height/3 <= mouse[1] <= height/3+40:
            p.draw.rect(screen,(170,170,170),[width/2-100,height/3,140,30])
        else:
            p.draw.rect(screen,(110,110,110),[width/2-100,height/3,140,30])
        p.draw.rect(screen,(RGB.red,0,0),[width/4-50,height/2,140,30])
        p.draw.rect(screen,(0,RGB.blue,0),[2*width/4-50,height/2,140,30])
        p.draw.rect(screen,(0,0,RGB.green),[3*width/4-50,height/2,140,30])
        screen.blit(gravar , (width/2-100,height/3))
        screen.blit(vermelho , (width/4-50,height/2))
        screen.blit(azul , (2*width/4-50,height/2))
        screen.blit(verde , (3*width/4-50,height/2))
        

        p.display.update()
        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    pass

                    # RGB.red += 10
                    # screen.fill(p.Color(RGB.red,RGB.green,RGB.blue))
            elif event.type == p.QUIT:
                p.quit()
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN:
                if width/2-100 <= mouse[0] <= width/2+40 and height/3 <= mouse[1] <= height/3+40:
                    print("Gravando")
                    mic.recordToFile("output.wav")
                    recognizer.recognizeFile("output.wav", True)
                    os.remove("output.wav")
main()
