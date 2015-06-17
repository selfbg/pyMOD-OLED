__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2015, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"

from oled import OLED
from oled import Font
from oled import Graphics

#
dis = OLED(0)
dis.begin()
dis.initialize()
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)

# Clear display
dis.clear()

# Set font scale x2
f = Font(2)

f.print_string(6, 0, "OLIMEX LTD")
f.scale = 1
f.print_string(0, 24, "MOD-OLED-128x64")
f.print_string(0, 32, "olimex.com")
dis.update()

dis.horizontal_scroll_setup(dis.LEFT_SCROLL, 3, 3, 7)
dis.activate_scroll()

dis.horizontal_scroll_setup(dis.LEFT_SCROLL, 4, 4, 7)
dis.activate_scroll()



Graphics.draw_pixel(0, 0)
Graphics.draw_line(0, 60, 100, 63)
dis.update()