
def prune_data(schools):
    """Prunes out all data except for id, latitude, and longnitude. Returns a
    json list with the following structure:
        [{"admin_id" : ..., "latitude" : ..., "longnitude" : ...}, ...]
    """
    features = schools["features"]
    return [{"admin_id" : s["properties"]["admin_id"],
             "latitude" : s["geometry"]["coordinates"][0],
             "longnitude" : s["geometry"]["coordinates"][1],
            } for s in features]

def sort_data(pruned_schools):
    """Sorts the jsonified list of schools/interest points first according to
    ascending latitude, then according to ascending longnitude. Returns two
    separate sorted lists.

    Make sure that the data you pass to this method is pruned beforehand using
    the prune_data method.
    """
    by_latitude = sorted(pruned_schools, key=lambda e: e["latitude"])
    by_longnitude = sorted(pruned_schools, key=lambda e: e["longnitude"])

    return (by_latitude, by_longnitude)
