# Library for parsing files from
# http://www2.informatik.uni-freiburg.de/~cziegler/BX/BX-CSV-Dump.zip

import re

def check_isbn(isbn):
    match = re.search(r'^(\d{9})(\d|X)$', isbn)
    if not match:
        return False
    else:
        return True

def parsing_record(line):
    """ Given a record (line) from the BX dataset return type.

    Input: Line
    examples:
    "276725";"034545104X";"0" # from BX-Book-Ratings.csv
    "1";"nyc, new york, usa";NULL  # from BX-Users.csv
    Returns: dictionary with selcetd info from each type. 
    """
    line = line.replace('"', '').strip()
    words = line.split(";")
    if len(words) == 8 and check_isbn(words[0]):
        return {"record_type": "book", "isbn": words[0], "author": words[2]}  
    if len(words) == 3:
        if check_isbn(words[1]) and words[0].isdigit():
            return {"record_type": "rating", "isbn": words[1],\
                    "user": words[0], "rating": words[2]}
        if words[0].isdigit():
            return {"record_type": "user", "user": words[0],\
                    "location": words[1], "age": words[2]}
    return None

