
FILENAME = 'rest.txt'

def commalist(foods):
    """ (str) -> [list]

        Return a list from comma-separated string

        >>>commalist('bob,joe')
        ['bob','joe']
        """
    output = foods.split(',')
    return output

def add_list_dict(dict, key, entry):
    """ {dict}, (str), (str) -> {dict}

         checks whether key exists in a given dictionary list,
         and appends to list for key or adds key & entry as appropriate

         """
    if key in dict:
        dict[key].append(entry)
    else:
        dict[key] = [entry]

def read_restaurants(file):

    """ (file) -> (dict of {str: int}, dict of {str: list of str}, dict of {str: list of str})

    Return a tuple of three dictionaries based on the information in file:

    - a dict of {restaurant name: rating%}
    - a dict of {price range: list of restaurant names}
    - a dict of {cuisine: list of restaurant names}
    """
    #initialize dicts
    name_to_rating = {}
    price_to_name = {'$':[], '$$':[], '$$$':[], '$$$$':[]}
    cuisine_to_name = {}

    #open file and strip away newlines and percent symbols
    filetext = open(file,'r')
    oglist = filetext.readlines()
    cleanlist = [item.rstrip() for item in oglist]
    cleanlist = [item.rstrip('%') for item in cleanlist]


    #parse list into different dicts

    linenumber = 0

    for line in cleanlist:
        if linenumber % 5 == 0:
            name = line
        elif linenumber % 5 == 1:
            rating = line
        elif linenumber % 5 == 2:
            price = line
        elif linenumber % 5 == 3:
            foods = line
        else:
            #parse foods list
            foodslist = commalist(foods)

            #add entry to first dict
            name_to_rating[name] = rating

            #use helper function to append
            add_list_dict(price_to_name, price, name)

            #for loop to add restaurant name to each food list
            for cuisine in foodslist:
                add_list_dict(cuisine_to_name, cuisine, name)

        linenumber += 1

    return name_to_rating, price_to_name, cuisine_to_name

print(read_restaurants(FILENAME))



