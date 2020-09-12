def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    if length <= 1:
        return None
    d = dict()
    i = 0
    for w in weights:
        d[i] = w
        for k, v in d.items():
            if limit - w == v:
                return (i, k)
                break
        i += 1
    return None
