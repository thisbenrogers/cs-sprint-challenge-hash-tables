def get_indices_of_item_weights(weights, length, limit):

    # * base test
    if length <= 1:
        return None

    # * sets up empty dictionary and index counter
    d = dict()
    i = 0

    # * iterates through numeric values in weights list
    for w in weights:
        d[w] = [i, (limit - w)]     # * Makes an entry where key = weight, value = [index, pair weight]
        i += 1                      # * Increments index

    for k, v in d.items():
        an_index = v[0]
        pair_weight = v[1]
        if pair_weight in d.keys() and k is not None:
            return (d[pair_weight][0], an_index)

    return None
