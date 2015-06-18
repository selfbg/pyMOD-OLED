=======================
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

- smbus-cffi

Installation
------------

From GitHub:

.. code-block:: bash

    git clone https://github.com/SelfDestroyer/pyMOD-OLED.git
    cd pyMOD-OLED
    python setup.py install

From PyPi:

.. code-block:: bash

    wget https://pypi.python.org/packages/source/m/mod-oled-128x64/mod-oled-128x64-0.0.3.tar.gz
    tar -zxf mod-oled-128x64-0.0.3.tar.gz
    cd mod-oled-128x64-0.0.3
    python setup.py install

Using pip:

.. code-block:: bash

    pip install mod-oled-128x64

Usage
-----
There are 3 modules in this package:

- OLED - Main class for control. Here you can make all the setup that you need.
- Font - Contains basic font table and has ability to write characters from it.
- Graphics - Basic drawing methods - pixel, line and circle.


To import module use:

.. code-block:: python

    from oled import OLED
    from oled import Font
    from oled import Graphics


Complete example:

.. code-block:: python

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

Classes and methods
-------------------

**class class oled.OLED(i2c, address=60)**

   *activate_scroll()*

      Activate Scroll (2Fh)

      This command starts the motion of scrolling and should only be
      issued after the scroll setup parameters have been defined by
      the scrolling setup commands :26h/27h/29h/2Ah . The setting in
      the last scrolling setup command overwrites the setting in the
      previous scrolling setup commands.

      The following actions are prohibited after the scrolling is
      activated
      RAM access (Data write or read)

      Changing the horizontal scroll setup parameters

   *begin()*

      Create communication object

   *charge_pump_setting(on)*

      Charge Pump Regulator (8Dh)

      Parameters:
         **on** -- True - Enable charge pump during display on False -
         Disable charge pump(RESET)

   *clear(update=True)*

      Clear video buffer

      Parameters:
         **update** -- If true send the empty buffer to the controller

   *close()*

      Close I2C bus and delete communication object

   *deactivate_scroll()*

      Deactivate scroll (2Eh)

      This command stops the motion of scrolling. After sending 2Eh
      command to deactivate the scrolling action,the ram data needs to
      be rewritten.

   *entire_display_on(status)*

      Entire Display ON (A4h/A5h)

      A4h command enable display outputs according to the GDDRAM
      contents.If A5h command is issued, then by using A4h command,
      the display will resume to the GDDRAM contents. In other words,
      A4h command resumes the display from entire display “ON” stage.
      A5h command forces the entire display to be “ON”, regardless of
      the contents of the display data RAM.

      Parameters:
         **status** -- True - Entire display ON. Output ignores RAM
         content False - Resume to RAM content display (RESET). Output
         follows RAM content

   *horizontal_scroll_setup(direction, start_page, end_page, speed)*

      Horizontal Scroll Setup (26h/27h)

      This command consists of consecutive bytes to set up the
      horizontal scroll parameters and determines the scrolling start
      page, end page and scrolling speed. Before issuing this command
      the horizontal scroll must be deactivated (2Eh). Otherwise, RAM
      content may be corrupted.

      Parameters:
         * **direction** -- 0 - Right Horizontal Scroll 1 - Left
           Horizontal Scroll

         * **start_page** -- Define start page address - PAGE0 ~
           PAGE7

         * **end_page** -- Define end page address - PAGE0 ~ PAGE7

         * **speed** -- Set time interval between each roll step in
           terms of frame frequency: 0 - 5 frames 1 - 64 frames 2 -
           128 frames 3 - 256 frames 4 - 3 frames 5 - 4 frames 6 - 25
           frames 7 - 2 frames

      Raises ValueError:
         Start page cannot be larger than end page

   *initialize()*

      Basic display initialization

   *send_data(data)*

      Send data in packets by 16 bytes

      Parameters:
         **data** -- Data to be send

   *send_nop()*

      NOP (E3h)

      No operation command

   *set_column_address(column_start_address, column_end_address)*

      Set Column Address (21h)

      This triple byte command specifies column start address and end
      address of the display data RAM. This command also sets the
      column address pointer to column start address.  This pointer is
      used to define the current read/write column address in graphic
      display data RAM.  If horizontal address increment mode is
      enabled by command 20h, after finishing read/write one column
      data, it is incremented automatically to the next column
      address.  Whenever the column address pointer finishes accessing
      the end column address, it is reset back to start column address
      and the row address is incremented to the next row.

      Parameters:
         * **column_start_address** -- Column start address, range :
           0-127d, (RESET=0d)

         * **column_end_address** -- Column end address, range :
           0-127d, (RESET =127d)

      Raises MethodError:
         This command is only for horizontal or vertical addressing
         mode.

   *set_com_pins_configuration(configuration, remap)*

      Set COM Pins Hardware Configuration (DAh)

      This command sets the COM signals pin configuration to match the
      OLED panel hardware layout. Refer to datasheet section 10.1.18
      for detailed information.

      Parameters:
         * **configuration** -- 0 - Sequential COM pin
           configuration, 1 - Alternative COM pin configuration
           (RESET)

         * **remap** -- 0 - Disable COM Left/Right remap (RESET) 1 -
           Enable COM Left/Right remap

   *set_contrast_control(contrast)*

      Set Contrast Control for BANK0 (81h)

      This command sets the Contrast Setting of the display. The chip
      has 256 contrast steps from 00h to FFh. The segment output
      current increases as the contrast step value increases.

      Parameters:
         **contrast** -- Double byte command to select 1 out of 256
         contrast steps. Contrast increases as the value increases.
         (RESET = 7Fh )

   *set_deselect_level(level)*

      Set Vcomh deselect level (DBh)

      This command adjust the Vcomh regulator output.

      Parameters:
         **level** -- 0, 1 or 2 0 ~ 0.65 * Vcc 1 ~ 0.77 * Vcc (RESET)
         2 ~ 0.83 * Vcc

   *set_display_clock(divider, osc_freq)*

      Set Display Clock Divide Ratio/Oscillator Frequency (D5h)

      This command consists of two functions:

         * Display Clock Divide Ratio (D)(A[3:0])

         Set the divide ratio to generate DCLK (Display Clock) from
         CLK.  The divide ratio is from 1 to 16, with reset value = 1.
         Please refer to section 8.3 for the details relationship of
         DCLK and CLK.

         * Oscillator Frequency (A[7:4])

         Program the oscillator frequency Fosc that is the source of
         CLK if CLS pin is pulled high.  The 4-bit value results in 16
         different frequency settings available as shown below.  The
         default setting is 1000b.

      Parameters:
         * **divider** -- Define the divide ratio (D) of the display
           clocks (DCLK): Dvide ration = DIVIDER + 1, RESET is 0
           (divide ratio = 1)

         * **osc_freq** -- Set the Oscillator Frequncy, Fosc.
           Oscillator Frequency increases with the value of OSC_FREQ
           and vice versa. RESET is 1000b. Range: 0000b ~ 1111b.

   *set_display_offset(offset)*

         Set Display Offset (D3h)

         This is a double byte command. The second command specifies
         the mapping of the display start line to one of COM0~COM63
         (assuming that COM0 is the display start line then the
         display start line register is equal to 0). For example, to
         move the COM16 towards the COM0 direction by 16 lines the
         6-bit data in the second byte should be given as 010000b. To
         move in the opposite direction by 16 lines the 6-bit data
         should be given by 64 – 16, so the second byte would be
         100000b.

      Parameters:
         **offset** -- Set vertical shift by COM from 0d~63d The value
         is reset to 00h after RESET.

   *set_display_on_off(on)*

      Set Display ON/OFF (AEh/AFh)

      These single byte commands are used to turn the OLED panel
      display ON or OFF. When the display is ON, the selected circuits
      by Set Master Configuration command will be turned ON. When the
      display is OFF, those circuits will be turned OFF and the
      segment and common output are in VSS state and high impedance
      state, respectively.

      Parameters:
         **on** -- True - Display ON False - Display OFF

   *set_display_start_line(start_line)*

      Set Display Start Line (40h~7Fh)

      This command sets the Display Start Line register to determine
      starting address of display RAM, by selecting a value from 0 to
      63. With value equal to 0, RAM row 0 is mapped to COM0. With
      value equal to 1, RAM row 1 is mapped to COM0 and so on.

      Parameters:
         **start_line** -- Set display RAM display start line register
         from 0-63. Display start line register is reset to 000000b
         during RESET.

   *set_higher_column(column)*

      Set Higher Column Start Address for Page Addressing Mode
      (10h~1Fh)

      This command specifies the higher nibble of the 8-bit column
      start address for the display data RAM under Page Addressing
      Mode. The column address will be incremented by each data
      access.

      Parameters:
         **column** -- Set the higher nibble of the column start
         address register for Page Addressing Mode using X[3:0] as
         data bits. The initial display line register is reset to
         0000b after RESET.

      Raises MethodError:
         This command is only for page addressing mode

   *set_inverse_display(inverse)*

      Set Normal/Inverse Display (A6h/A7h)

      This command sets the display to be either normal or inverse. In
      normal display a RAM data of 1 indicates an “ON” pixel while in
      inverse display a RAM data of 0 indicates an “ON” pixel.

      Parameters:
         **inverse** -- True - Inverse display False - ormal display
         (RESET)

   *set_lower_column(column)*

      Set Lower Column Start Address for Page Addressing Mode
      (00h~0Fh)

      This command specifies the lower nibble of the 8-bit column
      start address for the display data RAM under Page Addressing
      Mode. The column address will be incremented by each data
      access.

      Parameters:
         **column** -- Set the lower nibble of the column start
         address register for Page Addressing Mode using X[3:0] as
         data bits. The initial display line register is reset to
         0000b after RESET.

      Raises MethodError:
         This command is only for page addressing mode

   *set_memory_addressing_mode(mode)*

      Set Memory Addressing Mode (20h)

      There are 3 different memory addressing mode in SSD1306: page
      addressing mode, horizontal addressing mode and vertical
      addressing mode. This command sets the way of memory addressing
      into one of the above three modes. In there, “COL” means the
      graphic display data RAM column.

      Parameters:
         **mode** --

         2 - Page addressing mode In page addressing mode, after the
         display RAM is read/written, the column address pointer is
         increased automatically by 1.  If the column address pointer
         reaches column end address, the column address pointer is
         reset to column start address and page address pointer is not
         changed. Users have to set the new page and column addresses
         in order to access the next page RAM content.

         0 - Horizontal addressing mode In horizontal addressing mode,
         after the display RAM is read/written, the column address
         pointer is increased automatically by 1.  If the column
         address pointer reaches column end address, the column
         address pointer is reset to column start address and page
         address pointer is increased by 1. When both column and page
         address pointers reach the end address, the pointers are
         reset to column start address and page start address.

         1 - Vertical addressing mode In vertical addressing mode,
         after the display RAM is read/written, the page address
         pointer is increased automatically by 1.  If the page address
         pointer reaches the page end address, the page address
         pointer is reset to page start address and column address
         pointer is increased by 1. When both column and page address
         pointers reach the end address, the pointers are reset to
         column start address and page start address

   *set_multiplex_ratio(ratio)*

      Set Multiplex Ratio (A8h)

      This command switches the default 63 multiplex mode to any
      multiplex ratio, ranging from 16 to 63. The output pads
      COM0~COM63 will be switched to the corresponding COM signal.

      Parameters:
         **ratio** -- Set MUX ratio to N+1 MUX N=A[5:0] : from 16MUX
         to 64MUX, RESET= 111111b (i.e. 63d, 64MUX) A[5:0] from 0 to
         14 are invalid entry.

   *set_page_address(page_start_address, page_end_address)*

      Set Page Address (22h)

      This triple byte command specifies page start address and end
      address of the display data RAM. This command also sets the page
      address pointer to page start address. This pointer is used to
      define the current read/write page address in graphic display
      data RAM. If vertical address increment mode is enabled by
      command 20h, after finishing read/write one page data, it is
      incremented automatically to the next page address.  Whenever
      the page

         address pointer finishes accessing the end page address, it
         is reset back to start page address.

      Parameters:
         * **page_start_address** -- Page start Address, range :
           0-7d, (RESET = 0d)

         * **page_end_address** -- Page end Address, range : 0-7d,
           (RESET = 7d)

      Raises MethodError:
         This command is only for horizontal or vertical addressing
         mode.

   *set_page_start_address(page)*

      Set Page Start Address for Page Addressing Mode (B0h~B7h)

      This command positions the page start address from 0 to 7 in
      GDDRAM under Page Addressing Mode.

      Parameters:
         **page** -- Set GDDRAM Page Start Address (PAGE0~PAGE7) for
         Page Addressing Mode using X[2:0].

      Raises MethodError:
         This command is only for page addressing mode

   *set_precharge_period(phase1, phase2)*

      Set Pre-charge Period (D9h)

      This command is used to set the duration of the pre-charge
      period. The interval is counted in number of DCLK, where RESET
      equals 2 DCLKs.

      Parameters:
         * **phase1** -- Phase 1 period of up to 15 DCLK clocks, 0
           is invalid entry (RESET = 2h)

         * **phase2** -- Phase 2 period of up to 15 DCLK clocks, 0
           is invalid entry (RESET = 2h)

   *set_scan_direction(remapped)*

      Set COM Output Scan Direction (C0h/C8h)

      This command sets the scan direction of the COM output allowing
      layout flexibility in the OLED module design. Additionally, the
      display will show once this command is issued. For example, if
      this command is sent during normal display then the graphic
      display will be vertically flipped immediately.

      Parameters:
         **remapped** -- True - remapped mode. Scan from COM[N-1] to
         COM0 False - normal mode. Scan from COM0 to COM[N –1] (RESET)
         Where N is the Multiplex ratio.

   *set_segment_remap(remap)*

      Set Segment Re-map (A0h/A1h)

      This command changes the mapping between the display data column
      address and the segment driver. It allows flexibility in OLED
      module design. Please refer to Table 9-1.

      This command only affects subsequent data input.  Data already
      stored in GDDRAM will have no changes.

      Parameters:
         **remap** -- True - column address 127 is mapped to SEG0
         False - column address 0 is mapped to SEG0 (RESET)

   *set_vertical_scroll_area(start, count)*

      Set Vertical Scroll Area(A3h)

      This command consists of 3 consecutive bytes to set up the
      vertical scroll area. For the continuous vertical scroll
      function (command 29/2Ah), the number of rows that in vertical
      scrolling can be set smaller or equal to the MUX ratio.

      Parameters:
         * **start** -- Set No. of rows in top fixed area. The No.
           of rows in top fixed area is referenced to the top of the
           GDDRAM (i.e. row 0).[RESET =0]

         * **count** -- Set No. of rows in scroll area. This is the
           number of rows to be used for vertical scrolling. The
           scroll area starts in the first row below the top fixed
           area. [RESET = 64]

      Raises ValueError:

   *update()*

      Send video buffer to the controller

   *vertical_and_horizontal_scroll_setup(direction, start_page, end_page, speed, vertical_offset)*

      Continuous Vertical and Horizontal Scroll Setup (29h/2Ah)

      This command consists of 6 consecutive bytes to set up the
      continuous vertical scroll parameters and determines the
      scrolling start page, end page, scrolling speed and vertical
      scrolling offset.

      The bytes B[2:0], C[2:0] and D[2:0] of command 29h/2Ah are for
      the setting of the continuous horizontal scrolling. The byte
      E[5:0] is for the setting of the continuous vertical scrolling
      offset. All these bytes together are for the setting of
      continuous diagonal (horizontal + vertical) scrolling. If the
      vertical scrolling offset byte E[5:0] is set to zero, then only
      horizontal scrolling is performed (like command 26/27h).

      Before issuing this command the scroll must be deactivated
      (2Eh). Otherwise, RAM content may be corrupted.

      Parameters:
         * **direction** -- 0 - Vertical and Right Horizontal Scroll
           1 - Vertical and Left Horizontal Scroll

         * **start_page** -- Define start page address - PAGE0 ~
           PAGE7

         * **end_page** -- Define end page address -   PAGE0 ~ PAGE7

         * **speed** -- Set time interval between each roll step in
           terms of frame frequency: 0 - 5 frames 1 - 64 frames 2 -
           128 frames 3 - 256 frames 4 - 3 frames 5 - 4 frames 6 - 25
           frames 7 - 2 frames

         * **vertical_offset** -- Vertical scrolling offset e.g. 01h
           refer to offset = 1 row 3Fh refer to offset = 63 rows

      Raises ValueError:
         Start page cannot be larger than end page


**class class oled.Font(scale=1)**

   *print_char(x, y, ch)*

      Print single char at location

      Parameters:
         * **x** -- X location

         * **y** -- Y location

         * **ch** -- ASCII code for char

   *print_string(x0, y0, string)*

      Print string to display.

      Parameters:
         * **x0** -- Start X position

         * **y0** -- Start Y position

         * **string** -- String to display

      Returns: None


**class class oled.Graphics**

   *classmethod draw_circle(x0, y0, r)*

      Draw singled circle

      Parameters:
         * **x0** -- Center x location

         * **y0** -- Center y location

         * **r** -- Radius

   *classmethod draw_line(x0, y0, x1, y1)*

      Draw single line

      Parameters:
         * **x0** -- Start x location

         * **y0** -- Start y location

         * **x1** -- End x location

         * **y1** -- End y location

   *classmethod draw_pixel(x, y, on=True)*

      Draw single pixel to video buffer

      Parameters:
         * **x** -- X location

         * **y** -- Y location

         * **on** -- True - Set pixel, False - clear pixel
