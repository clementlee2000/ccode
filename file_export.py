import csv


def file_export(well_names, max_derivative_cycles, file_out):
    # better way to expand lists here with `sum` and `zip`?...
    expanded_well_names = []
    well_idx = []
    for i in range(len(well_names)):
        expanded_well_names.extend([well_names[i] for _ in range(len(max_derivative_cycles[0]))])
        well_idx.extend([k for k in range(len(max_derivative_cycles[0]))])

    first_derivative_max_cycle = [channels[0] for wells in max_derivative_cycles for channels in wells]
    second_derivative_max_cycle = [channels[1] for wells in max_derivative_cycles for channels in wells]

    # bad form to use same field names and variable names? what are some better names here?
    data = {'well_name': expanded_well_names, 'well_index': well_idx,
            'first_derivative_max_cycle': first_derivative_max_cycle,
            'second_derivative_max_cycle': second_derivative_max_cycle}

    if file_out[len(file_out)-4:len(file_out)] == '.csv':
        # `newline` necessary for Windows (else extra blank lines). any unix conflicts?
        with open(file_out, 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(data.keys())
            w.writerows(zip(*data.values()))
