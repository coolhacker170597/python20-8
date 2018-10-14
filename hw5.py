import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper