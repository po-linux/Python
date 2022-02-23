def test_one():
    dick = {
        'name': 'Polina',
        'age': 21,
        'love': {
            'name': 'Narek',
            'age': 23
        }
    }

    try:
        print(dick['fam'])
    except KeyError:
        pass