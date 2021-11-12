import json


def file_import(filename):
    if filename[-5:] == '.json':
        with open(filename, 'r') as f:
            data = json.load(f)
        return data.get('well_names'), data.get('timeseries_signals')
