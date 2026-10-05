import csv
import json

def to_csv(json_obj):
    if isinstance(json_obj, dict):
        return ','.join([f"{k}:{v}" for k, v in json_obj.items()])
    elif isinstance(json_obj, list):
        return '\n'.join([to_csv(item) for item in json_obj])
    else:
        return str(json_obj)
