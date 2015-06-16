MOD-OLED-128x64 Library
=======================

Introduction
------------
Python library for interfacing MOD-OLED-128x64 with OLinuXino boards.
SSD1306 controller support SPI, I2C and parallel interface, but with
this module only I2C is usable.

By default i2c-1 and i2c-2 buses use 100kHz clock. This means that you can 
achieve around 8 frames per second. You can use i2c-0 which in most OLinuXino boards
is running at 400kHz (around 25 fps, because this bus is used also for the PMU module).
You can speed things up by using smaller than 128x64 display area.

Requirements
------------
This package needs the following modules:

- pyserial

To install them use::

    pip install pyserial

or for python3::

    pip-3.x install pyserial


Installation
------------


Usage
-----

To import module use::

    from OLED import OLED
    from OLED import Font

