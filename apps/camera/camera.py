#Call App
#copyright (c) 2015 Tyler Spadgenske
#GPL License
###############################
#To be packaged with stock TYOS
###############################

from subprocess import Popen
import sys
import pygame

class Run():
    def __init__(self, fona):
        #Stuff to follow app protocol
        self.exit = False
        self.blit_one_surface = {'surface':[], 'rects':[]}
        self.blit = {'surfaces':[], 'rects':[]}

    def run_app(self):
        cam = Popen(['sudo', 'python', '/home/pi/adafruit-pi-cam/cam.py'])
        pygame.quit()
        sys.exit()
        
    def get_events(self, event):
        pass
