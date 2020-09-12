def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    d = dict()
    for i in a:
        k = abs(i)
        if k not in d:
            d[k] = 1
        else:
            d[k] += 1
    for k, v in d.items():
        if v > 1:
            result.append(k)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
