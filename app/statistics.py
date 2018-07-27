def get_mean_distance(classes_json):
    """Given classes.json, returns an approximation of the mean distance from a
    school to the nearest health centre.
    """
    total = sum(c[0] * len(c[1:]) for c in classes_json)
    length = sum(len(c[1:]) for c in classes_json)
    return total / length

def get_distance_stdev(classes_json):
    """Given classes.json, returns the standard deviation of schools
    to the nearest health centre.
    """
    mean = get_mean_distance(classes_json)
    length = sum(len(c[1:]) for c in classes_json)
    numerator = sum((c[0] - mean) ** 2 * len(c[1:]) for c in classes_json)
    print(length)
    return numerator / length

def get_modal_distance(classes_json):
    """Given classes.json, return the distance key of the modal class. In other
    words, return an approximation to the average distance of school from
    health centre.
    """
    return max(classes_json, key=len)[0]

def get_furthest_schools(classes_json, num_return):
    """Given classes.json, return the top (num_return) schools which are furthest away from their nearest health facility."""
    schools = [];
    i = 1
    for j in range(len(classes_json)):
        entry = classes_json[len(classes_json)-j-1]
        if(len(entry) > 1):
            for k in range(len(entry)):
                if(k != 0):
                    schools.append(entry[k])
                    i+=1
                if(i > num_return):
                    return schools
    return schools;
