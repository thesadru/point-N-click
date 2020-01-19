import pygame,sys,os,random,time
pygame.init()
from pointNclick.objects import Main
from locations import farm

def main():
    """ the mainloop, where everything is done """

    main = Main(60, (1440, 900),farm)
    print("starting mainloop")
    while main.mainloop:
        main.loopStart(False)
        
        main.events()
        main.DoKeys()
        
        # main.delayPrint(True," | ")
        print("\n")

        main.draw()

    sys.exit()
    pygame.quit()

if __name__ == "__main__":
    main()