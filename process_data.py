def derivative(x):
    """ simple numerical derivative, basically diff(). output length is shortened by 1 each time this is applied """
    try:
        return [x_i - x_o for x_i, x_o in zip(x[1:], x[:-1])]
    except Exception as e:
        raise ValueError('Unable to take numerical derivative', e)


def find_max_idx(x):
    """ returns first value if duplicate, which should be fine for the current application """
    return x.index(max(x))


def find_derivatives_maxima(raw_data):
    xp = derivative(raw_data)
    xpp = derivative(xp)
    n = 1  # increment, 1 for derivative truncation (remove if using central derivative, etc.)
    # potentially n = 2 for 'zeroth cycle' vs 'first cycle' if .csv is final report for human interpretation
    return [find_max_idx(xp) + n, find_max_idx(xpp) + (n + 1)]


def process_data(raw_data):
    # is it necessary to generate the matrix here? cleaner and faster than .append()?
    all_max_idx = [[None for dim1 in enumerate(raw_data[0])] for dim2 in enumerate(raw_data)]
    for well_idx, wells in enumerate(raw_data):
        for chan_idx, channels in enumerate(wells):
            all_max_idx[well_idx][chan_idx] = find_derivatives_maxima(channels)

    return all_max_idx
