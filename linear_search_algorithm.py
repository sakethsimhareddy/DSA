def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    else:
        return -1


tests = [
    {
        'input': {
            'array': [13, 11, 10, 7, 4, 3, 1, 0],
            'key':7
        },
        'output':3
    },
    {
        'input': {
            'array': [4, 2, 11, -1],
            'key':4
        },
        'output':0
    },
    {
        'input': {
            'array': [3, -1, -9, -127],
            'key':4
        },
        'output':-1
    },
    {
        'input': {
            'array': [13, 11, 7, 7, 7, 10, 7, 4, 3, 1, 0],
            'key':7
        },
        'output':2
    }
]
for test in tests:
    if linear_search(**test['input']) == test['output']:
        print('pass')
    else:
        print('error')
