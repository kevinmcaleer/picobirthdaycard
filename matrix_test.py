from pimoroni_i2c import PimoroniI2C
from breakout_rgbmatrix5x5 import BreakoutRGBMatrix5x5
from time import sleep
from font import font

PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}
i2c = PimoroniI2C(**PINS_PICO_EXPLORER)
matrix = BreakoutRGBMatrix5x5(i2c)

matrix.clear()
matrix.update()
matrix.set_pixel(0,0,255,255,255)
matrix.update()