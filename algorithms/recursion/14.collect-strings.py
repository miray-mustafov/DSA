"""Write a function called collectStrings
which accepts an object and returns an array of all
the values in the object that have a typeof string."""


def collectStrings(obj):
    strings = []
    for value in obj.values():
        if type(value) == str:
            strings.append(value)
        if type(value) == dict:
            strings.extend(collectStrings(value))
    return strings


my_obj = {
    "stuff": 'foo',
    "data": {
        "data": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

collection = collectStrings(my_obj)
print(collection)  # ['foo', 'bar', 'baz']
