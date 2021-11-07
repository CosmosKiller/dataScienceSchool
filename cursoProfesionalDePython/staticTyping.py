from typing import List, Dict, Tuple

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
    'argentina': 1,
    'mexico': 34,
    'colombia': 45
}

countries: List[Dict[str,str]] =[
    {
        'name': 'Argentina',
        'people': '450000'
    },
    {
        'name': 'México',
        'people': '90000000'
    },
    {
        'name': 'colombia',
        'people': '99999999999'
    }
]

numbers: Tuple[int, float, int] = (1, 0.5, 1)

#creating custom types to use later in our program

CoordinateTypes = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinateTypes = [
    {
        'coord1': (1, 2),
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1),
        'coord2': (2, 5)
    }
]