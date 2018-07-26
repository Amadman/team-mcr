"""Utility functions for working with classes.json, which is generated using
preprocess.py.
"""

def get_range(classes, lower, upper):
    """Given a classes json object, get_range returns a subset of the schools
    which lie within a distance interval [lower, upper] kilometers from the
    nearest health center.
    """
    schools = []
    for classs in classes:
        if classs[0] <= lower:
            continue
        elif classs[0] > upper:
            break
        schools.extend(classs[1:])

    return schools
