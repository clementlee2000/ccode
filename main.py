import os
from file_import import file_import
from process_data import process_data
from file_export import file_export


if __name__ == '__main__':
    file_in = os.path.join("data", "plate.json")  # hardcoded here but expected to be passed from upstream
    [well_names, raw_data] = file_import(file_in)

    all_max_idx = process_data(raw_data)

    file_out = 'plate.csv'
    file_export(well_names, all_max_idx, file_out)