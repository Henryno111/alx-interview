#!/usr/bin/python3
'''
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data,therefore you only
need to handle the 8 least significant bits of each integer
'''


def validUTF8(data):
    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        byte = data[i]

        # Determine the number of bytes in the UTF-8 character
        if byte & 0x80 == 0:  # 1-byte character
            pass
        elif byte & 0xE0 == 0xC0:  # 2-byte character
            if (i + 1 >= len(data) or
                    data[i + 1] & 0xC0 != 0x80):
                return False
            i += 1
        elif byte & 0xF0 == 0xE0:  # 3-byte character
            if (i + 2 >= len(data) or
                    data[i + 1] & 0xC0 != 0x80 or
                    data[i + 2] & 0xC0 != 0x80):
                return False
            i += 2
        elif byte & 0xF8 == 0xF0:  # 4-byte character
            if (i + 3 >= len(data) or
                    data[i + 1] & 0xC0 != 0x80 or
                    data[i + 2] & 0xC0 != 0x80 or
                    data[i + 3] & 0xC0 != 0x80):
                return False
            i += 3
        else:
            return False

        i += 1

    return True
