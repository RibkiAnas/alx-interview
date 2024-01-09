#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Method that determines if all the boxes
    can be opened or not.
    """
    if not boxes:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
