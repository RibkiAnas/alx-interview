#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
      Determines if a given data set
      represents a valid UTF-8 encoding

      Args:
          data (list): list of integers

      Returns:
          bool: True if data is a valid
    """
    bytes = 0
    for i in data:
        """
            Check if the most significant bit is 0
        """
        byte = i & 0xFF
        if bytes:
            """
                Check if the most significant bit is
                1 and the second bit is 0
            """
            if byte >> 6 != 0b10:
                return False
            bytes -= 1
            continue
        while (1 << abs(7 - bytes)) & byte:
            """
                Count the number of bytes the UTF-8
                Character will have
            """
            bytes += 1
        if bytes == 1 or bytes > 4:
            """The data is not a valid UTF-8 encoding"""
            return False
        bytes = max(bytes - 1, 0)
    return bytes == 0
