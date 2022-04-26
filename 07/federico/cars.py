from typing import Dict, List

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    jeeps = cars['Jeep']

    jeep_list =  ''

    for jeep in jeeps:
        jeep_list += jeep
        jeep_list += ", "

    return jeep_list[:-2]


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    first_model = list()

    for car in cars.keys():
        models = cars.get(car)
        first_model.append(models[0])
    return first_model


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    search_results = list()
    for car in cars:
        models = cars[car]
        for model in models:
            if grep.lower() in model.lower():
                search_results.append(model) 
    return sorted(search_results)


def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    ordered_dict = dict()

    for car in cars:
        # Note to self: this is done step-wise because
        # cars is a dictionary, and the value cars[car] is a list
        # Some how Python seems to get hung up in doing this in a single line
        models = cars[car]
        models.sort()
        ordered_dict[car] = models

    return ordered_dict

if __name__ == "__main__":
    sort_car_models(cars)