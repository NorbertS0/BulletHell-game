# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:34:51 2021

@author: norbe

module for handling keyboard controls of game
"""

import keyboard # using module keyboard

class KeyInput:
    #keyMap is a dict to support remapping controlls
    def __init__(self, keyMap):
        self.keyMap = keyMap
        self.Exit = False

    #detect when certain keys are pressed
    #returns set of keys (strings)
    def detect(self):
        pressed = set()
        for k in self.keyMap.keys():
            if keyboard.is_pressed(k):
                pressed.add(self.keyMap[k])
        return pressed
    
    #for rebinding, just changes the dictionary key
    #swapkeys is a pair tuple (originalKey, newKey)
    #returns true is successful
    #false if can't rebind due to that key already being in use
    def remap(self, originalKey, newKey):
        if newKey in self.keyMap.keys():
            return False
        self.keyMap[newKey] = self.keyMap.pop(originalKey)
        return True

#for testing, bewere inf loopt
if __name__ == '__main__':
    k = KeyInput({'a':'LEFT','s':'DOWN','d':'RIGHT','w':'UP'})
    print(k.remap('a', 's'))
    print(k.keyMap)
    print(k.remap('a', 't'))
    print(k.keyMap)
    # while True:
    #     print(k.detect())
        