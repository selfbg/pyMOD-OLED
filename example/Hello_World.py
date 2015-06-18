from oled import OLED
from oled import Font
from oled import Graphics

# Connect to the display on /dev/i2c-0
dis = OLED(0)

# Start communication
dis.begin()

# Start basic initialization
dis.initialize()

# Do additional configuration
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)

# Clear display
dis.clear()

# Set font scale x2
f = Font(2)

# Print some large text
f.print_string(6, 0, "OLIMEX LTD")

# Change font to 5x7
f.scale = 1
f.print_string(0, 24, "MOD-OLED-128x64")
f.print_string(0, 32, "olimex.com")

# Send video buffer to display
dis.update()

# Make horizontal scroll
dis.horizontal_scroll_setup(dis.LEFT_SCROLL, 3, 3, 7)
dis.activate_scroll()

# Only the last scroll setup is active
dis.horizontal_scroll_setup(dis.LEFT_SCROLL, 4, 4, 7)
dis.activate_scroll()

# Draw line
Graphics.draw_pixel(0, 0)
Graphics.draw_line(0, 60, 100, 63)
dis.update()