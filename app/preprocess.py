"""Preprocesses the schools.json data into the desired format."""
import argparse
import json
import math

import shapefile
import util

def distance(a, b):
    """Calculates the approximate distance in KM between two latitude-longitude
    coordinates a and b.
    """
    latitude_delta = a[0] - b[0]
    longitude_delta = a[1] - b[1]
    return math.sqrt((latitude_delta ** 2 + longitude_delta ** 2) * 111)

def preprocess(increment, hospitals, schools):
    """Breaks the data down into pre-processed classes for fast delivery to a
    web client.
    """
    classes = []
    MAX = 250

    for i in util.frange(increment, MAX, increment):
        print(i)
        classes.append([i]) # add a new class
        for hospital in hospitals.iterShapes():
            for school in schools:
                point = hospital.points[0]
                hpos = (point[0], point[1])
                spos = (school["latitude"], school["longitude"])

                d = distance(spos, hpos)
                if d < i and d > i - increment:
                    classes[-1].append(school)
                    schools.remove(school)
                    print(len(schools))

    return classes

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--increment", "-i", metavar="km", type=float, default=1,
                        help="The span/size of each class.")
    parser.add_argument("--schools-file", "-s", metavar="schools.json",
                        required=True, type=argparse.FileType("r"),
                        help="The original schools.json file.")
    parser.add_argument("--hospitals-file", "-p", metavar="healthsites",
                        required=True, help="The original healthsites dir.")

    args = parser.parse_args()
    hospitals = shapefile.Reader(args.hospitals_file)
    schools = json.loads(args.schools_file.read())
    schools = util.prune_data(schools) # get rid of some cruft

    classes = preprocess(args.increment, hospitals, schools)
    with open("done", "w") as f:
        f.write(json.dumps(classes))

if __name__ == "__main__":
    main()
