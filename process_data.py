def derivative(x):
    a = x[1:len(x)]
    b = x[0:len(x) - 1]
    d = [a_i - b_i for a_i, b_i in zip(a, b)]
    return d

def find_max_idx(x):
    max_val, max_idx = max((val, idx) for (idx, val) in enumerate(x))
    # any faster or cleaner way to do this?
    # returns first value if duplicate, which should be fine for the current application
    return max_idx


def find_derivatives_maxes(raw_data):
    xp = derivative(raw_data)
    xpp = derivative(xp)

    n = 1    # increment, 1 for derivative truncation (remove if using central derivative, etc.)
    # potentially n = 2 for 'zeroth cycle' vs 'first cycle' if .csv is final report for human readability
    xp_max_cycle_idx = find_max_idx(xp) + n
    xpp_max_cycle_idx = find_max_idx(xpp) + (n+1)
    return [xp_max_cycle_idx, xpp_max_cycle_idx]


def process_data(raw_data):
    if type(raw_data[0][0][0]) != float:
        print('Input data is not float')
        # support other data types / convert to float?

    all_max_idx = [[None for dim1 in enumerate(raw_data[0])] for dim2 in enumerate(raw_data)]
    for well_idx, wells in enumerate(raw_data):
        for chan_idx, channels in enumerate(wells):
            all_max_idx[well_idx][chan_idx] = find_derivatives_maxes(channels)

    return all_max_idx
