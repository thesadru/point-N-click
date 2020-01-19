import pygame
from pointNclick.doEvent import doEvent

class Location(object):
    def __init__(self,location_id,objects,background):
        self.id = location_id
        self.objects = objects
        self.bg = background

class Object(object):
    def __init__(self,rect,hitrect,imagePath,event,itemevent = None):
        """(128,64,50,50),"image.png",
        ("move"/"talk"/"use",5),
        ("key","move"/"talk"/"use",23)/None"""
        
        self.rect = pygame.Rect(rect)
        self.hitrect = pygame.Rect(hitrect)
        if imagePath == None:
            self.image = None
        else:
            self.image = imagePath

        self.event_type = event[0]
        self.action_num = event[1]
        if itemevent != None:
            self.item_require = itemevent[0]
            self.item_event_type = itemevent[1]
            self.item_action_num = itemevent[2]
        else:
            self.item_event_type = None
    def onClick(self):
        return doEvent(self.event_type,self.action_num)
    def onPlace(self,placed_item):
        if self.item_event_type==None:
            return doEvent(None)
        else:
            if placed_item == self.item_require:
                return doEvent(self.item_event_type,self.item_action_num)
            else:
                return doEvent(False,placed_item)