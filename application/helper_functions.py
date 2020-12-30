from parse import *

def property_types_la():
    return ['Entire apartment',
            'Entire house',
            'Private room in house',
            'Private room in apartment',
            'Entire guesthouse',
            'Entire condominium',
            'Entire guest suite',
            'Entire serviced apartment',
            'Entire bungalow',
            'Private room in condominium',
            'Shared room in house',
            'Private room in townhouse',
            'Entire townhouse',
            'Entire villa',
            'Entire loft']

def bathrooms_la():
    return ['0 baths', '0 shared baths', '1 bath', '1 private bath',
            '1 shared bath', '1.5 baths', '1.5 shared baths', '10 baths',
            '10.5 baths', '11 shared baths', '2 baths', '2 shared baths',
            '2.5 baths', '2.5 shared baths', '3 baths', '3 shared baths',
            '3.5 baths', '3.5 shared baths', '4 baths', '4 shared baths',
            '4.5 baths', '4.5 shared baths', '5 baths', '5 shared baths',
            '5.5 baths', '6 baths', '6 shared baths', '6.5 baths', '7 baths',
            '7.5 baths', '8 baths', '8 shared baths', '8.5 baths',
            '8.5 shared baths', '9 baths', '9.5 baths', 'Half-bath',
            'Private half-bath', 'Shared half-bath']


def parse_url(query):
    try:
        data = [[z for z in findall("zip={}&", query)][0][0],
                [sn for sn in findall("streetname={}&", query)][0][0],
                [sn for sn in findall("streetnum={}&", query)][0][0],
                [pt for pt in findall("ptype={}&", query)][0][0],
                [ac for ac in findall("accom={}&", query)][0][0],
                [nb for nb in findall("numbathrms={}&", query)][0][0],
                [nb for nb in findall("numbedrms={}&", query)][0][0],
                [nb for nb in findall("numbeds={}&", query)][0][0]]
        return data
    
    except IndexError:
        return False


