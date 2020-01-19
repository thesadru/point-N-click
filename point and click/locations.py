import pygame
from sounds import *
from pointNclick.location_objects import Location,Object

def loadify(path,resolution):
    image = pygame.image.load(path)
    pygame.transform.scale(image,resolution)
    return image

def _Object(hitbox,image,event,itemevent=None):
    return Object(
        hitbox,
        hitbox,
        False if image == False else loadify("res/objects/"+image+".png",(hitbox[2],hitbox[3])),
        event,
        itemevent
    )

backpack = Object(
    (1440-256,0,256,512),
    (0,0,0,0),
    loadify("res/objects/backpack.png",(256,512)),
    (None,None)
)

locked_home_door = _Object(
    (440,680,60,120),
    "door_2",
    ("talk",door_knock),
)
locked_basement_door = _Object(
    (161,685,60,120),
    "door_2",
    ("talk",locked_door),
    ("key_1","use","unlock_basement_door")
)
unlocked_basement_door = _Object(
    (388,550,60,120),
    "door_1",
    ("move",2),
)
basement_door_fromInside = _Object(
    (388,550,60,120),
    False,
    ("move",1)
)
bull = _Object(
    (1000,590,128,128),
    "bull_1",
    ("talk",bull_sounds)
)
coin = _Object(
    (388,550,64,64),
    "coin_1",
    ("use","grab_coin")
)
key = _Object(
    (750,750,64,64),
    "key_1",
    ("use","grab_key")
)
bag = _Object(
    (388,550,64,64),
    "bag_1",
    ("use","grab_bag")
)
girl = _Object(
    (1200,550,128,256),
    "girl_1",
    ("talk",interact_girl)
)
neutral_man = _Object(
    (900,550,128,256),
    "neutral_man_1",
    ("talk",interact_man)
)



farm = Location(
    1,
    [backpack,locked_home_door,locked_basement_door,bull,key,girl,neutral_man],
    loadify("res/locations/farm_1.png",(1440,900)),
)

garage = Location(
    2,
    [backpack,basement_door_fromInside,coin,bag],
    loadify("res/locations/garage_1.png",(1440,900)),
)