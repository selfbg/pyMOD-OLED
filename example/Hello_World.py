__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2015, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"

from oled import OLED
from oled import Font

dis = OLED.OLED(0)
dis.begin()
dis.initialize()
dis.set_memory_addressing_mode(0)
dis.set_column_address(0, 127)
dis.set_page_address(0, 7)

dis.clear()
f = Font.Font(2)

# f.print_string(0, 0, "OLIMEX LTD.")
# f.print_string(0, 16, "MOD-OLED-128x64")
f.print_string(20, 33, "123456789012345678901234567890")
dis.update()