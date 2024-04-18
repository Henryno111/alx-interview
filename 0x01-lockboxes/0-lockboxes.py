#!/usr/bin/python3
# a function call 
""" my function """ 
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

    opened_boxes = {0}

    available_keys = set(boxes[0])

    while available_keys:
        key = available_keys.pop()

        if key < num_boxes and key not in opened_boxes:
            opened_boxes.add(key)
            available_keys.update(boxes[key])

    return len(opened_boxes) == num_boxes
