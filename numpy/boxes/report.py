def get_description(): # see the docstring below?
    """Return random weather, just like the pros"""
    from random import choice#如果你希望在程式中其他地方用到可以考慮在一開頭做import
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
