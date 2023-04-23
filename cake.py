from pimoroni_i2c import PimoroniI2C
from breakout_rgbmatrix5x5 import BreakoutRGBMatrix5x5
from time import sleep

PINS_PICO_EXPLORER = {"sda": 2, "scl": 3}
i2c = PimoroniI2C(**PINS_PICO_EXPLORER)
matrix = BreakoutRGBMatrix5x5(i2c)

cake = ["Y Y Y",
        "W W W",
        "WWWWW",
        "RRRRR",
        "WWWWW"]

def draw_cake():
    r = g = b = 0
    row = 0
    for cake_row in cake:
        col = 0
        for color in cake_row:
            if color == "Y":
                r = 255
                g = 255
                b = 0
            if color == "W":
                r = 255
                g = 255
                b = 255
            if color == " ":
                r = 0
                g = 0
                b = 0
            if color == "R":
                r = 255
                g = 64
                b = 64
            
            matrix.set_pixel(row, col, r, g, b)
            
            col +=1
        row += 1
        matrix.update()
    
def clear():
    matrix.clear()
    matrix.update()

if __name__ == "__main__":
    draw_cake()
    sleep(1)
    clear()