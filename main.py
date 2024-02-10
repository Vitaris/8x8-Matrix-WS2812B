from matrix_8x8 import matrix_8x8
from graphics import *
import utime
import random
print(random.randint(0, 9))

if __name__ == "__main__":
    matrix = matrix_8x8(28, 5, brightness=0.02)
    matrix.show_symbol(smile, color=YELLOW)
    matrix.show_symbol(circle, offset=1, color=RED)
    matrix.show_symbol(circle, offset=2, color=ORANGE)
    matrix.show_symbol(circle, offset=3, color=GREEN)
    matrix.show_symbol(sad, offset=4, color=RED)

    while False:
        matrix.show_number(random.randint(0, 99), color=random.choice(COLORS))
        matrix.show_number(random.randint(0, 99), offset=1, color=random.choice(COLORS))
        matrix.show_number(random.randint(0, 99), offset=2, color=random.choice(COLORS))
        matrix.show_number(random.randint(0, 99), offset=3, color=random.choice(COLORS))
        matrix.show_number(random.randint(0, 99), offset=4, color=random.choice(COLORS))
        utime.sleep(1)
    
    

