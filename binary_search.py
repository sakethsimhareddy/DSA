def binary_search(array,key):
    lo=0
    hi=len(array)-1
    while lo <=hi:
        mid=(lo+hi)//2
        mid_value= array[mid]
        if mid_value==key:
            return mid
        elif mid_value> key:
            lo=mid+1
        elif mid_value<key:
            hi=mid-1
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
            'array': [13, 11, 10, 7, 7,7,7,4, 3, 1, 0],
            'key':7
        },
        'output':5
    }
]
for test in tests:
    if binary_search(**test['input']) == test['output']:
        print('pass')
    else:
        print('error')