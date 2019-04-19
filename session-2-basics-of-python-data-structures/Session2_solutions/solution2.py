
# Part 1
def lists_to_tuples(a, b):
    return [(a[i], b[i]) for i in range(len(a))]

# Part 2
def tuples_to_dict(tuples):
    d = dict()
    for t in tuples:
        key = t[0]
        value = t[1]
        d[key] = value
    return d

def tuples_to_dict_fancy(tuples):
    d = dict()
    for (key, value) in tuples:
        d[key] = value
    return d

# Part 3
def list_to_dict(a, b):
    tuples = lists_to_tuples(a, b)
    return tuples_to_dict(tuples)

# Part 4 
def tuples_to_dict_map(tuples):
    d = dict()
    def add_to_dict(my_tuple):
        (key, value) = my_tuple
        # this is equivalent to 
        # key = my_tuple[0]
        # key = my_tuple[1]

        d[key] = value
    
    list(map(add_to_dict, tuples))
    # we force iteration

    return d
