def maximum(values):
    _max = values[0]
    for val in values:
        if val > _max:
            _max = val
    return _max

def minimum(values):
    _min = values[0]
    for val in values:
        if val < _min:
            _min = val
    return _min

