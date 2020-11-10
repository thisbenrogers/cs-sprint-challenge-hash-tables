def get_indices_of_item_weights(weights, length, limit):

    if length <= 1:
        return None

    
    d = dict()
    r = []
    i = 0
    res = []

    
    for w in weights:
        d[i] = w
        r.append(limit - w)
        i += 1            

    for k, v in d.items():
        if v in r:
            res[:0] = [k]
        if len(res) == 2:
            return tuple(res)

    return None