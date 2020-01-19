import pygame,time,random
from pygame.locals import *
from locations import *


class Main(object):
    # basic variables
    def __init__(self, fps, window_size, location):
        self.fpsClock = pygame.time.Clock()
        self.mainloop = True
        self.keys = (0)*323
        self.fps = fps
        self.delay = 0
        self.last_time = time.time()-1
        self.loop = -1
        self.location = location
        self.last_change = location
        self.f3 = False
        if type(window_size) == tuple:
            self.width = window_size[0]
            self.height = window_size[1]
            self.window_size = window_size
        else:
            self.width = window_size
            self.height = window_size
            self.window_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.window_size)

    # draw on the screen
    def draw(self):
        def blitStr(string):
            return pygame.font.SysFont('sansbold', 32).render(string,True,(0,0,0))

        self.screen.blit(self.location.bg,(0,0))

        transparent = pygame.transform.scale(pygame.image.load("res/objects/False.png"),(1,1))
        for obj in self.location.objects:
            if obj.image == None:
                self.screen.blit(transparent,obj.rect.topleft)
            else:
                self.screen.blit(obj.image,obj.rect.topleft)

        if self.f3:
            self.screen.blit(
                blitStr(    'fps: '+self.trueFps()
                        if self.fps==None else
                            'fps: '+self.trueFps()+' / '+str(self.fps)),
                pygame.Rect(0,32*0,1,1))
            self.screen.blit(
                blitStr('pos: '+str(pygame.mouse.get_pos())),
                pygame.Rect(0,32*1,1,1))
            self.screen.blit(
                blitStr('location: '+str(self.location.id)),
                pygame.Rect(0,32*2,1,1))

        
        

        pygame.display.flip()


        

    # prints out the loop or the delay between frames
    def loopStart(self,printing=False,printend="\n"):
        if self.fps != None:
            self.fpsClock.tick(self.fps)
        self.loop += 1
        if printing:
            print(self.loop,end=printend)
        self.trueFps()

    def delayPrint(self,round,printend="\n"):
        try:
            if round:
                print(str(time.time() - self.last_time)[:7],end=printend)
            else:
                print(str(time.time() - self.last_time),end=printend)
            self.last_time = time.time()
        except:
            print("   0   ")
        try:
            print(str(1/main.fps)[:7])
        except:
            print("inf")
    
    def trueFps(self):
        try:
            output = str(int(1/(time.time() - self.last_time)))
        except ZeroDivisionError:
            output = 'inf'
        self.last_time = time.time()
        return output

    def events(self):
        def test_quit(event):
            if event.type == QUIT:
                self.mainloop = False

        def test_objects(event):
            def pickup(self):
                outcomes = {
                    ("use","grab_key"):Object(
                        (1184,0,128,128),
                        (1184,0,128,128),
                        pygame.transform.scale(pygame.image.load("res/objects/key_1.png"),(128,128)),
                        ("grab","key")),
                }
                if doing in outcomes:
                    self.location.objects.remove(obj)
                    self.location.objects.append(outcomes[doing])

            def grabbing(self):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:            
                        if obj.hitrect.collidepoint(event.pos):
                            self.object_draging = True
                            self.mouse_x, self.mouse_y = event.pos
                            self.offset_x = obj.rect.x - self.mouse_x
                            self.offset_y = obj.rect.y - self.mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:            
                        self.object_draging = False

                elif event.type == pygame.MOUSEMOTION:
                    if self.object_draging:
                        self.mouse_x, self.mouse_y = event.pos
                        obj.rect = pygame.Rect(
                            self.mouse_x+self.offset_x,self.mouse_y+self.offset_y,obj.rect.width,obj.rect.height
                        )
########################################################################################################################
            def dropping(self):
                if self.action == "key":
                    print("not holding")
                    try:
                        self.placed_on_door
                    except:
                        self.placed_on_door = False
                    if self.placed_on_door:
                        self.location.objects.remove(locked_basement_door)
                        self.location.objects.remove(key)
                        self.location.objects.append(unlocked_basement_door)
                    else:
                        obj.rect = pygame.Rect(
                            obj.rect.left,obj.rect.top,obj.rect.width,obj.rect.height
                        )

            pos = pygame.mouse.get_pos()
            for obj in self.location.objects:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if obj.hitrect.collidepoint(pos) or self.object_draging:
                        self.outcome,self.action = obj.onClick()
                        doing = (self.outcome,self.action)
                        print(obj.event_type,obj.action_num)
                        pickup(self)

                        if self.outcome == "grab":
                            grabbing(self)

                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    print("MOUSEBUTTONUP")
                    dropping(self)

        for event in pygame.event.get():
            test_quit(event)
            test_objects(event)


    def DoKeys(self):
        def key_F3(self, boolean):
            try:
                self.f3
                self.holdingF3
            except AttributeError:
                self.f3 = False
                self.holdingF3 = False

            if boolean and not self.holdingF3 and not self.f3:
                self.f3 = True
                self.holdingF3 = True
            elif boolean and not self.holdingF3 and self.f3:
                self.f3 = False
                self.holdingF3 = True
            elif not boolean and self.holdingF3:
                self.holdingF3 = False
        def key_F11(self, boolean):
            try:
                self.f11
                self.holdingF11
            except AttributeError:
                self.f11 = False
                self.holdingF11 = False

            if boolean and not self.holdingF11 and not self.f11:
                self.f11 = True
                self.screen = pygame.display.set_mode((self.width, self.height), FULLSCREEN)
                self.holdingF11 = True
            elif boolean and not self.holdingF11 and self.f11:
                self.f11 = False
                self.screen = pygame.display.set_mode((self.width//2, self.height//2))
                self.holdingF11 = True
            elif not boolean and self.holdingF11:
                self.holdingF11 = False

        def key_ESC(self, boolean):
            if boolean:
                self.mainloop=False
        
        def key_BACKQUOTE(self, boolean):
            if boolean:
                pygame.mixer.pause()
            else:
                pygame.mixer.unpause()
        self.keys = pygame.key.get_pressed()
        key_F3(self,self.keys[K_F3])
        key_F11(self,self.keys[K_F11])
        key_ESC(self,self.keys[K_ESCAPE])
        key_BACKQUOTE(self,self.keys[K_BACKQUOTE])