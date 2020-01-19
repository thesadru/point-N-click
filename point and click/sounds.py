import pygame
pygame.mixer.init()

def sound(sound):
    return pygame.mixer.Sound('res/sounds/'+sound+'.wav')

bull_sounds = sound('bull_sounds')
door_knock = sound('door_knock')
interact_girl = sound('interact_girl')
interact_man = sound('interact_man')
locked_door = sound('locked_door')