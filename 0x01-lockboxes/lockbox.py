#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes: a list of lists where each inner list represents a box
    and contains the keys it holds.

    Returns:
    - True if all boxes can be opened, else False.
    """
    num_boxes = len(boxes)
    if num_boxes == 0:
        return False

    # Initialize a set to keep track of opened boxes
    opened_boxes = {0}

    # Initialize a set to keep track of available keys
    available_keys = set(boxes[0])

    # Loop until no new boxes can be opened
    while available_keys:
        # Get a key from the available keys
        key = available_keys.pop()

        # If the key opens a box and the box hasn't been opened yet
        if key < num_boxes and key not in opened_boxes:
            # Add the box to the opened boxes
            opened_boxes.add(key)
            # Add keys from the newly opened box to available keys
            available_keys.update(boxes[key])

    # If all boxes have been opened
    return len(opened_boxes) == num_boxes
