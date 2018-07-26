"""Basic utility functions that are used frequently across the webapp."""

from hashlib import md5

def prune_data(schools):
    """Prunes out all data except for id, latitude, and longitude. Returns a
    json list with the following structure:
        [{"name" : ..., "latitude" : ..., "longitude" : ...}, ...]
    """
    features = schools["features"]
    return [{"name" : s["properties"]["name"],
             "latitude" : s["geometry"]["coordinates"][0],
             "longitude" : s["geometry"]["coordinates"][1],
            } for s in features]

def sort_data(pruned_schools):
    """Sorts the jsonified list of schools/interest points first according to
    ascending latitude, then according to ascending longitude. Returns two
    separate sorted lists.

    Make sure that the data you pass to this method is pruned beforehand using
    the prune_data method.
    """
    by_latitude = sorted(pruned_schools, key=lambda e: e["latitude"])
    by_longitude = sorted(pruned_schools, key=lambda e: e["longitude"])

    return (by_latitude, by_longitude)

def frange(start, end, step):
    """For some dumb reason, the Python range() builtin function doesn't
    support floating point starts, stops, or steps. So this is my
    implementation of it.
    """
    current = start
    while current < end:
        yield current
        current += step

def gravatar_url(email, size):
    digest = md5(email.lower().encode("utf-8")).hexdigest()
    return "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(digest,
                                                                        size)
