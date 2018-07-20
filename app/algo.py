import json
import shapefile
import io
import sys
from concurrent import futures
from bisect import bisect_left
from util import sort_data, prune_data

if (len(sys.argv) != 2):
    print ("USAGE: algo.py <kilometers>\n\t - retrieves a set of schools which are within <kilometers> from the nearest health site")
    sys.exit(0)

hospitals = shapefile.Reader("static/data/healthsites/shapefiles/healthsites")
kilometers = float(sys.argv[1]) / 111.0
latList = []
longList = []

with open('static/data/schools.json') as schools_json:
    schools_loaded = json.load(schools_json)
    pruned_schools = prune_data(schools_loaded)
    sorted_schools = sort_data(pruned_schools)
    schools = sorted_schools[0]
    for pos, school in enumerate(schools):
        latList.append(school['latitude'])
        longList.append(school['longitude'])

# Get a set of all schools which are "kilometers" away from a hospital
def get_all_schools():
    validSchools = set()
    with futures.ProcessPoolExecutor() as executor:
        for result in executor.map(get_close_schools, hospitals.iterShapes()):
            validSchools = validSchools.union(result)
    return validSchools

# Get the next closest point to a given number in a list
def getClosest(sortedList, num):
    pos = bisect_left(sortedList, num)
    if pos == len(sortedList):
        return -1
    before = sortedList[pos - 1]
    after = sortedList[pos]
    if after - num < num - before:
        return pos
    else:
        return pos - 1

# Traverse a list of coordinates (either lat or long)
# in a given direction and add the valid points to a set
def traverse(coordList, closest, point, increment):
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

# Get the set of schools which are "kilometers" km away
# laterally and longitudinally
def get_close_schools(hospital):
    point = hospital.points[0];
    closestLat = getClosest(latList, point[0])
    latSetF = traverse(latList, closestLat, point[0], 1);
    latSetB = traverse(latList, closestLat, point[0], -1);
    latSet = latSetF.union(latSetB)

    closestLong = getClosest(longList, point[1])
    longSetF = traverse(longList, closestLong, point[1], 1);
    longSetB = traverse(longList, closestLong, point[1], -1);
    longSet = longSetF.union(longSetB)

    return latSet.intersection(longSet)

print(len(get_all_schools()))
