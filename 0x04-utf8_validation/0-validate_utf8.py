#!/usr/bin/python3
'''
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
'''

def validUTF8(data):
    # Count of bytes in the current UTF-8 character
    bytes_count = 0


    # Iterate through each byte in the data
    
    for byte in data:
        # Check if this byte is the start of a new UTF-8 character
        if bytes_count == 0:
            # Count the number of leading 1s to determine byte count
            if byte >> 5 == 0b110:
                bytes_count = 1
            elif byte >> 4 == 0b1110:
                bytes_count = 2
            elif byte >> 3 == 0b11110:
                bytes_count = 3
            elif byte >> 7 != 0:
                # Invalid start of a UTF-8 character
                return False
        else:
            # Check if the byte is following the UTF-8 character format
            if byte >> 6 != 0b10:
                return False
            bytes_count -= 1
    
    # Check if there are any incomplete UTF-8 characters
    return bytes_count == 0
