"""Write a function called stringifyNumbers which takes in an object
 and finds all of the values which are numbers and converts them to strings.
Recursion would be a great way to solve this!"""


def stringifyNumbers(obj):
    new_obj = {}
    for key, val in obj.items():
        if type(val) == int:
            new_obj[key] = str(val)
        elif type(val) == dict:
            new_obj[key] = stringifyNumbers(val)
        else:
            new_obj[key] = val
    return new_obj


obj = {
    "num": 1,
    "test": [],
    "data": {
        "data": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

stringified_obj = stringifyNumbers(obj)
print(obj)
print(stringified_obj)
#    {'num': '1',
#         'test': [],
#         'data': {'data': '4',
#                  'info': {'isRight': True, 'random': '66'}
#                  }
#         }
