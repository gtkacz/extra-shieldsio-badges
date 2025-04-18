from typing import Union

from shieldsio_plus.common.enums.shields_io_named_colors import ShieldsIONamedColor
from shieldsio_plus.common.types.hex_code import HexColor

# Type alias for colors supported by Shields.io
ShieldsIOColor = Union[ShieldsIONamedColor, HexColor]
"""
Type alias representing colors supported by Shields.io.

This union type allows for either:
    - ShieldsIONamedColor: Predefined named colors from the Shields.io palette
    - HexColor: Custom colors represented as hex codes
"""
