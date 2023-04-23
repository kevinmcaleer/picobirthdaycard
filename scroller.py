from pimoroni_i2c import PimoroniI2C
from breakout_rgbmatrix5x5 import BreakoutRGBMatrix5x5
from time import sleep
from font import font

PINS_PICO_EXPLORER = {"sda": 2, "scl":3}
i2c = PimoroniI2C(**PINS_PICO_EXPLORER)
matrix = BreakoutRGBMatrix5x5(i2c)

# Simple 5x5 font (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z)

def display_character(matrix, character, r, g, b, ):
    for y, row in enumerate(character):
        for x, pixel in enumerate(row):
            if pixel == "1":
                matrix.set_pixel(x, y, r, g, b)
            else:
                matrix.set_pixel(x, y, 0, 0, 0)

def scroll_text(text,matrix, r,g,b,delay=0.2):
    for ch in text:
        if ch in font:
            ch_matrix = font[ch]
        else:
            ch_matrix = ["00000"] * 5
        for col in range(5):
            for row in range(5):
                if col >= 0 and col <= 5:
                    pixel_state = int(ch_matrix[row][col])
                else:
                    pixel_state = 0

                if pixel_state:
                    matrix.set_pixel(row, col, r, g, b)
                else:
                    matrix.set_pixel(row, col, 0, 0, 0)

        matrix.update()
        sleep(delay)
def scroll_text2(text, matrix, r, g, b, delay=0.1):
    full_text_matrix = []
    for ch in text:
        if ch.upper() in font:
            ch_matrix = font[ch.upper()]
        else:
            ch_matrix = ["000"] * 5  # Empty character if not in the font
        
        # Add the character columns to the full text matrix with an extra empty column
        width = len(ch_matrix[0])
        for col in ch_matrix:
            full_text_matrix.append([int(pixel) for pixel in col])
        full_text_matrix.append([0] * width)

    # Add extra empty columns at the beginning and end
    for _ in range(5):
        full_text_matrix.insert(0, [0] * 5)
        full_text_matrix.append([0] * 5)

    for start_col in range(len(full_text_matrix) - 4):
        for x in range(5):
            for y in range(5):
                pixel_state = full_text_matrix[start_col + x][y]
                if pixel_state:
                    matrix.set_pixel(x, y, r, g, b)
                else:
                    matrix.set_pixel(x, y, 0, 0, 0)
        matrix.update()
        sleep(delay)


# Example usage:
# scroll_text("HELLO", matrix, 255, 255, 0)


scroll_text2("Happy Birthday Alex",matrix,255,255,255, delay=0.1)