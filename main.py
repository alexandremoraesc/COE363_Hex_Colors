import pygame as p
import sys


def main():
    red,blue,green = 100,100,100

    p.init()
    running = True
    clock = p.time.Clock()
    screen = p.display.set_mode((512,512))
    screen.fill(p.Color(red,green,blue))
    width = screen.get_width()
    height = screen.get_height()
    smallfont = p.font.SysFont('Corbel',28)
    gravar = smallfont.render('Gravar' , True , (255,255,255))
    vermelho = smallfont.render(str(red) , True , (255,255,255))
    azul = smallfont.render(str(blue) , True ,  (255,255,255))
    verde = smallfont.render(str(green) , True ,  (255,255,255))


    while running:
        clock.tick(30)
        p.display.flip()
        mouse = p.mouse.get_pos()
        if width/2-100 <= mouse[0] <= width/2+40 and height/3 <= mouse[1] <= height/3+40:
            p.draw.rect(screen,(170,170,170),[width/2-100,height/3,140,30])
        else:
            p.draw.rect(screen,(110,110,110),[width/2-100,height/3,140,30])
        p.draw.rect(screen,(red,0,0),[width/4-50,height/2,140,30])
        p.draw.rect(screen,(0,blue,0),[2*width/4-50,height/2,140,30])
        p.draw.rect(screen,(0,0,green),[3*width/4-50,height/2,140,30])
        screen.blit(gravar , (width/2-100,height/3))
        screen.blit(vermelho , (width/4-50,height/2))
        screen.blit(azul , (2*width/4-50,height/2))
        screen.blit(verde , (3*width/4-50,height/2))

        p.display.update()
        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == p.K_1:
                    pass
                    # red += 10
                    # screen.fill(p.Color(red,green,blue))
            elif event.type == p.QUIT:
                p.quit()
                sys.exit()
            elif event.type == p.MOUSEBUTTONDOWN:
                if width/2-100 <= mouse[0] <= width/2+40 and height/3 <= mouse[1] <= height/3+40:
                    p.quit()
main()
