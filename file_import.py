import json


def file_import(filename):
    if filename[len(filename)-5:len(filename)] == '.json':
        with open(filename, 'r') as f:
            data = json.load(f)
        return data['well_names'], data['timeseries_signals']
