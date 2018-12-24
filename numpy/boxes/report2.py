def get_description():
    import random #如果你希望在程式中其他地方用到可以考慮在一開頭做import
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return random.choice(possibilities)
