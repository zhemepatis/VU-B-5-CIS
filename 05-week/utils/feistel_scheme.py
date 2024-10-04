def iteration(pair, func, key):
    l, r = pair
    l_result = eval(func) ^ l
    return (r, l_result)

def encrypt_ebc(pair, func, keys):
    for key in keys:
        pair = iteration(pair, func, key)

    r_result, l_result = pair
    return (l_result, r_result)

def decrypt_ebc(pair, func, keys):
    d_keys = keys[::-1]
    return encrypt_ebc(pair, func, d_keys)

def decrypt_cbc(pair, func, keys, initialisation_vector):
    d_keys = keys[::-1]

    for key in d_keys:
        pair = iteration(pair, func, key)

    r_result, l_result = pair
    return (l_result^initialisation_vector[0], r_result^initialisation_vector[1])

def decrypt_cfb(pair, func, keys, initialisation_vector):
    initialisation_vector
    for key in keys:
        initialisation_vector = iteration(initialisation_vector, func, key)

    r_result, l_result = initialisation_vector
    return (l_result^pair[0], r_result^pair[1])
