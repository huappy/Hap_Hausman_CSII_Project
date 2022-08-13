import time
from battles import *
import pygame
# from view2 import *

'''music commented out because Pycharm will not run it. Works in Thonny and other IDEs.'''
'''No GUI for text was a design choice. Running the text in the terminal gives it 
more of a retro text-adventure feel'''

pygame.init()


# pygame.mixer.music.load('grieve.mp3')
# pygame.mixer.music.play(-1)


def slow_print(dialogue):
    for char in dialogue:
        print(char, end='')
        time.sleep(.00001)


# TODO: Create a GUI that enacts this in its own window
def main():
    with open('scene_1.txt', 'r', encoding='utf-8') as scene_1:
        for line in scene_1:
            if line.isspace() == True:
                print(line, end='')
            elif line == "<INTRO BATTLE! WOOOO!>\n":
                # pygame.mixer.music.fadeout(5)
                # pygame.mixer.music.unload()
                # pygame.mixer.music.load('Distort3.mp3')
                # pygame.mixer.music.play(-1)
                
                rove_combat(alex, rove)
                
                # pygame.mixer.music.fadeout(5)
                # pygame.mixer.music.unload()
                # pygame.mixer.music.load('grieve.mp3')
                # pygame.mixer.music.play(-1)
                
            elif line == "<READY? GO!>\n":
                # pygame.mixer.music.fadeout(5)
                # pygame.mixer.music.unload()
                # pygame.mixer.music.load('gone_feral_take_2.mp3')
                # pygame.mixer.music.play(-1)
                
                cultist_combat(alex, cultist)
                
                # pygame.mixer.music.fadeout(5)
                # pygame.mixer.music.unload()
                # pygame.mixer.music.load('grieve.mp3')
                # pygame.mixer.music.play(-1)
                
            else:
                print(line)
                input()


if __name__ == "__main__":
    main()
