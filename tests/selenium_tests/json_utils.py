import json
import os


def read_test_data(json_name):
    with open(os.path.join(os.path.dirname(__file__), "test_data", json_name), "r", encoding="utf-8", ) as f:
        data = json.load(f)
        return data


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items() if v not in (None, ""))
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj if x not in (None, ""))
    else:
        return obj


def from_json_get_by_path(obj, path):
    for key in path.split("."):
        if isinstance(obj, list) and key.isdigit():
            obj = obj[int(key)]
        else:
            obj = obj[key]
    return obj


def json_compare(expected, received):
    assert ordered(expected) == ordered(received), (f"expected: {expected}\n" f"received: {received}")
