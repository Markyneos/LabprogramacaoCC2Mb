def permutations(lista:list) -> list:
    if len(lista) == 0:
        return [[]]

    first_element = lista[0]
    rest_perms = permutations(lista[1:])

    perms = []
    
    for perm in rest_perms:
        for i in range(len(perm)):
            new_perm = perm[:i] + [first_element] + perm[i:]


    return perms









numbers = [1, 5, 7]
print(permutations(numbers))