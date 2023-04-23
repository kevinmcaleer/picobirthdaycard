from cake import draw_cake, clear
from buzzer_demo import playsong, happy_birthday
from time import sleep
from machine import Pin
from scroll import *

touch = Pin(0, Pin.IN, Pin.PULL_UP)
scroll = Scroller(matrix)

# scroller demo

from font import font
from time import sleep
import math

class Scroller():
 
    def __init__(self,matrix):
        self.matrix = matrix

    offset = 0
    gap = 1
    hue = 1.0
    saturation = 1.0
    brightness = 1.0
    num_cols = 5
    num_rows = 5

    def hsv2rgb(self, hue, sat, val):
        """ Returns the RGB of Hue Saturation and Brightnes values """
    
        i = math.floor(hue * 6)
        f = hue * 6 - i
        p = val * (1 - sat)
        q = val * (1 - f * sat)
        t = val * (1 - (1 - f) * sat)

        r, g, b = [
            (val, t, p),
            (q, val, p),
            (p, val, t),
            (p, q, val),
            (t, p, val),
            (val, p, q),
        ][int(i % 6)]
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        
        return r, g, b
    
    def rgb2hsv(self, r:int, g:int, b:int):
        """ Returns the Hue Saturation and Value of RGB values """
        h = 0
        s = 0
        v = 0
        # constrain the values to the range 0 to 1
        r_normal, g_normal, b_normal,  = r / 255, g / 255, b / 255
        cmax = max(r_normal, g_normal, b_normal)
        cmin = min(r_normal, g_normal, b_normal)
        delta = cmax - cmin
        
        # Hue calculation
        if(delta ==0):
            h = 0
        elif (cmax == r_normal):
            h = (60 * (((g_normal - b_normal) / delta) % 6))
        elif (cmax == g_normal):
            h = (60 * (((b_normal - r_normal) / delta) + 2))
        elif (cmax == b_normal):
            h = (60 * (((r_normal - g_normal) / delta) + 4))
        
        # Saturation calculation
        if cmax== 0:
            s = 0
        else:
            s = delta / cmax
            
        # Value calculation
        v = cmax

        return h, s, v 
    
    def clear(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self.matrix.set_pixel(col, row, 0, 0, 0)
        
    def display_character(self, character,pos):

        # Convert the hue, saturation, and brightness values to RGB values
        red, green, blue = self.hsv2rgb(self.hue, self.saturation, self.brightness)

        # Initialize y to 0
        y = 0

        # Iterate over each row in the character
        for row_idx in range(0,self.num_rows):
            # Determine the length of the current row
            row_len = len(character[0])
            
            # Iterate over each column in the current row
            for col_idx in range (row_len):
                
                # Determine the x coordinate for the current pixel

                x = row_idx
                y = col_idx + self.offset + pos
                if x >= 0 and x < self.num_cols and y >= 0 and y < self.num_rows:
               
                  
                    if x <= self.num_cols and x >= 0:
                        if character[row_idx][col_idx] == '1':
                            self.matrix.set_pixel(x, y, red, green, blue)
                        else:
                            self.matrix.set_pixel(x, y, 0, 0, 0)
        
        # Update the offset
        self.offset += len(character[0]) + self.gap
        
    def show_message(self, message, position, hue:None):
        """ Shows the message on the display, at the
            position provided, using the Hue value
            specified """
        if hue is None:
            hue = 1.0
        self.hue = hue    
        for character in message:
            self.display_character(font.get(character), position)
        
        # Update the offset
        self.offset = 0
    
scroll = Scroller(matrix)
message = 'Happy Birthday Alex!'


def birthday_message():
    hue = 0
    for position in range(5, -len(message*(5 + 1)), -1):
        if hue <= 1 or hue == 0:
            hue += 0.01
        else: hue = 0
        
        matrix.clear()
        scroll.show_message(message, position, hue)
        matrix.update()
        sleep(0.05)

while True:
    if touch.value() == 1:
        draw_cake()
        playsong(happy_birthday)
        hue = 0
        birthday_message()
        for _ in range(5):
            draw_cake()
            sleep(0.25)
            clear()
            sleep(0.25)
    else:
        pass
    sleep(0.1)
    