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
