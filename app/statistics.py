
def get_mean_distance(classes_json):
    total = sum(c[0] * len(c[1:]) for c in classes_json)
    length = sum(len(c[1:]) for c in classes_json)
    return total / length

def get_modal_distance(classes_json):
    """Given classes.json, return the distance key of the modal class. In other
    words, return an approximation to the average distance of school from
    health centre.
    """
    return max(classes_json, key=len)[0]
