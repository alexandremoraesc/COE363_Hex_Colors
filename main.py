import pygame as p
import sys
import SpeechRecognition

def main():
    red,blue,green = 100,100,100
    p.init()
    running = True
    clock = p.time.Clock()
    screen = p.display.set_mode((512,512))
    screen.fill(p.Color(red,green,blue))

    while running:
        clock.tick(30)
        p.display.flip()

        for event in p.event.get():
            if event.type == p.KEYDOWN:
                if event.key == p.K_1:

                    # red += 10
                    # screen.fill(p.Color(red,green,blue))

            elif event.type == p.QUIT:
                p.quit()
                sys.exit()


main()
