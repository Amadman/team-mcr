"""Utility functions for working with classes.json, which is generated using
preprocess.py.
"""

# [[...], [2.5, {}, {}, ...], ...]

def get_range(classes, lower, upper):
    # NAIVE APPROACH CURRENTLY, maybe implement binary search if this is too
    # slow.
    schools = []
    for classs in classes:
        if classs[0] <= lower: continue
        elif classs[0] > upper: break
        schools.extend(classs[1:])

    return schools
