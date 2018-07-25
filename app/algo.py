"""Retrieves a set of schools which are within a given range (kilometers) from
the nearest health site.
"""

from bisect import bisect_left
from concurrent import futures
import io
import json
import sys

from util import sort_data, prune_data

import shapefile

lat_list, long_list = [], []
kilometers = 0
hospitals = shapefile.Reader("static/data/healthsites/shapefiles/healthsites")
kilometers = float(sys.argv[1]) / 111.0

with open('data.json') as schools_json:
    schools_loaded = json.load(schools_json)
    sorted_schools = schools_loaded
    schools = sorted_schools[0]
    for pos, school in enumerate(schools):
        lat_list.append(school['latitude'])
        long_list.append(school['longitude'])

def get_all_schools():
    """Get a set of all schools which are "kilometers" away from a hospital"""
    validSchools = set()
    with futures.ProcessPoolExecutor() as executor:
        for result in executor.map(get_close_schools, hospitals.iterShapes()):
            validSchools = validSchools.union(result)
    return validSchools

def get_closest(sortedList, num):
    """Get the next closest point to a given number in a list"""
    pos = bisect_left(sortedList, num)
    if pos == len(sortedList):
        return -1
    before = sortedList[pos - 1]
    after = sortedList[pos]
    if after - num < num - before:
        return pos
    else:
        return pos - 1

def traverse(coordList, closest, point, increment):
    """Traverse a list of coordinates (either lat or long) in a given direction
    and add the valid points to a set.
    """
    coordSet = set()
    currentKey = closest
    valid = True
    while valid:
        if(abs(coordList[currentKey] - point)) < kilometers:
            coordSet.add(currentKey)
            currentKey += increment;
        else:
            valid = False
    return coordSet

def get_close_schools(hospital):
    """Get the set of schools which are "kilometers" km away laterally and
    longitudinally.
    """
    point = hospital.points[0];
    closestLat = get_closest(lat_list, point[0])

    latSetF = traverse(lat_list, closestLat, point[0], 1);
    latSetB = traverse(lat_list, closestLat, point[0], -1);
    latSet = latSetF.union(latSetB)

    closestLong = get_closest(long_list, point[1])
    longSetF = traverse(long_list, closestLong, point[1], 1);
    longSetB = traverse(long_list, closestLong, point[1], -1);
    longSet = longSetF.union(longSetB)

    return latSet.intersection(longSet)

def usage():
    print("USAGE: algo.py <kilometers>\n" + __doc__)

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    print(get_all_schools())

if __name__ == "__main__":
    main()
