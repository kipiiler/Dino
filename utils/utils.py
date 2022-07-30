import json
import os


def readJsonFile(rela_path):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, rela_path)
    f = open(filename, "r")
    response = json.load(f)
    f.close()
    return response


def update_list(list):
    # Update el in a list
    for elem in list:
        elem.update()


def draw_list(list):
    # Draw element in a list
    for elem in list:
        elem.draw()


def cleanup_list(list):
    # Remove any el in list that is not alive
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.is_alive:
            list.pop(i)
        else:
            i += 1
