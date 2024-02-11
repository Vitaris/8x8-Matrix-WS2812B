![schema](https://github.com/Vitaris/8x8-Matrix-WS2812B/blob/main/pics/8x8_matrix_demo.gif)
# MicroPython 8x8 WS2812B LED Matrix Lib

## Overview

This MicroPython repository for Raspberry Pico RP2040 provides a simple and efficient way to control an 8x8 square matrix of WS2812B addressable LEDs. The WS2812B LEDs are individually addressable RGB LEDs, allowing for vibrant and customizable lighting effects.

## Features

- **MicroPython Compatibility:** The code is designed to work seamlessly with MicroPython, making it easy to program and control the LED matrix with MicroPython-enabled microcontrollers.

- **8x8 Matrix:** The repository includes code specifically tailored for an 8x8 LED matrix, providing a convenient interface for addressing each LED in the matrix individually.

- **RP2040 PIO Control:** Harness the precision and efficiency of the RP2040's PIO module to control WS2812B LEDs.

## Demo Script

The demo script included in this repository showcases the basic functionalities of the 8x8 LED matrix lib:

```python
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
