
def sort_data(schools):
    """Sorts the jsonified list of schools/interest points first according to
    ascending latitude, then according to ascending longnitude. Returns two
    separate sorted lists.
    """
    features = schools["features"]
    by_latitude = sorted(features, key=lambda e: e["geometry"]["coordinates"][0])
    by_longnitude = sorted(features, key=lambda e: e["geometry"]["coordinates"][1])

    return (by_latitude, by_longnitude)

def prune_data(schools):
    """Prunes out all data except for id, latitude, and longnitude. Returns a
    json list with the following structure:
        [{"admin_id" : ..., "latitude" : ..., "longnitude" : ...}, ...]
    """
    return [{"admin_id" : s["properties"]["admin_id"],
             "latitude" : s["geometry"]["coordinates"][0],
             "longnitude" : s["geometry"]["coordinates"][1],
            } for s in schools]
