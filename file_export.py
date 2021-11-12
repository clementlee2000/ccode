import csv


def file_export(well_names, max_derivative_cycles, filename):
    """
    :param well_names: (str list) unique well names, to be duplicated and paired with well idx in output file
    :param max_derivative_cycles: (2-D int list) cycle indices for first derivative and second derivative maxima
    :param filename: (str) name of output file
    """
    # better way to expand lists here with `sum` and `zip`?...
    expanded_well_names = []
    well_idx = []
    # repeat well names and indices to create pairs for data entry
    for i in range(len(well_names)):
        expanded_well_names.extend([well_names[i] for _ in range(len(max_derivative_cycles[0]))])
        well_idx.extend([k for k in range(len(max_derivative_cycles[0]))])

    first_derivative_max_cycle = [channels[0] for wells in max_derivative_cycles for channels in wells]
    second_derivative_max_cycle = [channels[1] for wells in max_derivative_cycles for channels in wells]

    # bad form to use same field names and variable names? what are some better names here?
    data = {'well_name': expanded_well_names, 'well_index': well_idx,
            'first_derivative_max_cycle': first_derivative_max_cycle,
            'second_derivative_max_cycle': second_derivative_max_cycle}

    if filename[-4:] == '.csv':
        # `newline` necessary for Windows (else extra blank lines). any unix conflicts?
        with open(filename, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(data.keys())
            w.writerows(zip(*data.values()))
