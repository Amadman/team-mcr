
def get_modal_distance(classes_json):
    """Given classes.json, return the distance key of the modal class. In other
    words, return an approximation to the average distance of school from
    health centre.
    """
    return max(classes_json, key=len)[0]
