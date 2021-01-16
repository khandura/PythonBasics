# way of creating dictionary
def create_dicts():
    # plain old way, add data inside {}
    fruits = {'Apple': 'Red', 'Mango': 'Yellow'}
    print('fruits  :', fruits)

    # create dict by calling dict() constructor
    days = dict({'sun': 'sunday', 'mon': 'monday'})
    months = dict(jan='Jan', feb='Feb')
    fruits = dict([(1, 'apple'), (2, 'ball')])
    print('days :', days)
    print('months :', months)
    print('fruits  :', fruits)

    # creating empty dictionary
    persons = {}
    persons["Akhi"] = "Python Dev"
    persons["Priyanka"] = "Java Dev"
    print('persons :', persons)


def create_complex_dict():
    # create dict from existing dict
    per_ages = {"Akhi": 32, "Priyanka": 29, 'Jaimini': 28, 'Navil': 35}
    per_age_gt_thirty = {key: val for key, val in per_ages.items() if val > 30}
    print('persons :', per_ages)
    print('persona age > 30 :', per_age_gt_thirty)

    # create dict using fromkeys() method
    basket = ('oranges', 'pears', 'apples', 'bananas')
    fruits = {}.fromkeys(basket, 1)  # fromkeys create a dict from exiting list with a provided default value
    print(fruits)


def add_update_items():
    basket = {'Apple': 10, 'Mango': 4}
    fruits = {'Peach': 2, 'Papaya': 4}
    print('initial basket :', basket)
    print('initial fruits :', fruits)

    # add items to basket
    basket["Cherry"] = 5
    basket['Banana'] = 2
    # setdefault() method will insert an entry to dict with provided default value if given key is not found
    basket.setdefault('Kiwi', 10)  # will add a new key Kiwi with value of 10 to dict
    basket.setdefault('Mango', 50)  # will not change anything as key is already present in dict
    # update basket item
    basket['Mango'] = 6
    basket.update(fruits)
    print('basket after adding and updating items :', basket)


def remove_items():
    basket = {'Apple': 10, 'Mango': 4}
    fruits = {'Peach': 2, 'Papaya': 4}
    basket.update(fruits)
    print('basket :', basket)
    print('fruits :', fruits)

    print('removing Peach from basket :', basket.pop('Peach'))
    print('removing Banana from basket :', basket.pop('Banana', 'NOT FOUND'))
    print('basket :', basket)
    print('fruits :', fruits)


def traverse_items():
    basket = {'Apple': 10, 'Mango': 4, 'Peach': 2, 'Papaya': 4}
    print('basket :', basket)
    print('keys :', basket.keys())
    print('values :', basket.values())
    print('items :', basket.items())

    # loop through keys()
    for key in basket.keys():
        print(f'key {key} : value {basket.get(key, None)}')

    # loop through each item using items()
    for key, val in basket.items():
        print(f'key {key} : value {val}')


# create_dicts()
# create_complex_dict()
# add_update_items()
# remove_items()
traverse_items()
