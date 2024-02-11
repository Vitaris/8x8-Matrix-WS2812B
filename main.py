from matrix_8x8 import matrix_8x8
from graphics import *
import utime
import random
print(random.randint(0, 9))

if __name__ == "__main__":
    matrix = matrix_8x8(28, 5, brightness=0.02)
    while True:
        matrix.show_number(random.randint(0, 99), color=random.choice(COLORS))
        matrix.show_symbol(random.choice(SYMBOLS), offset=1, color=random.choice(COLORS))
        matrix.show_symbol(random.choice(SYMBOLS), offset=2, color=random.choice(COLORS))
        utime.sleep(1)
    
    

