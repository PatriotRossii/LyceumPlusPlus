import requests
import json


def dwarf_pest(port, host, **kwargs):
    result = {}
    if "place" in kwargs:
        place = kwargs["place"]
        kwargs.pop("place")
        result[place] = [kwargs]

    r = requests.get(f"http://{host}:{port}")
    data = r.json()

    for place in data:
        if place in result:
            result[place].extend(data[place])
        else:
            result[place] = data[place]

    return result
