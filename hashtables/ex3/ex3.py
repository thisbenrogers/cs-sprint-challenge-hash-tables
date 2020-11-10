from collections import Counter

def intersection(arrays):
    
    result = []
    d = dict()
    counter = 0

    for arr in arrays:
        counter += 1
        for item in arr:
            if item in d:
                d[item] += 1
            else:
                d[item] = 1

    for key, value in d.items():
        if value == counter:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
